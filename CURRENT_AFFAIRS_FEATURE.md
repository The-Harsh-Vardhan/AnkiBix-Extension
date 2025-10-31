# 📅 Current Affairs Auto-Sync Feature

## Overview

The **Daily Current Affairs Auto-Sync** feature automatically imports daily current affairs questions from IndiaBix.com every time you open Anki. No manual action required!

---

## ✨ Features

### 1. **Automatic Daily Sync**
- ✅ Runs automatically when Anki starts (after 3-second delay)
- ✅ Tries today's date first
- ✅ Falls back to yesterday if today isn't available yet
- ✅ Avoids duplicate imports (tracks synced dates)
- ✅ Shows notification when new questions are imported

### 2. **Smart Tracking**
- Maintains a history of synced dates
- Never imports the same day twice
- Stored in `sync_history.json` in add-on folder

### 3. **Catch-Up Feature**
- Sync multiple days at once (e.g., if you missed a week)
- Date range selector for flexibility
- Progress tracking with detailed logs

### 4. **Fully Configurable**
- Enable/disable auto-sync via config or UI
- Customize target deck name
- All settings in `config.json`

---

## 🎯 How It Works

### URL Format
IndiaBix Current Affairs pages follow this pattern:
```
https://www.indiabix.com/current-affairs/YYYY-MM-DD/
```

Examples:
- Today: `https://www.indiabix.com/current-affairs/2025-10-31/`
- Yesterday: `https://www.indiabix.com/current-affairs/2025-10-30/`

### Sync Logic
1. **On Anki Startup** (3-second delay):
   - Check if today's date is already synced
   - If not, try to fetch today's current affairs
   - If today's page doesn't exist yet, try yesterday
   - Import questions to deck
   - Mark date as synced
   - Show notification

2. **Manual Sync**:
   - Click `Tools → Sync Daily Current Affairs`
   - Runs the same logic immediately

3. **Catch-Up Sync**:
   - Click `Tools → Manage Current Affairs`
   - Select date range
   - Click "Sync Date Range"
   - All missing dates are imported

---

## ⚙️ Configuration

### Settings in `config.json`

```json
{
  "auto_sync_current_affairs": true,      // Enable/disable auto-sync
  "current_affairs_deck": "IndiaBix::CurrentAffairs",  // Target deck name
  "include_explanation": true,             // Include explanations in cards
  "timeout": 30                            // Network timeout in seconds
}
```

### How to Change Settings

**Method 1: Edit config.json**
1. Go to `Tools → Add-ons`
2. Select "IndiaBix Flashcard Generator"
3. Click "Config" button
4. Edit settings
5. Click "OK" and restart Anki

**Method 2: Use the UI**
1. Go to `Tools → Manage Current Affairs`
2. Toggle "Enable auto-sync on Anki startup"
3. Settings are saved automatically

---

## 📚 Usage Examples

### Example 1: First Time Setup
```
1. Install add-on
2. Open Anki
3. Wait 3 seconds → Auto-sync runs
4. Check deck "IndiaBix::CurrentAffairs"
5. Today's 10 questions are imported! ✅
```

### Example 2: Daily Use
```
Day 1: Open Anki → Oct 30 questions imported
Day 2: Open Anki → Oct 31 questions imported
Day 3: Open Anki → Nov 1 questions imported
(No duplicates, fully automatic!)
```

### Example 3: Missed a Week
```
1. Click Tools → Manage Current Affairs
2. Set "From" date: 7 days ago
3. Set "To" date: Today
4. Click "Sync Date Range"
5. Watch progress bar
6. All 7 days imported in one go! ✅
```

### Example 4: Disable Auto-Sync
```
1. Tools → Manage Current Affairs
2. Uncheck "Enable auto-sync on Anki startup"
3. Done! (You can still sync manually)
```

---

## 🎨 Card Format

### Tags Applied
Each imported question gets these tags:
- `IndiaBix` - General tag
- `CurrentAffairs` - Category tag
- `current-affairs-2025-10-31` - Date-specific tag (for filtering)

### Example Card

**Front:**
```
What is the capital of France?

A. London
B. Paris
C. Berlin
D. Rome
```

**Back:**
```
Answer: B. Paris

Explanation:
Paris is the capital and largest city of France.
Located on the Seine River, it is known for landmarks
like the Eiffel Tower and Louvre Museum.
```

**Tags:** `IndiaBix`, `CurrentAffairs`, `current-affairs-2025-10-31`

---

## 🔧 Advanced Features

### 1. Sync History File
Location: `addon_folder/sync_history.json`

Format:
```json
{
  "2025-10-30": true,
  "2025-10-31": true,
  "2025-11-01": true
}
```

To reset history: Delete this file and restart Anki

