"""
Current Affairs Management Dialog
Allows users to sync missed days and manage auto-sync settings
"""

from datetime import datetime, timedelta
from typing import Optional

from aqt import mw
from aqt.qt import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QDateEdit, QCheckBox, QProgressBar, QTextEdit, Qt, QGroupBox
)
from aqt.utils import showInfo, tooltip

from .auto_sync import CurrentAffairsAutoSync


class CurrentAffairsDialog(QDialog):
    """Dialog for managing Current Affairs auto-sync"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.syncer = CurrentAffairsAutoSync()
        self.config = mw.addonManager.getConfig(__name__)
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the user interface"""
        self.setWindowTitle("Current Affairs Auto-Sync")
        self.setMinimumWidth(500)
        self.setMinimumHeight(400)
        
        layout = QVBoxLayout()
        
        # Status Section
        status_group = QGroupBox("Status")
        status_layout = QVBoxLayout()
        
        self.status_label = QLabel()
        self.update_status()
        status_layout.addWidget(self.status_label)
        
        status_group.setLayout(status_layout)
        layout.addWidget(status_group)
        
        # Settings Section
        settings_group = QGroupBox("Settings")
        settings_layout = QVBoxLayout()
        
        self.auto_sync_checkbox = QCheckBox("Enable auto-sync on Anki startup")
        self.auto_sync_checkbox.setChecked(
            self.config.get('auto_sync_current_affairs', True)
        )
        self.auto_sync_checkbox.stateChanged.connect(self.toggle_auto_sync)
        settings_layout.addWidget(self.auto_sync_checkbox)
        
        deck_label = QLabel(f"Target Deck: {self.config.get('current_affairs_deck', 'IndiaBix::CurrentAffairs')}")
        settings_layout.addWidget(deck_label)
        
        settings_group.setLayout(settings_layout)
        layout.addWidget(settings_group)
        
        # Catch-up Section
        catchup_group = QGroupBox("Catch Up on Missed Days")
        catchup_layout = QVBoxLayout()
        
        date_layout = QHBoxLayout()
        date_layout.addWidget(QLabel("From:"))
        self.start_date = QDateEdit()
        self.start_date.setCalendarPopup(True)
        self.start_date.setDate(datetime.now() - timedelta(days=7))
        date_layout.addWidget(self.start_date)
        
        date_layout.addWidget(QLabel("To:"))
        self.end_date = QDateEdit()
        self.end_date.setCalendarPopup(True)
        self.end_date.setDate(datetime.now())
        date_layout.addWidget(self.end_date)
        
        catchup_layout.addLayout(date_layout)
        
        self.sync_range_btn = QPushButton("Sync Date Range")
        self.sync_range_btn.clicked.connect(self.sync_date_range)
        catchup_layout.addWidget(self.sync_range_btn)
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        catchup_layout.addWidget(self.progress_bar)
        
        catchup_group.setLayout(catchup_layout)
        layout.addWidget(catchup_group)
        
        # Log Section
        log_group = QGroupBox("Activity Log")
        log_layout = QVBoxLayout()
        
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.log_text.setMaximumHeight(150)
        log_layout.addWidget(self.log_text)
        
        log_group.setLayout(log_layout)
        layout.addWidget(log_group)
        
        # Action Buttons
        button_layout = QHBoxLayout()
        
        self.sync_now_btn = QPushButton("Sync Today")
        self.sync_now_btn.clicked.connect(self.sync_now)
        button_layout.addWidget(self.sync_now_btn)
        
        self.close_btn = QPushButton("Close")
        self.close_btn.clicked.connect(self.close)
        button_layout.addWidget(self.close_btn)
        
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
        
        # Check for missing dates
        self.check_missing_dates()
    
    def update_status(self):
        """Update the status label"""
        today = datetime.now().strftime("%Y-%m-%d")
        yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        
        today_synced = self.syncer.is_date_synced(today)
        yesterday_synced = self.syncer.is_date_synced(yesterday)
        
        status_text = f"📅 Today ({today}): {'✅ Synced' if today_synced else '❌ Not synced'}\n"
        status_text += f"📅 Yesterday ({yesterday}): {'✅ Synced' if yesterday_synced else '❌ Not synced'}"
        
        self.status_label.setText(status_text)
    
    def check_missing_dates(self):
        """Check and display missing dates"""
        missing = self.syncer.get_missing_dates(days_back=30)
        if missing:
            self.log(f"⚠️ Found {len(missing)} missing days in the last 30 days")
            if len(missing) <= 5:
                self.log(f"Missing dates: {', '.join(missing[:5])}")
    
    def log(self, message: str):
        """Add message to log"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_text.append(f"[{timestamp}] {message}")
    
    def toggle_auto_sync(self, state):
        """Toggle auto-sync setting"""
        enabled = state == Qt.CheckState.Checked
        self.config['auto_sync_current_affairs'] = enabled
        mw.addonManager.writeConfig(__name__, self.config)
        self.log(f"Auto-sync {'enabled' if enabled else 'disabled'}")
    
    def sync_now(self):
        """Manually sync today's current affairs"""
        self.sync_now_btn.setEnabled(False)
        self.log("Starting manual sync...")
        
        try:
            self.syncer.auto_sync(show_notifications=False)
            self.log("✅ Sync completed")
            self.update_status()
        except Exception as e:
            self.log(f"❌ Error: {str(e)}")
        finally:
            self.sync_now_btn.setEnabled(True)
    
    def sync_date_range(self):
        """Sync a range of dates"""
        start_date = self.start_date.date().toPyDate()
        end_date = self.end_date.date().toPyDate()
        
        if start_date > end_date:
            showInfo("Start date must be before end date")
            return
        
        days = (end_date - start_date).days + 1
        if days > 90:
            showInfo("Please select a range of 90 days or less")
            return
        
        self.sync_range_btn.setEnabled(False)
        self.progress_bar.setVisible(True)
        self.progress_bar.setMaximum(days)
        self.progress_bar.setValue(0)
        
        self.log(f"Starting sync for {days} days...")
        
        try:
            start_dt = datetime.combine(start_date, datetime.min.time())
            end_dt = datetime.combine(end_date, datetime.min.time())
            
            def progress_callback(current_date, stats):
                days_done = (current_date - start_dt).days + 1
                self.progress_bar.setValue(days_done)
                self.log(f"Processed {current_date.strftime('%Y-%m-%d')}: "
                        f"Synced={stats['synced']}, Skipped={stats['skipped']}, Failed={stats['failed']}")
            
            stats = self.syncer.sync_date_range(start_dt, end_dt, progress_callback)
            
            self.log(f"✅ Completed: {stats['synced']} synced, "
                    f"{stats['skipped']} skipped, {stats['failed']} failed")
            self.update_status()
            
            tooltip(f"Sync complete! {stats['synced']} new days added.", period=3000)
            
        except Exception as e:
            self.log(f"❌ Error: {str(e)}")
            showInfo(f"Error during sync: {str(e)}")
        finally:
            self.sync_range_btn.setEnabled(True)
            self.progress_bar.setVisible(False)


def show_current_affairs_dialog():
    """Show the Current Affairs management dialog"""
    dialog = CurrentAffairsDialog(mw)
    dialog.exec()
