# 🚀 NEXT STEPS - Start Here!

Congratulations! You've built a complete Anki add-on. Here's your roadmap:

---

## ✅ STEP 1: Test the Scraper Independently ⏰ 5 minutes

Before installing in Anki, let's test that the web scraper works correctly.

### Run the Scraper Test:

```powershell
# Activate your virtual environment (if not already active)
.\.venv\Scripts\Activate.ps1

# Test the scraper
python scraper.py
```

**Expected Output:**
- Should show "Scraping X questions from Y category"
- Should display a sample question with options, answer, and explanation
- If it works, you're ready for Step 2! ✅

**If it fails:**
- Check your internet connection
- Verify IndiaBix.com is accessible
- Check the error message and fix any issues

---

## ✅ STEP 2: Locate Your Anki Add-ons Folder ⏰ 2 minutes

You need to find where Anki stores add-ons on your computer.

### For Windows (Your System):

1. **Press Win + R** to open Run dialog
2. **Type:** `%APPDATA%\Anki2\addons21\`
3. **Press Enter**

This will open your Anki add-ons folder in File Explorer.

**Note the path** - it's usually:
```
C:\Users\<YourUsername>\AppData\Roaming\Anki2\addons21\
```

---

## ✅ STEP 3: Copy Add-on to Anki Folder ⏰ 3 minutes

Now we'll install your add-on into Anki.

### Option A: Manual Copy (Recommended for Testing)

```powershell
# Copy the entire project folder to Anki's addons21 folder
$source = "PATH_TO_YOUR_PROJECT_FOLDER"
$destination = "$env:APPDATA\Anki2\addons21\indiabix_flashcard_generator"

# Create the destination folder
New-Item -ItemType Directory -Force -Path $destination

# Copy only the necessary files (excluding docs and dev files)
Copy-Item -Path "$source\__init__.py" -Destination $destination
Copy-Item -Path "$source\scraper.py" -Destination $destination
Copy-Item -Path "$source\ui.py" -Destination $destination
Copy-Item -Path "$source\deck_builder.py" -Destination $destination
Copy-Item -Path "$source\manifest.json" -Destination $destination
Copy-Item -Path "$source\config.json" -Destination $destination
Copy-Item -Path "$source\requirements.txt" -Destination $destination
Copy-Item -Path "$source\README.md" -Destination $destination

Write-Host "✅ Add-on files copied successfully!" -ForegroundColor Green
```

### Option B: Create Symbolic Link (For Development)

```powershell
# This creates a link so you can edit files and test immediately
$source = "C:\Users\harsh\OneDrive - Indian Institute of Information Technology, Nagpur\IIIT Nagpur\Summers 2025\Projects\AnkiBix Extension"
$link = "$env:APPDATA\Anki2\addons21\indiabix_flashcard_generator"

# Create symbolic link (requires admin privileges)
New-Item -ItemType SymbolicLink -Path $link -Target $source -Force

Write-Host "✅ Symbolic link created!" -ForegroundColor Green
```

---

## ✅ STEP 4: Install Dependencies in Anki's Python ⏰ 5 minutes

**IMPORTANT:** Anki uses its own Python environment, separate from your system Python!

### Find Anki's Python:

Anki's Python is usually located at:
```
C:\Program Files\Anki\python.exe
```

### Install Dependencies to Anki's Python:

```powershell
# Install to Anki's Python environment
& "C:\Program Files\Anki\python.exe" -m pip install beautifulsoup4 requests lxml

