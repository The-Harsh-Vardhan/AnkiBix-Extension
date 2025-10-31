# Architecture & Workflow Diagram

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    IndiaBix Flashcard Generator                  │
│                         Anki Add-on                              │
└─────────────────────────────────────────────────────────────────┘
                                 │
                    ┌────────────┴────────────┐
                    │                         │
        ┌───────────▼──────────┐  ┌──────────▼─────────┐
        │   User Interface     │  │   Configuration    │
        │      (ui.py)         │  │   (config.json)    │
        └───────────┬──────────┘  └────────────────────┘
                    │
                    │ URL Input
                    │
        ┌───────────▼──────────┐
        │   Web Scraper        │
        │   (scraper.py)       │
        │                      │
        │  - Fetch HTML        │
        │  - Parse Questions   │
        │  - Extract Data      │
        └───────────┬──────────┘
                    │
                    │ Question Data
                    │
        ┌───────────▼──────────┐
        │   Deck Builder       │
        │  (deck_builder.py)   │
        │                      │
        │  - Create Note Type  │
        │  - Format Cards      │
        │  - Add to Deck       │
        └───────────┬──────────┘
                    │
                    │ Flashcards
                    │
        ┌───────────▼──────────┐
        │   Anki Collection    │
        │                      │
        │  - Desktop App       │
        │  - AnkiWeb Sync      │
        │  - Mobile Apps       │
        └──────────────────────┘
```

## Data Flow

```
1. USER INPUT
   │
   ├─ IndiaBix URL
   ├─ Max Pages
   ├─ Target Deck
   └─ Options (tags, explanations)
   │
   ▼

2. SCRAPING
   │
   ├─ HTTP Request → IndiaBix Server
   ├─ Receive HTML
   ├─ Parse with BeautifulSoup
   │
   ├─ Extract:
   │   ├─ Question Text
   │   ├─ Options (A, B, C, D)
   │   ├─ Correct Answer
   │   └─ Explanation
   │
   ├─ Handle Pagination
   └─ Return Question List
   │
   ▼

3. PROCESSING
   │
   ├─ Validate Data
   ├─ Format Options as HTML
   ├─ Generate Category Tags
   └─ Create Note Objects
   │
   ▼

4. IMPORT
   │
   ├─ Create/Get Deck
   ├─ Ensure Note Type Exists
   ├─ Add Notes to Collection
   ├─ Apply Tags
   └─ Save Collection
   │
   ▼

5. RESULT
   │
   └─ Flashcards Available in Anki!
```

## Component Interaction

```
┌──────────────────┐
│   __init__.py    │  ← Entry Point
│                  │    - Registers menu action
│  ┌────────────┐  │    - Initializes add-on
│  │ Menu Hook  │  │
│  └─────┬──────┘  │
└────────┼─────────┘
         │
         │ Triggers
         ▼
┌──────────────────┐
│     ui.py        │  ← User Interface
│                  │
│  ┌────────────┐  │    - Shows dialog
│  │   Dialog   │  │    - Collects input
│  │            │  │    - Displays progress
│  │  [Input]   │  │
│  │  [Button]  │  │
│  └─────┬──────┘  │
└────────┼─────────┘
         │
         │ Calls
         ▼
┌──────────────────┐
│   scraper.py     │  ← Web Scraping
│                  │
│  ┌────────────┐  │    - Validates URL
│  │  Scraper   │  │    - Fetches pages
│  │            │  │    - Parses HTML
│  │  fetch()   │  │    - Extracts data
│  │  parse()   │  │
│  └─────┬──────┘  │
└────────┼─────────┘
         │
         │ Returns Data
         ▼
┌──────────────────┐
│ deck_builder.py  │  ← Anki Integration
│                  │
│  ┌────────────┐  │    - Creates note type
│  │  Builder   │  │    - Formats cards
│  │            │  │    - Adds to deck
│  │  create()  │  │    - Manages tags
│  │  format()  │  │
│  └─────┬──────┘  │
└────────┼─────────┘
         │
         │ Saves
         ▼
