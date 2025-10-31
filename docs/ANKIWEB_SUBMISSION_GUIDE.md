# AnkiWeb Add-on Submission Guide

## 📚 Official Documentation
- **Sharing Guide:** https://addon-docs.ankiweb.net/sharing.html
- **Main Docs:** https://addon-docs.ankiweb.net/

---

## 🎯 Step-by-Step Submission Process

### ✅ Prerequisites Checklist

Before submitting, ensure you have:

- [x] **Working add-on** - All code tested and functional
- [x] **manifest.json** - Contains all required fields
- [x] **README or documentation** - Clear usage instructions
- [x] **No personal info** - Security audit completed
- [x] **Dependencies listed** - requirements.txt or in README
- [x] **License file** - MIT License included
- [x] **GitHub repository** - Code publicly available

**Status: All prerequisites met! ✅**

---

## 📦 Step 1: Prepare Your .ankiaddon Package

### What You Have:
✅ `indiabix_flashcard_generator.ankiaddon` (10.8 KB) - Already created!

### What's Inside:
```
indiabix_flashcard_generator.ankiaddon (ZIP format)
├── __init__.py           # Entry point
├── scraper.py            # Web scraping logic
├── ui.py                 # PyQt GUI
├── deck_builder.py       # Anki card creation
├── manifest.json         # Metadata (REQUIRED)
└── config.json           # Default settings
```

### File Requirements (from Anki docs):
- ✅ **manifest.json is required** - You have this
- ✅ **Folder structure correct** - All files in root of ZIP
- ✅ **No unnecessary files** - Only essential code included
- ✅ **Proper naming** - Using snake_case package name

**Your package is ready!** ✅

---

## 🌐 Step 2: Create AnkiWeb Account (If You Don't Have One)

### 2.1 Register on AnkiWeb
1. Go to: **https://ankiweb.net/account/register**
2. Fill in:
   - **Email address** - Use your email
   - **Username** - Choose a username (visible to public)
   - **Password** - Create a strong password
3. Verify your email address

### 2.2 Sign In
- Go to: **https://ankiweb.net/account/login**
- Use your credentials

**Note:** You'll use this same account to upload add-ons and sync Anki decks.

---

## 📤 Step 3: Upload Your Add-on to AnkiWeb

### 3.1 Navigate to Upload Page
**Direct link:** https://ankiweb.net/shared/upload

Or manually:
1. Go to https://ankiweb.net
2. Click "Add-ons" in the top menu
3. Click "Share" button
4. Click "Upload a new add-on"

### 3.2 Fill in the Upload Form

#### **1. Add-on File**
- **Action:** Click "Choose File" or drag and drop
- **Upload:** `indiabix_flashcard_generator.ankiaddon`
- **Size:** 10.8 KB ✅

#### **2. Add-on Name** (Required)
```
IndiaBix Flashcard Generator
```

#### **3. Short Description** (Required - appears in search results)
```
Automatically scrape IndiaBix questions and convert them into Anki flashcards. Supports General Knowledge, Aptitude, Reasoning, and more.
```
**Character limit:** ~140 characters (keep it concise)

#### **4. Long Description** (Appears on add-on page)

**Recommended format:**

```markdown
# IndiaBix Flashcard Generator

Automatically scrape multiple-choice questions from IndiaBix.com and convert them into well-formatted Anki flashcards for spaced repetition learning!

## Features

✨ **Smart Web Scraping**
- Multi-page section scraping (handle 5-50 pages at once)
- Automatic question, option, answer, and explanation extraction
- Image support with automatic embedding
- Error handling for robust scraping

📚 **Rich Question Support**
- 5-option MCQs (A-E)
- Text questions with formatted explanations
- Code snippets and mathematical notation
- Images automatically downloaded and embedded

🎨 **Professional Card Styling**
- Clean, readable black text on white background
- Automatic line breaks in explanations
- Answer highlighting
- Mobile-friendly responsive design

🛠️ **User-Friendly Interface**
- Simple GUI integrated into Anki's Tools menu
- Progress tracking for long scraping sessions
- Deck selection from existing Anki decks
- Configurable settings

## Installation

1. Download the .ankiaddon file
2. Double-click to install in Anki
3. Install dependencies: `pip install beautifulsoup4 requests lxml`
4. Restart Anki
5. Find "Import from IndiaBix" in Tools menu

## Quick Start

1. Click **Tools → Import from IndiaBix**
2. Paste an IndiaBix URL (e.g., https://www.indiabix.com/general-knowledge/basic-general-knowledge/)
3. Enter number of pages to scrape
4. Click **Scrape Questions**
5. Select target deck
6. Click **Import to Anki**

## Supported Content

✅ General Knowledge
✅ Logical Reasoning
✅ Aptitude (Quantitative)
✅ Verbal Ability
✅ Technical MCQs (Programming, Computer Science, etc.)

## Configuration

Edit config.json in the add-on folder:
```json
{
  "default_deck": "IndiaBix::General",
  "auto_tag": true,
  "include_explanation": true,
  "timeout": 30
}
```

## Requirements

- Anki 2.1.49 or later
- Python 3.7+
- Dependencies: beautifulsoup4, requests, lxml

## Support

- **GitHub:** https://github.com/The-Harsh-Vardhan/AnkiBix-Extension
- **Issues:** Report bugs on GitHub
- **Documentation:** See README.md in repository

## License

MIT License - Free and open source

## Educational Use

This add-on is designed for personal educational use. Please respect IndiaBix.com's terms of service.

---

**Happy Learning! 📚✨**
```