# If that doesn't work, try:
& "C:\Program Files\Anki\Lib\site-packages\pip" install beautifulsoup4 requests lxml
```

**Alternative Method - Manual Install:**

If pip doesn't work with Anki's Python, you can:

1. Download the packages manually from PyPI
2. Copy them to Anki's site-packages folder:
   ```
   C:\Program Files\Anki\Lib\site-packages\
   ```

---

## ✅ STEP 5: Start Anki and Test ⏰ 5 minutes

### 1. Close Anki (if running)

Make sure Anki is completely closed.

### 2. Start Anki

Open Anki Desktop normally.

### 3. Check for the Add-on

1. Go to **Tools** menu
2. Look for **"Import from IndiaBix"**
3. If you see it - SUCCESS! ✅

### 4. Test the Import Dialog

1. Click **Tools → Import from IndiaBix**
2. The dialog should open without errors
3. Try entering a test URL:
   ```
   https://www.indiabix.com/general-knowledge/basic-general-knowledge/
   ```
4. Set pages to **1** (for quick test)
5. Click **Scrape Questions**
6. Wait for results

---

## ✅ STEP 6: Import Your First Cards ⏰ 3 minutes

If scraping worked:

1. **Select a deck** (or create new one called "IndiaBix::Test")
2. **Check the options:**
   - ☑ Auto-tag cards
   - ☑ Include explanations
3. **Click "Import to Anki"**
4. Wait for import to complete
5. **Study the cards!**

### View Your Cards:

1. Click on the deck you imported to
2. Click **Study Now**
3. Review the card formatting
4. Check that explanations show on the back

---

## 🐛 TROUBLESHOOTING

### Problem: Add-on doesn't appear in Tools menu

**Solutions:**
1. Check folder name is exactly: `indiabix_flashcard_generator`
2. Verify all files are present (especially `__init__.py` and `manifest.json`)
3. Check Anki's error log:
   - Tools → Add-ons → View Files
   - Look for errors.log

### Problem: "Import Error: No module named 'bs4'"

**Solution:**
Dependencies not installed in Anki's Python. Go back to Step 4.

### Problem: Scraper finds no questions

**Solutions:**
1. Check internet connection
2. Try a different IndiaBix URL
3. IndiaBix may have changed their HTML structure
4. Check the console for error messages

### Problem: Cards look strange

**Solution:**
The note type wasn't created properly. 
1. Go to Tools → Manage Note Types
2. Delete "IndiaBix MCQ" if it exists
3. Restart Anki and import again

---

## 📊 VERIFICATION CHECKLIST

Before moving forward, verify:

- [ ] Scraper test runs successfully
- [ ] Files copied to Anki addons folder
- [ ] Dependencies installed in Anki's Python
- [ ] Add-on appears in Tools menu
- [ ] Dialog opens without errors
- [ ] Can scrape test URL
- [ ] Cards import successfully
- [ ] Cards display correctly
- [ ] Tags are applied

---

## 🎯 AFTER SUCCESSFUL TESTING

Once everything works:

### 1. Create a Git Repository (5 minutes)

```powershell
cd "C:\Users\harsh\OneDrive - Indian Institute of Information Technology, Nagpur\IIIT Nagpur\Summers 2025\Projects\AnkiBix Extension"

# Initialize git
git init

# Add all files
git add .

# First commit
git commit -m "Initial release v1.0.0 - IndiaBix Flashcard Generator"

# Create a branch
git branch -M main
```

### 2. Create GitHub Repository (5 minutes)

1. Go to https://github.com/new
2. Repository name: `indiabix-anki-addon`
3. Description: "Automatically import IndiaBix questions into Anki flashcards"
4. Keep it **Public**
5. Don't initialize with README (you already have one)
6. Click **Create repository**

### 3. Push to GitHub (2 minutes)

```powershell
# Add remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/indiabix-anki-addon.git

# Push to GitHub
git push -u origin main

# Create a release tag
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

### 4. Share with Others (Optional)

- Post on r/Anki subreddit
- Share on Anki forums
- Tweet about it
- Submit to AnkiWeb

---

## 🎓 LEARNING RESOURCES

### If You Want to Modify the Add-on:

1. **Anki Add-on Development:**
   - https://addon-docs.ankiweb.net/

2. **BeautifulSoup Tutorial:**
   - https://www.crummy.com/software/BeautifulSoup/bs4/doc/

3. **PyQt5 Documentation:**
   - https://doc.qt.io/qtforpython/

### Useful Anki APIs:

```python
# Collection access
mw.col  # Main collection

# Deck operations
mw.col.decks.id(deck_name)  # Get deck ID
mw.col.decks.all()  # Get all decks

# Note operations
note = Note(col, model)  # Create note
col.add_note(note, deck_id)  # Add note

# UI operations
showInfo("Message")  # Show info dialog
tooltip("Quick message")  # Show tooltip
```

---

## 🚀 QUICK START COMMANDS

### Test the add-on:
```powershell
# From project directory
python scraper.py
```

### Copy to Anki:
```powershell
# Copy files
$source = "C:\Users\harsh\OneDrive - Indian Institute of Information Technology, Nagpur\IIIT Nagpur\Summers 2025\Projects\AnkiBix Extension"
$destination = "$env:APPDATA\Anki2\addons21\indiabix_flashcard_generator"
New-Item -ItemType Directory -Force -Path $destination
Copy-Item -Path "$source\*.py" -Destination $destination
Copy-Item -Path "$source\*.json" -Destination $destination
```

### Install dependencies to Anki:
```powershell
& "C:\Program Files\Anki\python.exe" -m pip install beautifulsoup4 requests lxml
```

---

## 📞 GET HELP

If you're stuck:

1. **Check the README.md** - Comprehensive documentation
2. **Check TROUBLESHOOTING section** - Common issues
3. **Review error logs** - Anki shows errors in Tools → Add-ons
4. **Ask for help** - I'm here to assist!

---

## ✨ CONGRATULATIONS!

You've built a complete, professional Anki add-on! 🎉

**Next milestone:** Get your first 100 cards imported and start studying!

**Good luck with your preparation! 📚✨**

---

**Pro Tip:** Start with a small test (1-2 pages) before importing large amounts of questions. This helps verify everything works correctly.
