# AnkiWeb Submission - IndiaBix Flashcard Generator

## 📝 Submission Form Details

### **Title** (less than 80 characters)
```
IndiaBix Flashcard Generator - Auto-Sync Current Affairs & Practice Questions
```

### **Tags** (space-separated)
```
indiabix flashcards web-scraping current-affairs competitive-exams gk aptitude reasoning study-tool auto-sync
```

### **Support Page** (URL)
```
https://github.com/The-Harsh-Vardhan/AnkiBix-Extension/issues
```

### **Branches**

| Branch | Min Version | Max Version |
|--------|-------------|-------------|
| 1.1.0  | 2.1.49      | (leave empty) |

---

## 📄 Description (Copy This for AnkiWeb)

```markdown
## 🎯 Overview

Automatically scrape IndiaBix questions and convert them into beautifully formatted Anki flashcards for spaced repetition learning. Perfect for competitive exam preparation!

![Import Interface](https://raw.githubusercontent.com/The-Harsh-Vardhan/AnkiBix-Extension/master/Images/Import_Screen.png)
*Simple one-click import interface*

---

## ✨ Key Features

### 🔄 Daily Current Affairs Auto-Sync
- **Automatic Import**: Latest current affairs sync on Anki startup
- **Smart Organization**: Hierarchical decks (Year → Month → Week)
- **Catch-up Mode**: Bulk import missed days (up to 90 days)
- **Zero Manual Work**: Set it and forget it!

![Current Affairs Management](https://raw.githubusercontent.com/The-Harsh-Vardhan/AnkiBix-Extension/master/Images/Manage_Current_Affairs_Screen.png)
*Manage daily Current Affairs auto-sync with one click*

---

### 📚 One-Click Question Import
- **Any IndiaBix Section**: GK, Aptitude, Reasoning, Verbal, Technical
- **Complete Content**: Questions, options, answers, explanations
- **Image Support**: Diagrams and figures included
- **Code Formatting**: Properly formatted programming questions
- **Multi-page Scraping**: Import entire sections at once

### 🎨 Beautiful Card Design
- Professional styling with color-coded sections
- Clear MCQ format (A-E options)
- Detailed explanations with step-by-step solutions
- Automatic tagging by category and subcategory

![Sample Card](https://raw.githubusercontent.com/The-Harsh-Vardhan/AnkiBix-Extension/master/Images/Question_and_Answer.png)
*Professionally formatted flashcards with clear explanations*

---

### 📂 Smart Organization
- Choose existing decks or create new ones
- Hierarchical Current Affairs decks: `IndiaBix::CurrentAffairs::2025::October::Week5`
- Automatic tagging for easy filtering
- Progress tracking during import

---

## 🚀 How to Use

### For Current Affairs (Auto-Sync)
1. **Enable**: Tools → IndiaBix → Manage Current Affairs Auto-Sync
2. **Configure**: Toggle auto-sync on/off
3. **Relax**: Daily questions automatically added!

### For Practice Questions
1. **Copy URL**: Go to any IndiaBix section, copy the URL
2. **Import**: Tools → IndiaBix → Import from IndiaBix
3. **Paste**: Enter URL, select deck, click "Start Scraping"

---

## 📖 Supported Categories

- ✅ **General Knowledge** (all topics)
- ✅ **Current Affairs** (daily auto-sync)
- ✅ **Logical Reasoning** (puzzles, blood relations, coding-decoding)
- ✅ **Quantitative Aptitude** (numbers, percentages, profit & loss)
- ✅ **Verbal Ability** (synonyms, antonyms, sentence correction)
- ✅ **Technical Subjects** (C, Java, Python, DBMS, Networking)
- ✅ **All other IndiaBix sections**

---

## 🔧 Configuration

Access settings via: `config.json` in add-on folder

```json
{
  "default_deck": "IndiaBix",
  "auto_sync_current_affairs": true,
  "current_affairs_deck": "IndiaBix::CurrentAffairs"
}
```

---

## 📊 Example URLs to Try

**General Knowledge:**
- `https://www.indiabix.com/general-knowledge/basic-general-knowledge/`
- `https://www.indiabix.com/general-knowledge/indian-history/`

**Aptitude:**
- `https://www.indiabix.com/aptitude/numbers/`
- `https://www.indiabix.com/aptitude/percentage/`

**Reasoning:**
- `https://www.indiabix.com/logical-reasoning/blood-relations/`
- `https://www.indiabix.com/logical-reasoning/puzzles/`

---

## 🆘 Troubleshooting

**No questions imported?**
- Check your internet connection
- Verify the URL is correct and accessible
- IndiaBix may have changed their HTML structure (report on GitHub)

**Auto-sync not working?**
- Check: Tools → IndiaBix → Manage Current Affairs Auto-Sync
- Ensure "Enable Auto-Sync" is checked
- Restart Anki

**Images not loading?**
- Images are embedded in cards automatically
- Check if images exist on IndiaBix page

---

## 📋 Requirements

- **Anki**: 2.1.49 or higher
- **Internet**: Required for scraping
- **Dependencies**: beautifulsoup4, requests, lxml (auto-installed)

---

## 🔗 Links

- **Documentation**: [GitHub Repository](https://github.com/The-Harsh-Vardhan/AnkiBix-Extension)
- **Bug Reports**: [GitHub Issues](https://github.com/The-Harsh-Vardhan/AnkiBix-Extension/issues)
- **Source Code**: [View on GitHub](https://github.com/The-Harsh-Vardhan/AnkiBix-Extension)

---

## ⚠️ Disclaimer

This is an **unofficial** add-on and is not affiliated with IndiaBix. Please respect IndiaBix's terms of service and use this tool **responsibly for personal educational purposes only**. Avoid excessive scraping that could burden their servers.

---

## 📜 License

MIT License - Free and open source!

**Version**: 1.1.0  
**Author**: The-Harsh-Vardhan  
**Last Updated**: October 31, 2025

**Happy Learning! 📚✨**
```

---

## 📦 File to Upload

**File**: `IndiaBix_FlashcardGenerator_v1.1.0.ankiaddon` (16.7 KB)

---

## ✅ Pre-Submission Checklist

- [x] Title is under 80 characters
- [x] Tags are space-separated (no commas)
- [x] Support page URL starts with `http`
- [x] All images use GitHub raw URLs
- [x] Description is comprehensive and well-formatted
- [x] .ankiaddon file is ready
- [x] Branch version set correctly (2.1.49+)
- [x] Add-on tested in Anki
- [x] Images are hosted on GitHub

---

## 🎯 Image URLs Used

All images are hosted on GitHub and will load correctly on AnkiWeb:

1. **Import Screen**: 
   `https://raw.githubusercontent.com/The-Harsh-Vardhan/AnkiBix-Extension/master/Images/Import_Screen.png`

2. **Current Affairs Management**: 
   `https://raw.githubusercontent.com/The-Harsh-Vardhan/AnkiBix-Extension/master/Images/Manage_Current_Affairs_Screen.png`

3. **Sample Card**: 
   `https://raw.githubusercontent.com/The-Harsh-Vardhan/AnkiBix-Extension/master/Images/Question_and_Answer.png`

---

## 🚀 Ready to Submit!

**Copy the Description section above** (from "## 🎯 Overview" to "Happy Learning!") and paste it into the AnkiWeb submission form's Description field.
