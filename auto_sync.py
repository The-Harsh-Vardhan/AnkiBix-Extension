"""
Auto-sync module for daily Current Affairs
Automatically imports daily current affairs questions on Anki startup
"""

import os
import json
from datetime import datetime, timedelta
from typing import Optional, Dict, List
from aqt import mw
from aqt.utils import showInfo, tooltip
from .scraper import IndiaBixScraper
from .deck_builder import DeckBuilder


class CurrentAffairsAutoSync:
    """Handles automatic daily syncing of Current Affairs"""
    
    def __init__(self):
        self.addon_dir = os.path.dirname(__file__)
        self.sync_file = os.path.join(self.addon_dir, "sync_history.json")
        self.config = mw.addonManager.getConfig(__name__)
        
    def get_sync_history(self) -> Dict[str, bool]:
        """Load sync history from file"""
        if os.path.exists(self.sync_file):
            try:
                with open(self.sync_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error loading sync history: {e}")
                return {}
        return {}
    
    def save_sync_history(self, history: Dict[str, bool]):
        """Save sync history to file"""
        try:
            with open(self.sync_file, 'w', encoding='utf-8') as f:
                json.dump(history, f, indent=2)
        except Exception as e:
            print(f"Error saving sync history: {e}")
    
    def mark_date_synced(self, date_str: str):
        """Mark a date as synced"""
        history = self.get_sync_history()
        history[date_str] = True
        self.save_sync_history(history)
    
    def is_date_synced(self, date_str: str) -> bool:
        """Check if a date has been synced"""
        history = self.get_sync_history()
        return history.get(date_str, False)
    
    def get_current_affairs_url(self, date: datetime) -> str:
        """Generate URL for a specific date's current affairs"""
        date_str = date.strftime("%Y-%m-%d")
        return f"https://www.indiabix.com/current-affairs/{date_str}/"
    
    def get_week_number(self, date: datetime) -> int:
        """Get the week number within the month (1-5)"""
        # Get the day of the month
        day = date.day
        # Calculate week number (1-based)
        week_num = ((day - 1) // 7) + 1
        return week_num
    
    def get_hierarchical_deck_name(self, date: datetime) -> str:
        """
        Generate hierarchical deck name: 
        IndiaBix::CurrentAffairs::YYYY::Month::WeekN
        
        Example: IndiaBix::CurrentAffairs::2025::October::Week1
        """
        base_deck = self.config.get('current_affairs_deck', 'IndiaBix::CurrentAffairs')
        
        # Get year, month name, and week number
        year = date.strftime("%Y")
        month = date.strftime("%B")  # Full month name (e.g., "October")
        week_num = self.get_week_number(date)
        
        # Build hierarchical deck name
        deck_name = f"{base_deck}::{year}::{month}::Week{week_num}"
        
        return deck_name
    
    def try_sync_date(self, date: datetime) -> Optional[Dict]:
        """Try to sync current affairs for a specific date"""
        date_str = date.strftime("%Y-%m-%d")
        
        # Check if already synced
        if self.is_date_synced(date_str):
            print(f"Current Affairs for {date_str} already synced")
            return None
        
        # Try to scrape
        url = self.get_current_affairs_url(date)
        print(f"Attempting to sync Current Affairs from: {url}")
        
        try:
            scraper = IndiaBixScraper(timeout=self.config.get('timeout', 30))
            result = scraper.scrape_url(url, max_pages=1)
            
            if result and result.get('questions'):
                return {
                    'date': date_str,
                    'questions': result['questions'],
                    'count': len(result['questions'])
                }
            else:
                print(f"No questions found for {date_str}")
                return None
                
        except Exception as e:
            print(f"Error syncing {date_str}: {str(e)}")
            return None
    
    def auto_sync(self, show_notifications: bool = True):
        """
        Automatically sync current affairs
        Tries today first, then falls back to yesterday
        """
        # Check if auto-sync is enabled
        if not self.config.get('auto_sync_current_affairs', True):
            print("Auto-sync is disabled")
            return
        
        today = datetime.now()
        yesterday = today - timedelta(days=1)
        
        # Try today first
        result = self.try_sync_date(today)
        
        # If today not available, try yesterday
        if not result:
            result = self.try_sync_date(yesterday)
        
        # If still no result, nothing to sync
        if not result:
            print("No new Current Affairs to sync")
            return
        
        # Import to Anki
        try:
            # Parse the date to create hierarchical deck name
            date_obj = datetime.strptime(result['date'], "%Y-%m-%d")
            deck_name = self.get_hierarchical_deck_name(date_obj)
            
            builder = DeckBuilder(mw.col)
            
            # Add date tag
            date_tag = f"current-affairs-{result['date']}"
            tags = ['IndiaBix', 'CurrentAffairs', date_tag]
            
            # Import questions
            added = builder.add_questions_batch(
                deck_name=deck_name,
                questions=result['questions'],
                tags=tags,
                include_explanation=self.config.get('include_explanation', True)
            )
            
            # Mark as synced
            self.mark_date_synced(result['date'])
            
            # Show notification
            if show_notifications and added > 0:
                message = f"✅ Current Affairs synced!\n\n📅 Date: {result['date']}\n📚 Questions: {added}\n🎯 Deck: {deck_name}"
                tooltip(message, period=5000)
                print(f"Successfully synced {added} questions for {result['date']}")
            
        except Exception as e:
            error_msg = f"Error importing Current Affairs: {str(e)}"
            print(error_msg)
            if show_notifications:
                showInfo(error_msg)
    
    def sync_date_range(self, start_date: datetime, end_date: datetime, 
                       progress_callback=None) -> Dict[str, int]:
        """
        Sync multiple dates (for catching up on missed days)
        Returns dict with stats
        """
        stats = {'synced': 0, 'skipped': 0, 'failed': 0}
        current_date = start_date
        
        while current_date <= end_date:
            date_str = current_date.strftime("%Y-%m-%d")
            
            if self.is_date_synced(date_str):
                stats['skipped'] += 1
            else:
                result = self.try_sync_date(current_date)
                if result:
                    try:
                        # Use hierarchical deck name
                        deck_name = self.get_hierarchical_deck_name(current_date)
                        builder = DeckBuilder(mw.col)
                        date_tag = f"current-affairs-{result['date']}"
                        tags = ['IndiaBix', 'CurrentAffairs', date_tag]
                        
                        added = builder.add_questions_batch(
                            deck_name=deck_name,
                            questions=result['questions'],
                            tags=tags,
                            include_explanation=self.config.get('include_explanation', True)
                        )
                        
                        if added > 0:
                            self.mark_date_synced(result['date'])
                            stats['synced'] += 1
                        else:
                            stats['failed'] += 1
                    except Exception as e:
                        print(f"Error importing {date_str}: {e}")
                        stats['failed'] += 1
                else:
                    stats['failed'] += 1
            
            if progress_callback:
                progress_callback(current_date, stats)
            
            current_date += timedelta(days=1)
        
        return stats
    
    def get_missing_dates(self, days_back: int = 30) -> List[str]:
        """Get list of dates that haven't been synced"""
        missing = []
        today = datetime.now()
        
        for i in range(days_back):
            check_date = today - timedelta(days=i)
            date_str = check_date.strftime("%Y-%m-%d")
            if not self.is_date_synced(date_str):
                missing.append(date_str)
        
        return missing


def run_auto_sync():
    """Run auto-sync on startup"""
    try:
        syncer = CurrentAffairsAutoSync()
        syncer.auto_sync(show_notifications=True)
    except Exception as e:
        print(f"Auto-sync error: {str(e)}")
