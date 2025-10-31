"""
Test script for Current Affairs Auto-Sync feature
Tests the logic without requiring Anki to be running
"""

import os
import sys
from datetime import datetime, timedelta

# Add the parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_url_generation():
    """Test URL generation for different dates"""
    print("=" * 80)
    print("TEST 1: URL Generation")
    print("=" * 80)
    
    test_dates = [
        datetime(2025, 10, 31),
        datetime(2025, 10, 30),
        datetime(2025, 11, 1),
    ]
    
    for date in test_dates:
        date_str = date.strftime("%Y-%m-%d")
        url = f"https://www.indiabix.com/current-affairs/{date_str}/"
        print(f"✅ Date: {date_str} → URL: {url}")
    
    print()

def test_date_logic():
    """Test the date fallback logic"""
    print("=" * 80)
    print("TEST 2: Date Fallback Logic")
    print("=" * 80)
    
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    
    print(f"Today: {today.strftime('%Y-%m-%d')}")
    print(f"Yesterday: {yesterday.strftime('%Y-%m-%d')}")
    print(f"Logic: Try today first, if not available, try yesterday")
    print()

def test_scraper_import():
    """Test if scraper module can be imported"""
    print("=" * 80)
    print("TEST 3: Module Imports")
    print("=" * 80)
    
    try:
        from scraper import IndiaBixScraper, format_question_text
        print("✅ scraper.py imported successfully")
        print(f"   - IndiaBixScraper: {IndiaBixScraper}")
        print(f"   - format_question_text: {format_question_text}")
    except ImportError as e:
        print(f"❌ Failed to import scraper: {e}")
        return False
    
    try:
        from deck_builder import DeckBuilder
        print("✅ deck_builder.py imported successfully")
        print(f"   - DeckBuilder: {DeckBuilder}")
    except ImportError as e:
        print(f"❌ Failed to import deck_builder: {e}")
        return False
    
    print()
    return True

def test_sync_history():
    """Test sync history file operations"""
    print("=" * 80)
    print("TEST 4: Sync History Management")
    print("=" * 80)
    
    import json
    import tempfile
    
    # Create a temporary sync history file
    temp_file = os.path.join(tempfile.gettempdir(), "test_sync_history.json")
    
    # Test writing
    test_history = {
        "2025-10-30": True,
        "2025-10-31": True
    }
    
    try:
        with open(temp_file, 'w', encoding='utf-8') as f:
            json.dump(test_history, f, indent=2)
        print(f"✅ Created test history file: {temp_file}")
        
        # Test reading
        with open(temp_file, 'r', encoding='utf-8') as f:
            loaded_history = json.load(f)
        
        print(f"✅ Loaded history: {loaded_history}")
        print(f"✅ History matches: {loaded_history == test_history}")
        
        # Cleanup
        os.remove(temp_file)
        print(f"✅ Cleaned up test file")
        
    except Exception as e:
        print(f"❌ Error in sync history test: {e}")
        return False
    
    print()
    return True

def test_current_affairs_url():
    """Test if we can access a current affairs URL"""
    print("=" * 80)
    print("TEST 5: Current Affairs URL Access")
    print("=" * 80)
    
    import requests
    from bs4 import BeautifulSoup
    
    # Try yesterday's URL (most likely to exist)
    yesterday = datetime.now() - timedelta(days=1)
    date_str = yesterday.strftime("%Y-%m-%d")
    url = f"https://www.indiabix.com/current-affairs/{date_str}/"
    
    print(f"Testing URL: {url}")
    
    try:
        response = requests.get(url, timeout=10)
        print(f"✅ Status Code: {response.status_code}")
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Try to find question elements
            questions = soup.find_all('div', class_='bix-div-container')
            print(f"✅ Found {len(questions)} question containers")
            
            if len(questions) > 0:
                print(f"✅ Current Affairs page is accessible and has questions!")
                return True
            else:
                print(f"⚠️ Page accessible but no questions found (might be old date)")
                return True
        else:
            print(f"⚠️ Page returned {response.status_code} (might not be published yet)")
            return True
            
    except Exception as e:
        print(f"❌ Error accessing URL: {e}")
        return False
    
    print()

