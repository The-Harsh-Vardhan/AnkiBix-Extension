# Demo Script - IndiaBix Flashcard Generator

This script walks you through a complete demonstration of the add-on.

## 🎬 Demo Scenario: Importing General Knowledge Questions

### Prerequisites
- Anki Desktop installed and running
- Add-on installed and configured
- Internet connection active

---

## Part 1: Opening the Add-on (30 seconds)

**Narrator**: "Let me show you how easy it is to import questions from IndiaBix into Anki."

**Actions**:
1. Open Anki Desktop
2. Click **Tools** in the menu bar
3. Select **Import from IndiaBix**
4. *Dialog opens*

**Screenshot Point**: Main dialog window

---

## Part 2: Entering the URL (1 minute)

**Narrator**: "First, we paste the URL of the IndiaBix section we want to study."

**Actions**:
1. Copy this URL: `https://www.indiabix.com/general-knowledge/basic-general-knowledge/`
2. Paste into the URL input field
3. Note the helpful examples shown below

**Dialog Shows**:
```
Enter the IndiaBix section URL:
[https://www.indiabix.com/general-knowledge/basic-general-knowledge/]

Examples:
• https://www.indiabix.com/general-knowledge/basic-general-knowledge/
• https://www.indiabix.com/logical-reasoning/blood-relations/
• https://www.indiabix.com/aptitude/numbers/
```

**Screenshot Point**: URL entered

---

## Part 3: Configuring Options (1 minute)

**Narrator**: "Now let's configure our import options."

**Actions**:
1. Set **Maximum pages to scrape**: `5`
2. Select **Target Deck**: `IndiaBix::GK` (or create new)
3. Check ☑ **Automatically tag cards with category**
4. Check ☑ **Include explanation on card back**

**Dialog Shows**:
```
Step 2: Configure Options

Maximum pages to scrape: [5]

Target Deck: [IndiaBix::GK] [New Deck]

☑ Automatically tag cards with category
☑ Include explanation on card back
```

**Screenshot Point**: Options configured

---

## Part 4: Scraping Questions (2 minutes)

**Narrator**: "With one click, the add-on will scrape all questions from IndiaBix."

**Actions**:
1. Click **Scrape Questions** button
2. Watch the progress indicator
3. Read status messages

**Status Messages Show**:
```
Starting scraper for: https://www.indiabix.com/general-knowledge/basic-general-knowledge/
URL validated successfully
Scraping up to 5 pages...
Fetching page 1: [URL]
Found 10 questions on page 1
Fetching page 2: [URL]
Found 10 questions on page 2
...
✓ Successfully scraped 50 questions from 'General Knowledge::Basic General Knowledge'
Ready to import into Anki deck: IndiaBix::GK
```

**Screenshot Point**: Scraping complete

---

## Part 5: Importing to Anki (1 minute)

**Narrator**: "Finally, we import these questions as flashcards into our Anki deck."

**Actions**:
1. Click **Import to Anki** button
2. Watch progress bar fill up
3. Wait for completion message

**Status Messages Show**:
```
Importing 50 cards to 'IndiaBix::GK'...
[Progress: ████████████████████ 50/50]
✓ Successfully imported 50 out of 50 cards!
Cards are now available in your Anki collection.
```

**Dialog Appears**:
```
Successfully imported 50 flashcards to deck 'IndiaBix::GK'!

You can now study these cards or sync them to AnkiWeb.
```

**Screenshot Point**: Import complete

---

## Part 6: Viewing the Cards (2 minutes)

**Narrator**: "Let's see what these cards look like in Anki."

**Actions**:
1. Close the import dialog
2. Click on deck **IndiaBix::GK**
3. Click **Study Now**
4. View a sample card

**Front Side Shows**:
```
┌─────────────────────────────────────────┐
│ Question:                               │
│                                         │
│ The largest organ in the human body is:│
│                                         │
│ Options:                                │
│ A. Heart                                │
│ B. Brain                                │
│ C. Skin                                 │
│ D. Liver                                │
└─────────────────────────────────────────┘

[Show Answer]
```

**Click "Show Answer"**

**Back Side Shows**:
```
┌─────────────────────────────────────────┐
│ [Front side content]                    │
│ ─────────────────────────────────────── │
│                                         │
│ ✓ Correct Answer:                       │
│ C. Skin                                 │
│                                         │
│ 💡 Explanation:                         │
│ The skin is the largest organ of the   │
│ human body, covering approximately 2    │
│ square meters in adults. It serves as   │
│ a protective barrier and regulates      │
│ body temperature.                       │
└─────────────────────────────────────────┘

[Again] [Hard] [Good] [Easy]
```

**Screenshot Point**: Card example

---

## Part 7: Syncing to Mobile (1 minute)

**Narrator**: "Now sync these cards to study on your phone or tablet."

**Actions**:
1. Click the **Sync** button in Anki
2. Wait for sync to complete
3. Open AnkiMobile/AnkiDroid
4. Sync on mobile device
5. Cards are now available!

**Screenshot Point**: Mobile app with cards

