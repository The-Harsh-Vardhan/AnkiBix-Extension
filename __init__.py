"""
IndiaBix Flashcard Generator - Anki Add-on
Automatically scrape IndiaBix questions and create Anki flashcards
"""

from aqt import mw, gui_hooks
from aqt.qt import QAction, QTimer
from aqt.utils import showInfo
from . import ui
from .auto_sync import run_auto_sync, CurrentAffairsAutoSync
from .current_affairs_ui import show_current_affairs_dialog

__version__ = "1.1.0"


def show_import_dialog():
    """Show the main IndiaBix import dialog"""
    try:
        dialog = ui.IndiaBixDialog(mw)
        dialog.exec()
    except Exception as e:
        showInfo(f"Error opening IndiaBix dialog: {str(e)}")


def show_sync_current_affairs():
    """Manually trigger Current Affairs sync"""
    try:
        syncer = CurrentAffairsAutoSync()
        syncer.auto_sync(show_notifications=True)
    except Exception as e:
        showInfo(f"Error syncing Current Affairs: {str(e)}")


def show_current_affairs_manager():
    """Show Current Affairs management dialog"""
    try:
        show_current_affairs_dialog()
    except Exception as e:
        showInfo(f"Error opening Current Affairs manager: {str(e)}")


def init_addon():
    """Initialize the add-on and add menu items"""
    # Create main import action
    action = QAction("Import from IndiaBix", mw)
    action.triggered.connect(show_import_dialog)
    mw.form.menuTools.addAction(action)
    
    # Create Current Affairs sync action
    sync_action = QAction("Sync Daily Current Affairs", mw)
    sync_action.triggered.connect(show_sync_current_affairs)
    mw.form.menuTools.addAction(sync_action)
    
    # Create Current Affairs manager action
    manager_action = QAction("Manage Current Affairs", mw)
    manager_action.triggered.connect(show_current_affairs_manager)
    mw.form.menuTools.addAction(manager_action)
    
    # Run auto-sync after a short delay (to let Anki finish loading)
    QTimer.singleShot(3000, run_auto_sync)  # 3 second delay


# Initialize the add-on when Anki loads
gui_hooks.main_window_did_init.append(init_addon)