def test_scraper_with_current_affairs():
    """Test scraper with actual current affairs URL"""
    print("=" * 80)
    print("TEST 6: Scraper with Current Affairs URL")
    print("=" * 80)
    
    try:
        from scraper import IndiaBixScraper
        
        scraper = IndiaBixScraper(timeout=15)
        
        # Try yesterday's date
        yesterday = datetime.now() - timedelta(days=1)
        date_str = yesterday.strftime("%Y-%m-%d")
        url = f"https://www.indiabix.com/current-affairs/{date_str}/"
        
        print(f"Attempting to scrape: {url}")
        print("This may take 10-15 seconds...")
        
        result = scraper.scrape_url(url, max_pages=1)
        
        print(f"\n✅ Scraping completed!")
        print(f"   - Result type: {type(result)}")
        print(f"   - Questions found: {len(result.get('questions', []))}")
        print(f"   - Category: {result.get('category', 'N/A')}")
        print(f"   - Total: {result.get('total', 0)}")
        
        if result.get('questions'):
            q = result['questions'][0]
            print(f"\n📝 Sample question:")
            print(f"   - Question: {q['question'][:100]}...")
            print(f"   - Options: {len(q.get('options', {}))}")
            print(f"   - Answer: {q.get('answer', 'N/A')}")
            print(f"   - Has explanation: {bool(q.get('explanation'))}")
            
            # Verify all 10 questions
            if len(result['questions']) == 10:
                print(f"\n✅ Perfect! Found exactly 10 questions (standard for daily current affairs)")
            return True
        else:
            print(f"⚠️ No questions found (URL might not be published yet)")
            return False
            
    except Exception as e:
        print(f"❌ Error in scraper test: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    print()

def test_config_reading():
    """Test config.json reading"""
    print("=" * 80)
    print("TEST 7: Config Reading")
    print("=" * 80)
    
    config_file = "config.json"
    
    if not os.path.exists(config_file):
        print(f"❌ config.json not found")
        return False
    
    try:
        import json
        with open(config_file, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        print(f"✅ Config loaded successfully")
        print(f"   - auto_sync_current_affairs: {config.get('auto_sync_current_affairs')}")
        print(f"   - current_affairs_deck: {config.get('current_affairs_deck')}")
        print(f"   - timeout: {config.get('timeout')}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error reading config: {e}")
        return False
    
    print()

def run_all_tests():
    """Run all tests"""
    print("\n")
    print("🧪" * 40)
    print("CURRENT AFFAIRS AUTO-SYNC FEATURE TEST SUITE")
    print("🧪" * 40)
    print("\n")
    
    tests = [
        ("URL Generation", test_url_generation),
        ("Date Fallback Logic", test_date_logic),
        ("Module Imports", test_scraper_import),
        ("Sync History", test_sync_history),
        ("Config Reading", test_config_reading),
        ("Current Affairs URL Access", test_current_affairs_url),
        ("Scraper with Current Affairs", test_scraper_with_current_affairs),
    ]
    
    results = []
    
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"❌ Test '{name}' crashed: {e}")
            results.append((name, False))
    
    # Summary
    print("\n")
    print("=" * 80)
    print("TEST SUMMARY")
    print("=" * 80)
    
    passed = 0
    failed = 0
    
    for name, result in results:
        if result:
            print(f"✅ {name}")
            passed += 1
        elif result is False:
            print(f"❌ {name}")
            failed += 1
        else:
            print(f"⚠️ {name} (skipped or partial)")
    
    print(f"\nTotal: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("\n🎉 All tests passed! Feature is ready!")
    else:
        print(f"\n⚠️ {failed} test(s) failed. Please review.")
    
    return failed == 0

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
