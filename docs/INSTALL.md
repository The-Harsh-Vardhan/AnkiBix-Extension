# Installation Guide

## Step-by-Step Installation Instructions

### For Windows Users

1. **Locate your Anki add-ons folder:**
   - Press `Win + R` to open Run dialog
   - Type: `%APPDATA%\Anki2\addons21\`
   - Press Enter

2. **Create the add-on folder:**
   - Create a new folder named `indiabix_flashcard_generator`
   - Copy all files from this project into that folder

3. **Install Python dependencies:**
   - Open PowerShell as Administrator
   - Navigate to the add-on folder:
     ```powershell
     cd "$env:APPDATA\Anki2\addons21\indiabix_flashcard_generator"
     ```
   - Install dependencies:
     ```powershell
     python -m pip install beautifulsoup4 requests
     ```

4. **Restart Anki**

### For macOS Users

1. **Locate your Anki add-ons folder:**
   ```bash
   open ~/Library/Application\ Support/Anki2/addons21/
   ```

2. **Create the add-on folder:**
   ```bash
   mkdir -p ~/Library/Application\ Support/Anki2/addons21/indiabix_flashcard_generator
   ```

3. **Copy files:**
   - Copy all project files to the newly created folder

4. **Install Python dependencies:**
   ```bash
   cd ~/Library/Application\ Support/Anki2/addons21/indiabix_flashcard_generator
   python3 -m pip install beautifulsoup4 requests
   ```

5. **Restart Anki**

### For Linux Users

1. **Locate your Anki add-ons folder:**
   ```bash
   cd ~/.local/share/Anki2/addons21/
   ```

2. **Create the add-on folder:**
   ```bash
   mkdir -p ~/.local/share/Anki2/addons21/indiabix_flashcard_generator
   ```

3. **Copy files:**
   ```bash
   cp -r /path/to/project/* ~/.local/share/Anki2/addons21/indiabix_flashcard_generator/
   ```

4. **Install Python dependencies:**
   ```bash
   cd ~/.local/share/Anki2/addons21/indiabix_flashcard_generator
   python3 -m pip install beautifulsoup4 requests
   ```

5. **Restart Anki**

## Verification

After installation, verify the add-on is working:

1. Open Anki
2. Go to **Tools** menu
3. You should see **"Import from IndiaBix"** option
4. Click it to test the dialog opens successfully

## Troubleshooting Installation

### Dependencies Not Installing

If `pip install` fails, try:

**Windows:**
```powershell
# Use Anki's bundled Python
"C:\Program Files\Anki\python.exe" -m pip install beautifulsoup4 requests
```

**Mac/Linux:**
```bash
# Install to user directory
python3 -m pip install --user beautifulsoup4 requests
```

### Add-on Not Appearing in Tools Menu

1. Check the folder name is exactly: `indiabix_flashcard_generator`
2. Verify all files are present (especially `__init__.py`)
3. Check Anki's error log:
   - Tools → Add-ons → View Files → Look for error logs

### Permission Errors

Run your terminal/PowerShell as Administrator/sudo when installing dependencies.

## Alternative: Install via requirements.txt

Create a `requirements.txt` file with:
```
beautifulsoup4>=4.9.0
requests>=2.25.0
```

Then install:
```bash
pip install -r requirements.txt
```

## Need Help?

If you encounter issues, please:
1. Check the main README.md troubleshooting section
2. Open an issue on GitHub with error details
3. Include your Anki version and operating system