### 2. Check Missing Dates
```python
# The system can detect up to 30 days of missing imports
Tools → Manage Current Affairs → See activity log
```

### 3. Custom Deck Organization
Create hierarchical decks:
```json
{
  "current_affairs_deck": "Studies::CurrentAffairs::2025"
}
```

---

## 🐛 Troubleshooting

### Problem: Auto-sync not working
**Solutions:**
1. Check if enabled in config: `"auto_sync_current_affairs": true`
2. Look for errors in Anki console: `Tools → Add-ons → View Files`
3. Try manual sync: `Tools → Sync Daily Current Affairs`
4. Check internet connection

### Problem: Same questions imported twice
**Solution:**
- Should not happen! Check `sync_history.json`
- If corrupted, delete the file

### Problem: Today's page not found
**Explanation:**
- IndiaBix publishes current affairs with a delay
- Auto-sync automatically tries yesterday if today fails
- This is normal behavior

### Problem: Want to re-import a date
**Solution:**
1. Open `sync_history.json`
2. Remove that date from the JSON
3. Run manual sync

### Problem: Too many old dates missing
**Solution:**
Use the Catch-Up feature:
1. `Tools → Manage Current Affairs`
2. Select date range (max 90 days)
3. Click "Sync Date Range"

---

## 📊 Performance

### Resource Usage
- **Network:** ~50KB per day (10 questions)
- **Disk:** ~5KB sync history file
- **Memory:** Minimal impact
- **Startup Delay:** 3 seconds (configurable)

### Limitations
- Max 90 days in single catch-up sync (can repeat)
- Requires active internet connection
- Respects IndiaBix.com availability

---

## 🎓 Best Practices

### 1. Daily Review Routine
```
Morning:
1. Open Anki (auto-sync runs)
2. Review due cards from previous days
3. Study new current affairs (today's 10 questions)

Benefits:
- Consistent daily learning
- Never miss a day
- Spaced repetition for retention
```

### 2. Deck Organization
```
Create sub-decks by month:
- IndiaBix::CurrentAffairs::2025::October
- IndiaBix::CurrentAffairs::2025::November
- IndiaBix::CurrentAffairs::2025::December

Configure in config.json:
"current_affairs_deck": "IndiaBix::CurrentAffairs::2025::November"
```

### 3. Tag-Based Filtering
```
Use tags to study specific periods:
- Study all October: Filter by "current-affairs-2025-10"
- Study specific day: Filter by "current-affairs-2025-10-31"
- Study all current affairs: Filter by "CurrentAffairs"
```

### 4. Vacation Mode
```
Going on vacation? Two options:

Option 1: Disable auto-sync
Tools → Manage Current Affairs → Uncheck auto-sync

Option 2: Let it run (sync on return)
When you return, use Catch-Up feature to import missed days
```

---

## 🔐 Privacy & Data

### What Gets Stored
- Sync history (dates only, no personal data)
- Configuration settings
- Imported questions (in your Anki database)

### What Doesn't Get Stored
- No tracking or analytics
- No personal information
- No external server communication (except IndiaBix.com for scraping)

### Data Location
```
Windows: %APPDATA%\Anki2\addons21\indiabix_flashcard_generator\
Mac: ~/Library/Application Support/Anki2/addons21/indiabix_flashcard_generator/
Linux: ~/.local/share/Anki2/addons21/indiabix_flashcard_generator/
```

---

## 📞 Support

### Getting Help
1. Check this documentation first
2. Look at activity log: `Tools → Manage Current Affairs`
3. Check GitHub issues: [AnkiBix-Extension/issues](https://github.com/The-Harsh-Vardhan/AnkiBix-Extension/issues)
4. Report bugs with details (date, error message, etc.)

### Feature Requests
- Want different sync timing? Let us know!
- Want more categories auto-synced? Suggest them!
- Found a bug? Report it on GitHub!

---

## 🚀 Future Enhancements (Planned)

- [ ] Auto-sync for other daily topics (e.g., "Quote of the Day")
- [ ] Custom sync schedule (e.g., sync at 9 AM daily)
- [ ] Email notifications for new questions
- [ ] Statistics dashboard (questions learned, streak tracking)
- [ ] Export sync history as CSV

---

## ✅ Summary

**What you get:**
- ✅ Automatic daily import of current affairs
- ✅ Zero manual effort after setup
- ✅ Never miss a day (catch-up feature)
- ✅ Smart duplicate prevention
- ✅ Fully configurable
- ✅ Privacy-friendly

**How to use:**
1. Install add-on
2. Open Anki
3. Watch it work! 🎉

**That's it! Your daily current affairs study routine is now automated.**

---

*Last updated: October 31, 2025*  
*Feature version: 1.1.0*  
*Add-on version: 1.0.0*
