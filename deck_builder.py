"""
IndiaBix Flashcard Generator - Deck Builder Module
Handles Anki API integration for creating flashcards
"""

from typing import List, Dict, Optional
from anki.collection import Collection
from anki.notes import Note
import time


class DeckBuilder:
    """Build Anki decks from scraped questions"""
    
    def __init__(self, collection: Collection):
        self.col = collection
    
    def get_or_create_deck(self, deck_name: str) -> int:
        """Get existing deck or create a new one"""
        deck_id = self.col.decks.id(deck_name)
        return deck_id
    
    def ensure_note_type(self) -> dict:
        """
        Ensure the IndiaBix note type exists, create if necessary
        Returns the note type (model)
        """
        model_name = "IndiaBix MCQ"
        
        # Check if model already exists
        existing_model = self.col.models.by_name(model_name)
        if existing_model:
            return existing_model
        
        # Create new note type
        model = self.col.models.new(model_name)
        
        # Add fields
        self.col.models.add_field(model, self.col.models.new_field("Question"))
        self.col.models.add_field(model, self.col.models.new_field("Options"))
        self.col.models.add_field(model, self.col.models.new_field("Answer"))
        self.col.models.add_field(model, self.col.models.new_field("Explanation"))
        
        # Add card template
        template = self.col.models.new_template("Card 1")
        
        # Front template
        template['qfmt'] = """
<div class="question">
    <h3>Question:</h3>
    {{Question}}
</div>

<div class="options">
    <h4>Options:</h4>
    {{Options}}
</div>
"""
        
        # Back template
        template['afmt'] = """
{{FrontSide}}

<hr id="answer">

<div class="answer">
    <h3 style="color: green;">Correct Answer:</h3>
    <strong>{{Answer}}</strong>
</div>

{{#Explanation}}
<div class="explanation">
    <h4>Explanation:</h4>
    {{Explanation}}
</div>
{{/Explanation}}
"""
        
        self.col.models.add_template(model, template)
        
        # Add styling
        model['css'] = """
.card {
    font-family: Arial, sans-serif;
    font-size: 16px;
    text-align: left;
    color: #000; /* Changed from #333 to pure black */
    background-color: #fff;
    padding: 20px;
}

/* Ensure all nested text is black */
.card * {
    color: #000 !important;
}

.question {
    margin-bottom: 20px;
    padding: 15px;
    background-color: #f0f8ff;
    border-left: 4px solid #2196F3;
    border-radius: 4px;
}

.question h3 {
    margin-top: 0;
    color: #000; /* Make heading black */
}

.options {
    margin-bottom: 20px;
    padding: 15px;
    background-color: #f9f9f9;
    border-radius: 4px;
}

.options h4 {
    margin-top: 0;
    color: #000; /* Make heading black */
}

.answer {
    padding: 15px;
    background-color: #e8f5e9;
    border-left: 4px solid #4CAF50;
    border-radius: 4px;
    margin-bottom: 20px;
}

.explanation {
    padding: 15px;
    background-color: #fff3e0;
    border-left: 4px solid #FF9800;
    border-radius: 4px;
    margin-top: 20px;
}

.explanation h4 {
    margin-top: 0;
    color: #000; /* Make heading black */
}

strong {
    font-size: 18px;
    color: #000; /* Ensure bold text is black */
}

hr {
    border: none;
    border-top: 2px solid #e0e0e0;
    margin: 20px 0;
}
"""
        
        # Save the model
        self.col.models.add(model)
        self.col.models.save(model)
        
        return model
    
    def format_options(self, options: Dict[str, str]) -> str:
        """Format options dictionary into HTML"""
        if not options:
            return ""
        
        html_parts = []
        for key in sorted(options.keys()):
            value = options[key]
            html_parts.append(f"<strong>{key}.</strong> {value}")
        
        return "<br>".join(html_parts)
    
    def add_question(self, 
                    deck_name: str, 
                    question_data: Dict,
                    tags: Optional[List[str]] = None,
                    include_explanation: bool = True) -> Note:
        """
        Add a single question as a flashcard
        
        Args:
            deck_name: Name of the target deck
            question_data: Dictionary with 'question', 'options', 'answer', 'explanation'
            tags: List of tags to add to the card
            include_explanation: Whether to include explanation on the back
        
        Returns:
            The created Note object
        """
        # Get deck
        deck_id = self.get_or_create_deck(deck_name)
        
        # Ensure note type exists
        model = self.ensure_note_type()
        
        # Create note
        note = Note(self.col, model)
        
        # Set deck
        note.note_type()['did'] = deck_id
        
        # Fill in fields - use HTML version if images present
        if question_data.get('has_images') and question_data.get('question_html'):
            note['Question'] = question_data['question_html']
        else:
            note['Question'] = question_data.get('question', '')
        
        note['Options'] = self.format_options(question_data.get('options', {}))
        
        # Format answer
        answer = question_data.get('answer', '')
        if answer in question_data.get('options', {}):
            answer_text = f"{answer}. {question_data['options'][answer]}"
        else:
            answer_text = answer
        note['Answer'] = answer_text
        
        # Add explanation if requested - use HTML version if images present
        if include_explanation and question_data.get('explanation'):
            if question_data.get('explanation_html'):
                note['Explanation'] = question_data['explanation_html']
            else:
                # Convert formatted text to HTML with line breaks
                explanation_text = question_data['explanation']
                # Replace double line breaks with paragraph breaks
                explanation_html = explanation_text.replace('\n\n', '</p><p>')
                # Wrap in paragraph tags
                explanation_html = f'<p>{explanation_html}</p>'
                note['Explanation'] = explanation_html
        else:
            note['Explanation'] = ""
        
        # Add tags
        if tags:
            note.tags = tags
        
        # Add note to collection
        self.col.add_note(note, deck_id)
        
        return note
    
    def add_questions_batch(self,
                           deck_name: str,
                           questions: List[Dict],
                           tags: Optional[List[str]] = None,
                           include_explanation: bool = True,
                           progress_callback=None) -> int:
        """
        Add multiple questions as flashcards
        
        Args:
            deck_name: Name of the target deck
            questions: List of question dictionaries
            tags: List of tags to add to all cards
            include_explanation: Whether to include explanations
            progress_callback: Optional callback function(current, total)
        
        Returns:
            Number of cards successfully added
        """
        added = 0
        total = len(questions)
        
        for i, question_data in enumerate(questions):
            try:
                self.add_question(
                    deck_name=deck_name,
                    question_data=question_data,
                    tags=tags,
                    include_explanation=include_explanation
                )
                added += 1
                
                if progress_callback:
                    progress_callback(i + 1, total)
                    
            except Exception as e:
                print(f"Error adding question {i+1}: {str(e)}")
                continue
        
        return added
    
    def get_deck_stats(self, deck_name: str) -> Dict:
        """Get statistics for a deck"""
        try:
            deck_id = self.col.decks.id_for_name(deck_name)
            if not deck_id:
                return {'exists': False}
            
            # Get card count
            card_count = self.col.decks.card_count(deck_id, include_subdecks=True)
            
            return {
                'exists': True,
                'id': deck_id,
                'name': deck_name,
                'card_count': card_count
            }
        except Exception as e:
            return {'exists': False, 'error': str(e)}


def test_deck_builder():
    """Test function for the deck builder"""
    from aqt import mw
    
    if not mw or not mw.col:
        print("Anki collection not available")
        return
    
    builder = DeckBuilder(mw.col)
    
    # Test data
    test_question = {
        'question': 'What is the capital of India?',
        'options': {
            'A': 'Mumbai',
            'B': 'New Delhi',
            'C': 'Kolkata',
            'D': 'Chennai'
        },
        'answer': 'B',
        'explanation': 'New Delhi is the capital of India, located in the northern part of the country.'
    }
    
    try:
        note = builder.add_question(
            deck_name="IndiaBix::Test",
            question_data=test_question,
            tags=['test', 'IndiaBix'],
            include_explanation=True
        )
        print(f"Successfully created test card with ID: {note.id}")
        
        stats = builder.get_deck_stats("IndiaBix::Test")
        print(f"Deck stats: {stats}")
        
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    test_deck_builder()
