# Quick Start Guide - IndiaBix Flashcard Generator

## 🚀 Get Started in 5 Minutes!

### Step 1: Install the Add-on

**Copy these files to your Anki add-ons folder:**

- Windows: `%APPDATA%\Anki2\addons21\indiabix_flashcard_generator\`
- Mac: `~/Library/Application Support/Anki2/addons21/indiabix_flashcard_generator/`
- Linux: `~/.local/share/Anki2/addons21/indiabix_flashcard_generator/`

### Step 2: Install Dependencies

Open terminal/PowerShell in the add-on folder and run:

```bash
pip install beautifulsoup4 requests
```

### Step 3: Restart Anki

Close and reopen Anki.

### Step 4: Use the Add-on

1. Click **Tools → Import from IndiaBix**
2. Paste a URL like: `https://www.indiabix.com/general-knowledge/basic-general-knowledge/`
3. Click **Scrape Questions**
4. Click **Import to Anki**
5. Done! 🎉

## 📝 Project Files Overview

### Core Files (Required)
- `__init__.py` - Entry point, adds menu to Anki
- `scraper.py` - Web scraping logic for IndiaBix
- `ui.py` - PyQt GUI dialog
- `deck_builder.py` - Creates flashcards in Anki
- `manifest.json` - Add-on metadata
- `config.json` - Default settings

### Documentation (Optional)
- `README.md` - Complete documentation
- `INSTALL.md` - Detailed installation guide
- `CONTRIBUTING.md` - Contribution guidelines
- `CHANGELOG.md` - Version history
- `LICENSE` - MIT License
- `requirements.txt` - Python dependencies

### Development (Optional)
- `.gitignore` - Git ignore patterns
- `Idea.txt` - Original project proposal

## 🎯 Usage Examples

### Example 1: Import General Knowledge
```
URL: https://www.indiabix.com/general-knowledge/basic-general-knowledge/
Pages: 5
Deck: IndiaBix::GK::Basic
Tags: Automatically added
```

### Example 2: Import Logical Reasoning
```
URL: https://www.indiabix.com/logical-reasoning/blood-relations/
Pages: 3
Deck: IndiaBix::Reasoning::BloodRelations
Tags: Automatically added
```

### Example 3: Import Aptitude Questions
```
URL: https://www.indiabix.com/aptitude/percentage/
Pages: 10
Deck: IndiaBix::Aptitude::Percentage
Tags: Automatically added
```

## ⚙️ Configuration

Edit `config.json` to customize:

```json
{
  "default_deck": "IndiaBix::General",
  "auto_tag": true,
  "include_explanation": true,
  "timeout": 30
}
```

## 🔧 Troubleshooting

### Problem: Add-on doesn't appear in Tools menu
**Solution:** Check folder name is exactly `indiabix_flashcard_generator`

### Problem: Import errors about missing modules
**Solution:** Install dependencies: `pip install beautifulsoup4 requests`

### Problem: No questions found
**Solution:** Try a different URL or check your internet connection

### Problem: Cards look wrong
**Solution:** Delete the "IndiaBix MCQ" note type and restart Anki

## 📚 More Help

- See `README.md` for complete documentation
- See `INSTALL.md` for detailed installation
- See `CONTRIBUTING.md` to contribute
- Open GitHub issue for bugs

## 🎓 Tips for Best Results

1. **Start small** - Test with 1-2 pages first
2. **Organize decks** - Use hierarchical names like `IndiaBix::Category::Topic`
3. **Review regularly** - Use Anki's spaced repetition system
4. **Sync often** - Keep cards synced across devices
5. **Contribute** - Report bugs and suggest features!

## 📞 Support

Need help? 
- Check the README.md file
- Open a GitHub issue
- Contact the maintainer

---

**Happy Learning! 📚✨**