---

## Alternative Demo: Logical Reasoning

### Quick Example (3 minutes)

**URL**: `https://www.indiabix.com/logical-reasoning/blood-relations/`

**Settings**:
- Pages: 3
- Deck: IndiaBix::Reasoning::BloodRelations
- Tags: Auto-tagged
- Explanation: Included

**Result**: 30 logical reasoning questions imported!

**Sample Question**:
```
Front:
"Pointing to a photograph, a man said, 'I have no brother or sister 
but that man's father is my father's son.' Whose photograph was it?"

A. His son
B. His father
C. His nephew
D. His brother

Back:
✓ Correct Answer: A. His son

Explanation:
'My father's son' refers to the man himself (since he has no siblings).
So, 'that man's father' is the speaker himself.
Therefore, the photograph is of his son.
```

---

## Alternative Demo: Aptitude

### Quick Example (3 minutes)

**URL**: `https://www.indiabix.com/aptitude/percentage/`

**Settings**:
- Pages: 10
- Deck: IndiaBix::Aptitude::Percentage
- Tags: Auto-tagged
- Explanation: Included

**Result**: 100 percentage questions imported!

**Sample Question**:
```
Front:
"What percentage of 60 is 12?"

A. 10%
B. 15%
C. 20%
D. 25%

Back:
✓ Correct Answer: C. 20%

Explanation:
Percentage = (12/60) × 100 = 20%
```

---

## Tips Demonstration (1 minute)

**Narrator**: "Here are some pro tips for using this add-on."

### Tip 1: Organize with Hierarchical Decks
```
IndiaBix
  ├─ General Knowledge
  │    ├─ Basic GK
  │    ├─ History
  │    └─ Geography
  ├─ Logical Reasoning
  │    ├─ Blood Relations
  │    └─ Puzzles
  └─ Aptitude
       ├─ Percentage
       └─ Time & Work
```

### Tip 2: Start Small
"Begin with 1-2 pages to test, then import more."

### Tip 3: Review Regularly
"Use Anki's spaced repetition for best retention."

### Tip 4: Sync Often
"Keep your cards synced across all devices."

---

## Error Handling Demo (1 minute)

**Narrator**: "The add-on gracefully handles errors."

### Example 1: Invalid URL
**Input**: `https://www.google.com`
**Result**: "Invalid IndiaBix URL. Please check the URL and try again."

### Example 2: Network Error
**Scenario**: Disconnect internet
**Result**: "Failed to fetch page: Connection error"

### Example 3: Empty Section
**Scenario**: Section with no questions
**Result**: "No questions found. The page structure may have changed."

---

## Summary (30 seconds)

**Narrator**: "In just a few clicks, you've imported 50 questions from IndiaBix into Anki!"

**Key Benefits**:
✅ No manual typing
✅ Professional card formatting
✅ Automatic organization
✅ Ready for spaced repetition
✅ Available on all devices

**Time Saved**: Instead of spending 2-3 hours manually creating 50 cards, you did it in 5 minutes!

---

## Complete Demo Timeline

| Time | Activity | Duration |
|------|----------|----------|
| 0:00 | Introduction | 30s |
| 0:30 | Open add-on | 30s |
| 1:00 | Enter URL | 1m |
| 2:00 | Configure options | 1m |
| 3:00 | Scrape questions | 2m |
| 5:00 | Import to Anki | 1m |
| 6:00 | View cards | 2m |
| 8:00 | Sync to mobile | 1m |
| 9:00 | Tips & tricks | 1m |
| 10:00 | Closing | 30s |
| **Total** | **Complete Demo** | **~10 minutes** |

---

## Demo Preparation Checklist

### Before Demo
- [ ] Anki installed and running
- [ ] Add-on installed correctly
- [ ] Internet connection stable
- [ ] Screen recording software ready
- [ ] Test URLs work
- [ ] Backup Anki collection
- [ ] Close unnecessary programs
- [ ] Prepare example deck names

### During Demo
- [ ] Speak clearly and slowly
- [ ] Show each step explicitly
- [ ] Wait for operations to complete
- [ ] Read status messages aloud
- [ ] Highlight key features
- [ ] Show final results

### After Demo
- [ ] Show sync feature
- [ ] Demonstrate mobile app
- [ ] Review card quality
- [ ] Answer questions
- [ ] Provide links to documentation

---

## Q&A Section

**Q: How long does it take to import 100 questions?**
A: Typically 3-5 minutes, depending on internet speed.

**Q: Can I import from multiple sections?**
A: Yes! Just repeat the process with different URLs.

**Q: What if IndiaBix changes their website?**
A: We'll update the scraper. Report issues on GitHub.

**Q: Can I edit the cards after import?**
A: Absolutely! They're regular Anki cards.

**Q: Does this work offline?**
A: Scraping requires internet, but studying is offline.

---

**End of Demo**

For more information, see:
- README.md for complete documentation
- QUICKSTART.md for quick setup
- GitHub for issues and support

**Thank you for using IndiaBix Flashcard Generator!** 🎉