┌──────────────────┐
│  Anki Collection │  ← Storage
│                  │
│    [Database]    │    - SQLite DB
│    [Media]       │    - Note storage
│    [Decks]       │    - Sync ready
└──────────────────┘
```

## File Structure Tree

```
indiabix_flashcard_generator/
│
├── 📝 Core Python Modules
│   ├── __init__.py ............... Entry point & menu integration
│   ├── scraper.py ................ Web scraping logic
│   ├── ui.py ..................... PyQt5 GUI dialog
│   └── deck_builder.py ........... Anki API integration
│
├── ⚙️ Configuration
│   ├── manifest.json ............. Add-on metadata (Anki)
│   └── config.json ............... User settings
│
├── 📚 Documentation
│   ├── README.md ................. Main documentation
│   ├── QUICKSTART.md ............. 5-minute setup guide
│   ├── INSTALL.md ................ Installation instructions
│   ├── CONTRIBUTING.md ........... Contribution guidelines
│   ├── CHANGELOG.md .............. Version history
│   ├── PROJECT_SUMMARY.md ........ This summary
│   └── ARCHITECTURE.md ........... You are here!
│
├── 📄 Project Files
│   ├── LICENSE ................... MIT License
│   ├── requirements.txt .......... Python dependencies
│   ├── .gitignore ................ Git ignore patterns
│   └── Idea.txt .................. Original proposal
│
└── 🎯 Future Additions
    ├── tests/ .................... Unit tests (planned)
    ├── assets/ ................... Images/icons (planned)
    └── examples/ ................. Sample decks (planned)
```

## Class Diagram

```
┌─────────────────────────┐
│   IndiaBixScraper       │
├─────────────────────────┤
│ - session: Session      │
│ - timeout: int          │
│ - user_agent: str       │
├─────────────────────────┤
│ + validate_url()        │
│ + extract_category()    │
│ + fetch_page()          │
│ + parse_question()      │
│ + scrape_section()      │
│ + scrape_url()          │
└───────────┬─────────────┘
            │
            │ Used by
            ▼
┌─────────────────────────┐
│   IndiaBixDialog        │
│   (QDialog)             │
├─────────────────────────┤
│ - url_input: QLineEdit  │
│ - deck_combo: QComboBox │
│ - progress_bar: QBar    │
│ - scraper: Scraper      │
│ - scraped_data: Dict    │
├─────────────────────────┤
│ + setup_ui()            │
│ + scrape_questions()    │
│ + import_to_anki()      │
│ + add_status()          │
└───────────┬─────────────┘
            │
            │ Uses
            ▼
┌─────────────────────────┐
│     DeckBuilder         │
├─────────────────────────┤
│ - col: Collection       │
├─────────────────────────┤
│ + ensure_note_type()    │
│ + format_options()      │
│ + add_question()        │
│ + add_questions_batch() │
│ + get_deck_stats()      │
└─────────────────────────┘
```

## State Diagram (User Flow)

```
┌─────────┐
│  START  │
└────┬────┘
     │
     ▼
┌─────────────────┐
│ Open Anki       │
│ Tools → Import  │
└────┬────────────┘
     │
     ▼
┌─────────────────┐
│ Enter URL       │
│ Configure       │
└────┬────────────┘
     │
     ▼
┌─────────────────┐      ✗ Error
│ Scrape          │──────────┐
│ Questions       │          │
└────┬────────────┘          │
     │ ✓ Success             │
     ▼                       │
┌─────────────────┐          │
│ Review          │          │
│ Scraped Data    │          │
└────┬────────────┘          │
     │                       │
     ▼                       │
┌─────────────────┐          │
│ Import to       │          │
│ Anki            │          │
└────┬────────────┘          │
     │ ✓ Success             │
     ▼                       │
┌─────────────────┐          │
│ Cards Created   │          │
│ in Deck         │          │
└────┬────────────┘          │
     │                       │
     ▼                       │
┌─────────────────┐          │
│ Sync with       │          │
│ AnkiWeb         │          │
└────┬────────────┘          │
     │                       │
     ▼                       │
┌─────────────────┐          │
│ Study on        │          │
│ Any Device      │          │
└────┬────────────┘          │
     │                       │
     ▼                       │
