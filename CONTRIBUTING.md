# Contributing to IndiaBix Flashcard Generator

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## 🎯 Ways to Contribute

### 1. Report Bugs
- Use GitHub Issues to report bugs
- Include detailed steps to reproduce
- Mention your Anki version and OS
- Attach screenshots if relevant

### 2. Suggest Features
- Open an issue with the "enhancement" label
- Clearly describe the feature and use case
- Explain why it would be valuable

### 3. Submit Code
- Fork the repository
- Create a feature branch
- Write clean, documented code
- Submit a pull request

### 4. Improve Documentation
- Fix typos or unclear instructions
- Add examples or screenshots
- Translate documentation

## 🔧 Development Setup

### Prerequisites
- Python 3.8+
- Anki Desktop 2.1.49+
- Git
- Text editor or IDE

### Setup Steps

1. **Fork and clone the repository:**
   ```bash
   git clone https://github.com/your-username/indiabix-anki.git
   cd indiabix-anki
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Link to Anki:**
   - Create a symbolic link from the project folder to Anki's addons21 folder
   - This allows live testing

4. **Make changes and test:**
   - Edit code
   - Restart Anki to test changes
   - Check for errors in Anki's debug console

## 📝 Code Style Guidelines

### Python Style
- Follow PEP 8 conventions
- Use 4 spaces for indentation
- Maximum line length: 100 characters
- Use meaningful variable names

### Documentation
- Add docstrings to all functions and classes
- Use type hints for function parameters
- Include examples in docstrings when helpful

### Example:
```python
def parse_question(self, question_div) -> Optional[Dict]:
    """
    Parse a single question from the page
    
    Args:
        question_div: BeautifulSoup element containing question data
        
    Returns:
        Dictionary with question data or None if parsing fails
        
    Example:
        >>> scraper = IndiaBixScraper()
        >>> question_data = scraper.parse_question(soup.find('div', class_='question'))
    """
    pass
```

## 🧪 Testing

### Manual Testing
- Test with various IndiaBix URLs
- Try different configuration options
- Verify card formatting in Anki
- Test on different operating systems

### Test Cases to Cover
- Valid URLs
- Invalid URLs
- Empty sections
- Sections with many pages
- Network errors
- Malformed HTML

## 🚀 Pull Request Process

1. **Before submitting:**
   - Test your changes thoroughly
   - Update documentation if needed
   - Follow code style guidelines
   - Add comments for complex logic

2. **Submit PR:**
   - Use a clear, descriptive title
   - Describe what changed and why
   - Reference any related issues
   - Include screenshots for UI changes

3. **After submitting:**
   - Respond to review comments
   - Make requested changes
   - Keep the PR updated with main branch

## 🎨 Commit Message Guidelines

Use clear, descriptive commit messages:

### Format:
```
<type>: <subject>

<body>

<footer>
```

### Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting)
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

### Examples:
```
feat: Add support for pagination in scraper

- Implemented page navigation logic
- Added max_pages parameter to scrape_section()
- Updated UI to allow users to set page limit

Closes #15
```

```
fix: Handle missing explanation fields gracefully

Previously, the scraper would crash if a question had no explanation.
Now it sets explanation to empty string and continues.

Fixes #23
```

## 🐛 Bug Report Template

When reporting bugs, include:

```markdown
## Bug Description
[Clear description of the bug]

## Steps to Reproduce
1. Open Anki
2. Go to Tools → Import from IndiaBix
3. Enter URL: [URL]
4. Click Scrape Questions
5. [Error occurs]

## Expected Behavior
[What should happen]

## Actual Behavior
[What actually happens]

## Environment
- Anki Version: [e.g., 2.1.54]
- OS: [e.g., Windows 11, macOS 12, Ubuntu 22.04]
- Add-on Version: [e.g., 1.0.0]

## Screenshots
[If applicable]

## Error Logs
[Paste any error messages from Anki's debug console]
```

## 💡 Feature Request Template

```markdown
## Feature Description
[Clear description of the proposed feature]

## Use Case
[Why is this feature needed? Who will benefit?]

## Proposed Solution
[How would this feature work?]

## Alternatives Considered
[Any alternative approaches?]

## Additional Context
[Screenshots, mockups, examples, etc.]
```

## 🏗️ Architecture Guidelines

### Adding New Features

When adding features, consider:
- **Modularity**: Keep features separate and reusable
- **Configuration**: Make features configurable when possible
- **Error Handling**: Handle failures gracefully
- **User Feedback**: Provide clear status messages
- **Documentation**: Update docs and inline comments

### Code Organization

```
scraper.py         → Web scraping logic only
ui.py              → User interface components
deck_builder.py    → Anki API interactions
__init__.py        → Entry point and initialization
config.json        → User settings
```

## 📚 Resources

### Helpful Links
- [Anki Add-on Development Guide](https://addon-docs.ankiweb.net/)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [PyQt5 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt5/)
- [PEP 8 Style Guide](https://pep8.org/)

### Community
- [Anki Forums](https://forums.ankiweb.net/)
- [GitHub Discussions](https://github.com/your-repo/discussions)

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## ❓ Questions?

If you have questions about contributing:
- Open a GitHub Discussion
- Ask in the Issues section
- Contact the maintainer

Thank you for contributing! 🎉
