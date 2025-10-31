"""
IndiaBix Flashcard Generator - Anki Add-on
Automatically scrape IndiaBix questions and create Anki flashcards
"""

from aqt import mw, gui_hooks
from aqt.qt import QAction
from aqt.utils import showInfo
from . import ui

__version__ = "1.0.0"


def show_import_dialog():
    """Show the main IndiaBix import dialog"""
    try:
        dialog = ui.IndiaBixDialog(mw)
        dialog.exec()
    except Exception as e:
        showInfo(f"Error opening IndiaBix dialog: {str(e)}")


def init_addon():
    """Initialize the add-on and add menu items"""
    # Create menu action
    action = QAction("Import from IndiaBix", mw)
    action.triggered.connect(show_import_dialog)
    
    # Add to Tools menu
    mw.form.menuTools.addAction(action)


# Initialize the add-on when Anki loads
gui_hooks.main_window_did_init.append(init_addon)
