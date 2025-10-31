# Changelog

All notable changes to the IndiaBix Flashcard Generator will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2025-10-31

### Added
- ⭐ **Daily Current Affairs Auto-Sync** - Automatically imports daily current affairs on Anki startup
- Smart date detection (tries today, falls back to yesterday)
- Sync history tracking to prevent duplicates
- "Sync Daily Current Affairs" menu item for manual sync
- "Manage Current Affairs" dialog with comprehensive management features
- Catch-up feature to sync multiple missed days at once
- Date range selector for bulk syncing (up to 90 days)
- Activity log showing sync operations
- Progress tracking for batch syncs
- Enable/disable auto-sync via config or UI
- Configurable target deck for current affairs
- Date-specific tagging (e.g., `current-affairs-2025-10-31`)
- Notification system for successful syncs
- Comprehensive documentation (`CURRENT_AFFAIRS_FEATURE.md`)

### Changed
- Updated version to 1.1.0
- Enhanced manifest description to mention auto-sync
- Added new config options: `auto_sync_current_affairs`, `current_affairs_deck`
- Auto-sync runs 3 seconds after Anki startup (non-intrusive)

### Technical
- New module: `auto_sync.py` - Core auto-sync logic
- New module: `current_affairs_ui.py` - Management dialog
- Sync history stored in `sync_history.json`
- QTimer integration for delayed startup sync

## [1.0.0] - 2025-10-31

### Added
- Initial release of IndiaBix Flashcard Generator
- Web scraping functionality for IndiaBix questions
- PyQt-based GUI for user input
- Automatic deck creation and management
- Category-based tagging system
- Custom note type with styled card templates
- Pagination support for multi-page sections
- Progress tracking and status updates
- Configuration system for user preferences
- Comprehensive documentation (README, INSTALL, CONTRIBUTING)

### Features
- Scrape any IndiaBix section URL
- Convert questions to MCQ-format flashcards
- Automatic category detection and tagging
- Deck selection and creation
- Optional explanation inclusion
- Beautiful card styling with color-coded sections
- Real-time progress bar during import
- Error handling and user feedback

### Documentation
- Complete README with usage instructions
- Installation guide for all platforms
- Contributing guidelines
- Code of conduct
- License (MIT)

## [Unreleased]

### Planned Features
- Support for other Q&A websites (GeeksforGeeks, LeetCode)
- Daily question scraper with automated imports
- AI-enhanced explanations using GPT
- Batch URL processing
- Custom card templates
- Export/import question sets
- Statistics and analytics dashboard
- Mobile app companion

### Known Issues
- IndiaBix HTML structure changes may break scraper
- Large imports (>500 cards) may be slow
- Some special characters may not render correctly

---

## Version History

### Version 1.0.0 (2025-10-31)
- **Status**: Initial Release
- **Changes**: First public version with core functionality
- **Contributors**: Initial development team

---

## How to Read This Changelog

- **Added**: New features
- **Changed**: Changes to existing functionality
- **Deprecated**: Features that will be removed in future versions
- **Removed**: Features that have been removed
- **Fixed**: Bug fixes
- **Security**: Security-related changes

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for information on how to contribute to this project.