**Tips for description:**
- Use clear formatting (Markdown supported)
- Include screenshots if possible (upload to GitHub, link in description)
- Mention all key features
- Include installation steps
- Add troubleshooting tips
- Link to GitHub for detailed docs

#### **5. Tags** (Optional but recommended)
```
indiabix, flashcards, mcq, questions, web-scraper, competitive-exams, aptitude, reasoning
```
**Tip:** Use tags that users might search for

#### **6. Category** (Choose one)
**Recommended:** `Productivity` or `Import/Export`

Available categories:
- Learning tools
- Productivity
- Import/Export
- Card styling
- Study tools

#### **7. Anki Version Compatibility**
- **Minimum version:** `2.1.49` (from your manifest.json)
- **Maximum version:** Leave blank (works with latest)

#### **8. Homepage/Support URL** (Optional but recommended)
```
https://github.com/The-Harsh-Vardhan/AnkiBix-Extension
```

#### **9. License** (Optional but recommended)
```
MIT License
```

### 3.3 Review and Submit
1. **Preview** your add-on page
2. Check all information is correct
3. Click **"Upload"** or **"Submit"**

---

## ⏳ Step 4: Wait for Review

### What Happens Next?

1. **Automatic Processing** (~5 minutes)
   - AnkiWeb extracts and validates your .ankiaddon file
   - Checks manifest.json format
   - Scans for obvious issues

2. **Manual Review** (1-7 days)
   - AnkiWeb staff review your add-on
   - Check for security issues
   - Verify it follows guidelines
   - Test basic functionality

3. **Approval or Feedback**
   - **If approved:** Add-on goes live immediately
   - **If issues found:** You'll receive feedback via email
   - **If rejected:** Fix issues and resubmit

### During Review:
- ✅ Monitor your email for notifications
- ✅ Check AnkiWeb dashboard for status
- ✅ Be patient - reviews can take up to a week

---

## ✅ Step 5: After Approval

### 5.1 Your Add-on Goes Live!

Once approved, users can find your add-on at:
```
https://ankiweb.net/shared/info/[YOUR-ADDON-ID]
```

You'll receive an **add-on ID** (e.g., `123456789`)

### 5.2 Update manifest.json with AnkiWeb ID

After getting your add-on ID, update `manifest.json`:

```json
{
  "package": "indiabix_flashcard_generator",
  "name": "IndiaBix Flashcard Generator",
  "version": "1.0.0",
  "author": "The-Harsh-Vardhan",
  "homepage": "https://github.com/The-Harsh-Vardhan/AnkiBix-Extension",
  "conflicts": [],
  "min_point_version": 49,
  "max_point_version": 0,
  "description": "Automatically scrape IndiaBix questions and convert them into Anki flashcards.",
  "ankiweb_id": "123456789"  ← Add this line
}
```

Commit and push this change to GitHub.

### 5.3 Promote Your Add-on

**Update README.md with AnkiWeb badge:**
```markdown
[![AnkiWeb](https://img.shields.io/badge/AnkiWeb-123456789-blue)](https://ankiweb.net/shared/info/123456789)
```

**Share on social media:**
- Reddit: r/Anki community
- Twitter/X: Tag @AnkiMobile
- Anki forums: https://forums.ankiweb.net/

**Create GitHub release:**
- Add AnkiWeb link to release notes
- Include installation instructions

---

## 🔄 Step 6: Updating Your Add-on (Future)

### When You Release v1.1.0, v1.2.0, etc.:

1. **Update version in manifest.json**
   ```json
   "version": "1.1.0"
   ```

