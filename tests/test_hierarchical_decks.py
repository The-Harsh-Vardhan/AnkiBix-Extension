"""
Test hierarchical deck name generation for Current Affairs
"""

from datetime import datetime

def get_week_number(date: datetime) -> int:
    """Get the week number within the month (1-5)"""
    day = date.day
    week_num = ((day - 1) // 7) + 1
    return week_num

def get_hierarchical_deck_name(date: datetime, base_deck: str = "IndiaBix::CurrentAffairs") -> str:
    """Generate hierarchical deck name"""
    year = date.strftime("%Y")
    month = date.strftime("%B")
    week_num = get_week_number(date)
    deck_name = f"{base_deck}::{year}::{month}::Week{week_num}"
    return deck_name

# Test cases
print("=" * 80)
print("HIERARCHICAL DECK NAME TESTING")
print("=" * 80)
print()

test_dates = [
    # October 2025
    datetime(2025, 10, 1),   # Week 1
    datetime(2025, 10, 7),   # Week 1 (last day)
    datetime(2025, 10, 8),   # Week 2 (first day)
    datetime(2025, 10, 14),  # Week 2
    datetime(2025, 10, 15),  # Week 3
    datetime(2025, 10, 21),  # Week 3
    datetime(2025, 10, 22),  # Week 4
    datetime(2025, 10, 28),  # Week 4
    datetime(2025, 10, 29),  # Week 5
    datetime(2025, 10, 30),  # Week 5
    datetime(2025, 10, 31),  # Week 5 (last day of month)
    
    # November 2025
    datetime(2025, 11, 1),   # Week 1 (new month)
    datetime(2025, 11, 8),   # Week 2
    datetime(2025, 11, 15),  # Week 3
    datetime(2025, 11, 22),  # Week 4
    datetime(2025, 11, 29),  # Week 5
    
    # December 2025
    datetime(2025, 12, 1),   # Week 1
    datetime(2025, 12, 25),  # Week 4 (Christmas)
    datetime(2025, 12, 31),  # Week 5 (New Year's Eve)
]

print("Testing deck name generation for various dates:")
print()

current_month = None
for date in test_dates:
    deck_name = get_hierarchical_deck_name(date)
    day_name = date.strftime("%A")
    
    # Add separator for new month
    month = date.strftime("%B %Y")
    if month != current_month:
        if current_month is not None:
            print()
        print(f"📅 {month}")
        print("-" * 80)
        current_month = month
    
    print(f"  {date.strftime('%Y-%m-%d')} ({day_name:9s}) → {deck_name}")

print()
print("=" * 80)
print("DECK HIERARCHY STRUCTURE")
print("=" * 80)
print()
print("IndiaBix")
print("└── CurrentAffairs")
print("    ├── 2025")
print("    │   ├── October")
print("    │   │   ├── Week1 (Oct 1-7)")
print("    │   │   ├── Week2 (Oct 8-14)")
print("    │   │   ├── Week3 (Oct 15-21)")
print("    │   │   ├── Week4 (Oct 22-28)")
print("    │   │   └── Week5 (Oct 29-31)")
print("    │   ├── November")
print("    │   │   ├── Week1 (Nov 1-7)")
print("    │   │   ├── Week2 (Nov 8-14)")
print("    │   │   ├── Week3 (Nov 15-21)")
print("    │   │   ├── Week4 (Nov 22-28)")
print("    │   │   └── Week5 (Nov 29-30)")
print("    │   └── December")
print("    │       ├── Week1 (Dec 1-7)")
print("    │       ├── Week2 (Dec 8-14)")
print("    │       ├── Week3 (Dec 15-21)")
print("    │       ├── Week4 (Dec 22-28)")
print("    │       └── Week5 (Dec 29-31)")
print("    └── 2026")
print("        └── (and so on...)")
print()

print("=" * 80)
print("BENEFITS OF THIS STRUCTURE")
print("=" * 80)
print()
print("✅ Easy to browse by time period")
print("✅ Manageable chunk sizes (~70 questions per week)")
print("✅ Clear organization by year, month, and week")
print("✅ Can study specific weeks easily")
print("✅ Can review entire months together")
print("✅ Automatic subdeck creation - no manual work!")
print()
