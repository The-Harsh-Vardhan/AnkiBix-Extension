# IndiaBix Flashcard Generator v1.0.0 - Initial Release 🎉

**Release Date:** October 31, 2025

## 🌟 What's New

This is the **first official release** of IndiaBix Flashcard Generator - an Anki add-on that automatically imports multiple-choice questions from IndiaBix.com into your Anki decks!

## ✨ Key Features

### 🔍 Smart Web Scraping
- Automatically scrapes questions from IndiaBix.com
- Handles multi-page sections with intelligent pagination
- Supports text questions, images, and code snippets
- Error-resistant with graceful failure handling

### 📚 Rich Question Support
- **5-option MCQs** (A-E) with full support
- **Image embedding** - Automatically downloads and embeds images
- **Formatted explanations** - Clean line breaks and paragraph spacing
- **Answer highlighting** - Correct answer clearly marked

### 🎨 Professional Card Styling
- Clean, readable black text on white background
- Proper formatting for explanations with auto line breaks
- Responsive layout that works on desktop and mobile
- Custom "IndiaBix MCQ" note type

### 🛠️ User-Friendly Interface
- Simple PyQt GUI integrated into Anki's Tools menu
- Progress tracking for long scraping sessions
- Deck selection from existing Anki decks
- Configurable settings via `config.json`

### 🔒 Privacy & Security
- No data collection or tracking
- All processing happens locally
- No API keys or authentication required
- Open-source and audited for security

## 📦 Installation

### Method 1: Download .ankiaddon File (Recommended)
1. Download `indiabix_flashcard_generator.ankiaddon` from this release
2. Double-click the file to install in Anki
3. Restart Anki

### Method 2: Manual Installation
1. Clone this repository
2. Copy files to `Anki2/addons21/indiabix_flashcard_generator/`
3. Install dependencies: `pip install beautifulsoup4 requests lxml`
4. Restart Anki

## 🚀 Quick Start

1. Open Anki and click **Tools → Import from IndiaBix**
2. Paste a URL (e.g., `https://www.indiabix.com/general-knowledge/basic-general-knowledge/`)
3. Enter number of pages to scrape (1-50)
4. Click **Scrape Questions**
5. Select target deck
6. Click **Import to Anki**

## 🎯 Supported Content

### Tested Categories
✅ General Knowledge  
✅ Logical Reasoning  
✅ Aptitude (Quantitative)  
✅ Verbal Ability  
✅ Technical MCQs (Programming, CS, etc.)  

### Content Types
✅ Text-only questions  
✅ Questions with images  
✅ Questions with code snippets  
✅ Questions with mathematical notation  
✅ Explanations with formatting  

## 📊 Technical Details

- **Python Version:** 3.7+ (tested on 3.12)
- **Anki Version:** 2.1.49+
- **Dependencies:** BeautifulSoup4, requests, lxml, PyQt5 (bundled with Anki)
- **Lines of Code:** ~900 (core modules)
- **Documentation:** 2,500+ lines across 15 files

## 🧪 Testing

- ✅ 12/12 edge case tests passed
- ✅ Multi-page pagination tested
- ✅ Image handling verified
- ✅ 5-option questions validated
- ✅ Error scenarios tested (404, invalid URLs, etc.)

## 📝 Configuration Options

Edit `config.json` to customize:

```json
{
  "default_deck": "IndiaBix::General",
  "auto_tag": true,
  "include_explanation": true,
  "timeout": 30
}
```

## 🐛 Known Limitations

- Requires active internet connection
- IndiaBix.com must be accessible
- Rate limiting not implemented (be respectful of the source site)
- Some complex mathematical equations may not render perfectly

## 🔮 Future Enhancements (Planned)

- [ ] Rate limiting to prevent server overload
- [ ] Batch URL import from file
- [ ] Custom CSS themes for cards
- [ ] Export/import of scraped questions
- [ ] Support for additional question websites
- [ ] Progress persistence (resume interrupted scrapes)

## 🙏 Credits

### Developer
- **Author:** The-Harsh-Vardhan
- **GitHub:** [@The-Harsh-Vardhan](https://github.com/The-Harsh-Vardhan)

### Libraries Used
- **Anki:** Open-source spaced repetition software
- **BeautifulSoup4:** HTML parsing
- **Requests:** HTTP library
- **PyQt5:** GUI framework

### Special Thanks
- IndiaBix.com for providing excellent practice questions
- Anki community for add-on development resources
- All future contributors and users!

## 📄 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📞 Support

- **Issues:** [GitHub Issues](https://github.com/The-Harsh-Vardhan/AnkiBix-Extension/issues)
- **Documentation:** See README.md for comprehensive guide
- **Quick Start:** See QUICKSTART.md for 5-minute setup

## 🎓 Educational Use

This add-on is designed for **personal educational use only**. Please respect IndiaBix.com's terms of service and use responsibly.

---

**Download the add-on and start building your flashcard collection today!** 🚀📚

Happy Learning! ✨