2. **Create new .ankiaddon package**
   ```powershell
   Compress-Archive -Path "__init__.py","scraper.py","ui.py","deck_builder.py","manifest.json","config.json" -DestinationPath "indiabix_flashcard_generator.zip" -Force
   Rename-Item "indiabix_flashcard_generator.zip" "indiabix_flashcard_generator.ankiaddon" -Force
   ```

3. **Upload to AnkiWeb**
   - Go to https://ankiweb.net/shared/upload
   - Select "Update existing add-on"
   - Choose your add-on from dropdown
   - Upload new .ankiaddon file
   - Add changelog notes

4. **Update GitHub**
   - Create new GitHub release with new version tag
   - Update README.md if needed
   - Commit all changes

### Version Numbering:
- **1.0.0** → **1.0.1** - Bug fixes
- **1.0.0** → **1.1.0** - New features (backward compatible)
- **1.0.0** → **2.0.0** - Breaking changes

---

## 📊 Monitoring Your Add-on

### AnkiWeb Dashboard

Visit: https://ankiweb.net/shared/mine

**You can see:**
- Download count
- User ratings
- Reviews and comments
- Installation statistics

### Responding to Users

1. **Monitor comments** regularly
2. **Respond to questions** promptly
3. **Fix reported bugs** quickly
4. **Thank users** for feedback
5. **Update documentation** based on common questions

---

## 🚫 Common Rejection Reasons (Avoid These!)

### ❌ Don't Include:
- Personal information (API keys, passwords, emails)
- Copyrighted content without permission
- Malicious code or security vulnerabilities
- Excessive network requests (rate limit properly)
- Code that modifies Anki's core functionality unsafely

### ✅ Do Include:
- Clear documentation
- Error handling
- Proper license
- Dependencies list
- Contact information (GitHub)

**Your add-on already follows all best practices!** ✅

---

## 📋 Pre-Submission Checklist

Use this checklist before submitting:

### Code Quality
- [x] All features tested and working
- [x] No errors or crashes
- [x] Error handling implemented
- [x] No console spam (excessive logging)

### Documentation
- [x] Clear installation instructions
- [x] Usage examples provided
- [x] Configuration options explained
- [x] Troubleshooting guide included

### Package
- [x] manifest.json complete and valid
- [x] Only necessary files included
- [x] Proper file structure
- [x] Dependencies listed

### Security & Privacy
- [x] No personal information
- [x] No hardcoded credentials
- [x] No data collection without consent
- [x] Respects user privacy

### Legal
- [x] License file included (MIT)
- [x] No copyright violations
- [x] Proper attribution for libraries
- [x] Terms of service respected

**All checks passed! You're ready to submit!** ✅

---

## 🎯 Your Next Actions

### Immediate (Today):

1. **Go to AnkiWeb:** https://ankiweb.net/shared/upload
2. **Upload your .ankiaddon file:** `indiabix_flashcard_generator.ankiaddon`
3. **Fill in the form** (use descriptions from this guide)
4. **Submit and wait for review**

### After Approval (1-7 days):

1. **Update manifest.json** with AnkiWeb ID
2. **Add AnkiWeb badge to README.md**
3. **Create GitHub release** with AnkiWeb link
4. **Share on social media** (Reddit, Twitter, forums)
5. **Monitor feedback** and respond to users

### Ongoing:

1. **Monitor AnkiWeb dashboard** for downloads/reviews
2. **Respond to user comments** and questions
3. **Fix bugs** reported by users
4. **Plan v1.1.0** with new features
5. **Keep documentation updated**

---

## 📞 Support Resources

### Official Anki Resources:
- **Sharing Guide:** https://addon-docs.ankiweb.net/sharing.html
- **Add-on Development:** https://addon-docs.ankiweb.net/
- **Anki Forums:** https://forums.ankiweb.net/
- **AnkiWeb Contact:** support@ankiweb.net

### Your Resources:
- **GitHub Repo:** https://github.com/The-Harsh-Vardhan/AnkiBix-Extension
- **Issue Tracker:** https://github.com/The-Harsh-Vardhan/AnkiBix-Extension/issues
- **Documentation:** README.md, QUICKSTART.md, etc.

---

## 🎉 You're Ready!

Everything is prepared for submission:
- ✅ Add-on tested and working
- ✅ Package created (10.8 KB)
- ✅ Documentation complete
- ✅ Security audit passed
- ✅ GitHub repository public
- ✅ All prerequisites met

**Now go submit your add-on and help students worldwide!** 🚀📚

---

*Good luck with your submission! Your add-on will help countless students prepare for competitive exams.* ✨