┌─────────┐                  │
│   END   │◄─────────────────┘
└─────────┘
```

## Card Template Structure

```
┌───────────────────────────────────────┐
│          FRONT SIDE (Question)        │
├───────────────────────────────────────┤
│                                       │
│  ┌─────────────────────────────────┐ │
│  │ Question:                       │ │
│  │ {{Question}}                    │ │
│  └─────────────────────────────────┘ │
│                                       │
│  ┌─────────────────────────────────┐ │
│  │ Options:                        │ │
│  │ {{Options}}                     │ │
│  │ (Formatted as A. B. C. D.)      │ │
│  └─────────────────────────────────┘ │
│                                       │
└───────────────────────────────────────┘
                    │
                    │ User Reveals Answer
                    ▼
┌───────────────────────────────────────┐
│      BACK SIDE (Answer + Explanation) │
├───────────────────────────────────────┤
│  {{FrontSide}}                        │
│  ─────────────────────────────────    │
│                                       │
│  ┌─────────────────────────────────┐ │
│  │ ✓ Correct Answer:               │ │
│  │ {{Answer}}                      │ │
│  │ (Highlighted in green)          │ │
│  └─────────────────────────────────┘ │
│                                       │
│  ┌─────────────────────────────────┐ │
│  │ 💡 Explanation:                 │ │
│  │ {{Explanation}}                 │ │
│  │ (Optional, yellow background)   │ │
│  └─────────────────────────────────┘ │
│                                       │
└───────────────────────────────────────┘
```

## Technology Stack Layers

```
┌─────────────────────────────────────┐
│         USER INTERFACE              │
│         (Anki Desktop)              │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│      ADD-ON LAYER (This Project)    │
│                                     │
│  ┌─────────┐  ┌──────────┐         │
│  │   UI    │  │ Scraper  │         │
│  │  PyQt5  │  │   BS4    │         │
│  └─────────┘  └──────────┘         │
│                                     │
│  ┌─────────────────────────┐       │
│  │    Deck Builder         │       │
│  │    Anki API             │       │
│  └─────────────────────────┘       │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│       ANKI CORE (aqt, anki)         │
│                                     │
│  - Collection Management            │
│  - Note Types                       │
│  - Card Scheduling                  │
│  - Media Management                 │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│      STORAGE LAYER                  │
│                                     │
│  - SQLite Database                  │
│  - Media Files                      │
│  - User Preferences                 │
└─────────────────────────────────────┘
```

## Dependencies Graph

```
manifest.json
config.json
     │
     │ Read by
     ▼
__init__.py ──────────────┐
     │                    │
     │ Imports            │ Initializes
     ▼                    ▼
   ui.py                Anki Hooks
     │
     ├─────► scraper.py ──────► requests
     │            │              bs4
     │            └──────────► urllib
     │
     └─────► deck_builder.py ──► anki.collection
                   │              anki.notes
                   └──────────► aqt (Anki Qt)
```

## Error Handling Flow

```
User Action
    │
    ▼
Try: Execute Operation
    │
    ├──► Success ──► Continue
    │
    └──► Exception
         │
         ├──► Network Error
         │    └──► Retry / Show Warning
         │
         ├──► Parse Error
         │    └──► Skip Question / Log
         │
         ├──► Validation Error
         │    └──► Show Warning Dialog
         │
         └──► Anki Error
              └──► Rollback / Show Error
```

## Performance Considerations

```
Scraping Phase:
├── Network I/O (Slow)
│   └── Mitigation: Progress bar, timeout settings
│
├── HTML Parsing (Medium)
│   └── Mitigation: BeautifulSoup optimization
│
└── Data Extraction (Fast)
    └── Mitigation: Efficient regex, string ops

Import Phase:
├── Note Creation (Fast)
│   └── Mitigation: Batch processing
│
├── Database Writes (Medium)
│   └── Mitigation: Transaction batching
│
└── UI Updates (Fast)
    └── Mitigation: Progress callbacks
```

---

**This document provides a comprehensive visual overview of the system architecture.**

For implementation details, see the source code files.
For usage instructions, see README.md and QUICKSTART.md.
