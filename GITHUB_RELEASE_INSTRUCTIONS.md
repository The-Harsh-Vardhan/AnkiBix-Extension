# GitHub Release Creation Instructions

## 📦 Package Already Created

✅ `indiabix_flashcard_generator.ankiaddon` is ready for upload (10.8 KB)

## 🚀 Steps to Create GitHub Release

### 1. Go to GitHub Repository
Visit: https://github.com/The-Harsh-Vardhan/AnkiBix-Extension

### 2. Navigate to Releases
- Click on "Releases" in the right sidebar
- OR go directly to: https://github.com/The-Harsh-Vardhan/AnkiBix-Extension/releases

### 3. Create New Release
- Click **"Draft a new release"** button

### 4. Fill in Release Details

**Tag version:** `v1.0.0`
- Click "Choose a tag" dropdown
- Type: `v1.0.0`
- Click "Create new tag: v1.0.0 on publish"

**Release title:** `v1.0.0 - IndiaBix Flashcard Generator (Initial Release)`

**Description:** Copy the content from `RELEASE_NOTES_v1.0.0.md`

**Attach files:**
- Click "Attach binaries by dropping them here or selecting them"
- Upload: `indiabix_flashcard_generator.ankiaddon`

### 5. Publish Release
- Check "Set as the latest release"
- Click **"Publish release"**

## 📋 Release Checklist

Before publishing:
- ✅ Code is committed and pushed
- ✅ Security audit completed
- ✅ .ankiaddon package created (10.8 KB)
- ✅ Release notes prepared
- ✅ Version tag matches manifest.json (1.0.0)
- ✅ No personal information in code
- ✅ All tests passing

## 🌐 After Release

### Update README.md
Add installation badge:
```markdown
[![Download](https://img.shields.io/github/v/release/The-Harsh-Vardhan/AnkiBix-Extension)](https://github.com/The-Harsh-Vardhan/AnkiBix-Extension/releases/latest)
```

### Share Your Work
- Tweet about the release
- Post on Anki forums
- Share on Reddit r/Anki
- Add to AnkiWeb (optional)

## 📤 AnkiWeb Submission (Optional)

If you want to submit to AnkiWeb:

1. **Create AnkiWeb Account**
   - Go to: https://ankiweb.net/account/register

2. **Submit Add-on**
   - Visit: https://ankiweb.net/shared/upload
   - Upload: `indiabix_flashcard_generator.ankiaddon`
   - Fill in details from manifest.json

3. **Add-on Details**
   - Name: IndiaBix Flashcard Generator
   - Description: Copy from README.md (first paragraph)
   - Category: "Productivity" or "Study Tools"
   - Tags: anki, flashcards, mcq, india, indiabix, web-scraper

4. **Review Process**
   - AnkiWeb will review your submission
   - May take 1-7 days
   - You'll receive email notification

## 🎓 Tips

- Use semantic versioning (MAJOR.MINOR.PATCH)
- Write clear, detailed release notes
- Include screenshots in future releases
- Tag important releases with "Latest release"
- Consider pre-releases for beta testing

## 📞 Need Help?

- GitHub Release Docs: https://docs.github.com/en/repositories/releasing-projects-on-github
- AnkiWeb Guidelines: https://addon-docs.ankiweb.net/

---

**You're ready to publish! 🎉**
