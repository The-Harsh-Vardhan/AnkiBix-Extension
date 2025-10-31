"""
IndiaBix Flashcard Generator - User Interface Module
PyQt dialog for user input and configuration
"""

from aqt import mw
from aqt.qt import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QSpinBox, QProgressBar,
    QTextEdit, QGroupBox, QMessageBox, Qt
)
from aqt.utils import showInfo, showWarning, tooltip
from typing import Optional
import json

from . import scraper
from . import deck_builder


class IndiaBixDialog(QDialog):
    """Main dialog for IndiaBix import"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.scraper = None
        self.scraped_data = None
        self.setWindowTitle("IndiaBix Flashcard Generator")
        self.setMinimumWidth(600)
        self.setMinimumHeight(500)
        self.setup_ui()
        self.load_config()
    
    def load_config(self):
        """Load configuration from config.json"""
        try:
            config = mw.addonManager.getConfig(__name__)
            if config:
                self.default_deck = config.get('default_deck', 'IndiaBix::General')
                self.auto_tag = config.get('auto_tag', True)
                self.timeout = config.get('timeout', 30)
        except Exception as e:
            print(f"Error loading config: {e}")
            self.default_deck = 'IndiaBix::General'
            self.auto_tag = True
            self.timeout = 30
    
    def setup_ui(self):
        """Setup the user interface"""
        layout = QVBoxLayout()
        
        # URL Input Section
        url_group = QGroupBox("Step 1: Enter IndiaBix URL")
        url_layout = QVBoxLayout()
        
        url_label = QLabel("Enter the IndiaBix section URL:")
        url_layout.addWidget(url_label)
        
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("e.g., https://www.indiabix.com/general-knowledge/basic-general-knowledge/")
        url_layout.addWidget(self.url_input)
        
        example_label = QLabel("Examples:\n"
                              "• https://www.indiabix.com/general-knowledge/basic-general-knowledge/\n"
                              "• https://www.indiabix.com/logical-reasoning/blood-relations/\n"
                              "• https://www.indiabix.com/aptitude/numbers/")
        example_label.setStyleSheet("color: gray; font-size: 9pt;")
        url_layout.addWidget(example_label)
        
        url_group.setLayout(url_layout)
        layout.addWidget(url_group)
        
        # Scraping Options Section
        options_group = QGroupBox("Step 2: Configure Options")
        options_layout = QVBoxLayout()
        
        # Max pages
        pages_layout = QHBoxLayout()
        pages_label = QLabel("Maximum pages to scrape:")
        self.max_pages_spin = QSpinBox()
        self.max_pages_spin.setMinimum(1)
        self.max_pages_spin.setMaximum(100)
        self.max_pages_spin.setValue(5)
        pages_layout.addWidget(pages_label)
        pages_layout.addWidget(self.max_pages_spin)
        pages_layout.addStretch()
        options_layout.addLayout(pages_layout)
        
        # Deck selection
        deck_layout = QHBoxLayout()
        deck_label = QLabel("Target Deck:")
        self.deck_combo = QComboBox()
        self.populate_decks()
        deck_layout.addWidget(deck_label)
        deck_layout.addWidget(self.deck_combo)
        
        self.new_deck_button = QPushButton("New Deck")
        self.new_deck_button.clicked.connect(self.create_new_deck)
        deck_layout.addWidget(self.new_deck_button)
        options_layout.addLayout(deck_layout)
        
        # Tag options
        self.auto_tag_checkbox = QCheckBox("Automatically tag cards with category")
        self.auto_tag_checkbox.setChecked(True)
        options_layout.addWidget(self.auto_tag_checkbox)
        
        self.include_explanation_checkbox = QCheckBox("Include explanation on card back")
        self.include_explanation_checkbox.setChecked(True)
        options_layout.addWidget(self.include_explanation_checkbox)
        
        options_group.setLayout(options_layout)
        layout.addWidget(options_group)
        
        # Progress Section
        progress_group = QGroupBox("Step 3: Import Cards")
        progress_layout = QVBoxLayout()
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        progress_layout.addWidget(self.progress_bar)
        
        self.status_text = QTextEdit()
        self.status_text.setReadOnly(True)
        self.status_text.setMaximumHeight(100)
        self.status_text.setPlaceholderText("Status messages will appear here...")
        progress_layout.addWidget(self.status_text)
        
        progress_group.setLayout(progress_layout)
        layout.addWidget(progress_group)
        
        # Action Buttons
        button_layout = QHBoxLayout()
        
        self.scrape_button = QPushButton("Scrape Questions")
        self.scrape_button.clicked.connect(self.scrape_questions)
        self.scrape_button.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold;")
        button_layout.addWidget(self.scrape_button)
        
        self.import_button = QPushButton("Import to Anki")
        self.import_button.clicked.connect(self.import_to_anki)
        self.import_button.setEnabled(False)
        self.import_button.setStyleSheet("background-color: #2196F3; color: white; font-weight: bold;")
        button_layout.addWidget(self.import_button)
        
        self.close_button = QPushButton("Close")
        self.close_button.clicked.connect(self.close)
        button_layout.addWidget(self.close_button)
        
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
    
    def populate_decks(self):
        """Populate the deck combo box with existing decks"""
        self.deck_combo.clear()
        deck_names = sorted([d.name for d in mw.col.decks.all()])
        self.deck_combo.addItems(deck_names)
        
        # Try to select default deck
        try:
            default_index = deck_names.index(self.default_deck)
            self.deck_combo.setCurrentIndex(default_index)
        except ValueError:
            pass
    
    def create_new_deck(self):
        """Create a new deck"""
        from aqt.utils import getText
        
        deck_name, ok = getText("Enter new deck name:", 
                               title="Create New Deck",
                               default="IndiaBix::MyCategory")
        
        if ok and deck_name:
            try:
                deck_id = mw.col.decks.id(deck_name)
                mw.col.decks.save(mw.col.decks.get(deck_id))
                self.populate_decks()
                
                # Select the newly created deck
                index = self.deck_combo.findText(deck_name)
                if index >= 0:
                    self.deck_combo.setCurrentIndex(index)
                
                tooltip(f"Deck '{deck_name}' created successfully!")
            except Exception as e:
                showWarning(f"Error creating deck: {str(e)}")
    
    def add_status(self, message: str):
        """Add a status message to the text area"""
        self.status_text.append(message)
        # Scroll to bottom
        self.status_text.verticalScrollBar().setValue(
            self.status_text.verticalScrollBar().maximum()
        )
    
    def scrape_questions(self):
        """Scrape questions from the provided URL"""
        url = self.url_input.text().strip()
        
        if not url:
            showWarning("Please enter a valid IndiaBix URL")
            return
        
        # Disable buttons during scraping
        self.scrape_button.setEnabled(False)
        self.import_button.setEnabled(False)
        self.progress_bar.setVisible(True)
        self.progress_bar.setRange(0, 0)  # Indeterminate progress
        
        self.status_text.clear()
        self.add_status(f"Starting scraper for: {url}")
        
        try:
            # Initialize scraper
            self.scraper = scraper.IndiaBixScraper(timeout=self.timeout)
            
            # Validate URL
            if not self.scraper.validate_url(url):
                raise ValueError("Invalid IndiaBix URL. Please check the URL and try again.")
            
            self.add_status("URL validated successfully")
            
            # Scrape questions
            max_pages = self.max_pages_spin.value()
            self.add_status(f"Scraping up to {max_pages} pages...")
            
            self.scraped_data = self.scraper.scrape_url(url, max_pages=max_pages)
            
            total = self.scraped_data['total']
            category = self.scraped_data['category']
            
            if total == 0:
                raise Exception("No questions found. The page structure may have changed.")
            
            self.add_status(f"✓ Successfully scraped {total} questions from '{category}'")
            self.add_status(f"Ready to import into Anki deck: {self.deck_combo.currentText()}")
            
            # Enable import button
            self.import_button.setEnabled(True)
            tooltip(f"Successfully scraped {total} questions!")
            
        except Exception as e:
            self.add_status(f"✗ Error: {str(e)}")
            showWarning(f"Scraping failed: {str(e)}")
        
        finally:
            self.scrape_button.setEnabled(True)
            self.progress_bar.setVisible(False)
    
    def import_to_anki(self):
        """Import scraped questions to Anki"""
        if not self.scraped_data or not self.scraped_data.get('questions'):
            showWarning("No questions to import. Please scrape questions first.")
            return
        
        deck_name = self.deck_combo.currentText()
        if not deck_name:
            showWarning("Please select a target deck")
            return
        
        # Disable buttons during import
        self.scrape_button.setEnabled(False)
        self.import_button.setEnabled(False)
        self.progress_bar.setVisible(True)
        self.progress_bar.setRange(0, len(self.scraped_data['questions']))
        self.progress_bar.setValue(0)
        
        self.add_status(f"\nImporting {len(self.scraped_data['questions'])} cards to '{deck_name}'...")
        
        try:
            # Prepare tags
            tags = []
            if self.auto_tag_checkbox.isChecked():
                category = self.scraped_data['category']
                tags.append(category.replace('::', '_').replace(' ', '_'))
            tags.append('IndiaBix')
            
            # Initialize deck builder
            builder = deck_builder.DeckBuilder(mw.col)
            
            # Import questions
            imported = 0
            for i, question in enumerate(self.scraped_data['questions']):
                try:
                    builder.add_question(
                        deck_name=deck_name,
                        question_data=question,
                        tags=tags,
                        include_explanation=self.include_explanation_checkbox.isChecked()
                    )
                    imported += 1
                    self.progress_bar.setValue(i + 1)
                except Exception as e:
                    self.add_status(f"Warning: Failed to import question {i+1}: {str(e)}")
            
            # Save changes
            mw.col.reset()
            mw.reset()
            
            self.add_status(f"✓ Successfully imported {imported} out of {len(self.scraped_data['questions'])} cards!")
            self.add_status("Cards are now available in your Anki collection.")
            
            showInfo(f"Successfully imported {imported} flashcards to deck '{deck_name}'!\n\n"
                    f"You can now study these cards or sync them to AnkiWeb.")
            
        except Exception as e:
            self.add_status(f"✗ Import Error: {str(e)}")
            showWarning(f"Import failed: {str(e)}")
        
        finally:
            self.scrape_button.setEnabled(True)
            self.import_button.setEnabled(True)
            self.progress_bar.setVisible(False)
