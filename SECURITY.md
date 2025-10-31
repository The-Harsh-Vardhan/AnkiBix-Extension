# Security Policy

## Supported Versions

We release patches for security vulnerabilities in the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.1.x   | :white_check_mark: |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

If you discover a security vulnerability in IndiaBix Flashcard Generator, please follow these steps:

### 1. **Do Not** Publicly Disclose
Please do not open a public GitHub issue about the vulnerability. This could put users at risk.

### 2. Report via GitHub Security
Use GitHub's [Security Advisory](https://github.com/The-Harsh-Vardhan/AnkiBix-Extension/security/advisories/new) feature to privately report the vulnerability.

### 3. Provide Details
Include as much information as possible:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if you have one)

### 4. Response Time
- We will acknowledge receipt within **48 hours**
- We will provide a detailed response within **7 days**
- We will work on a fix and release a patch as soon as possible

## Security Best Practices

When using this add-on:

1. **Keep Updated**: Always use the latest version
2. **Review Code**: This is open-source - review the code before installing
3. **Personal Use**: Use this add-on for personal educational purposes only
4. **Rate Limiting**: Respect IndiaBix's servers - don't scrape excessively
5. **Data Privacy**: This add-on doesn't collect or transmit your personal data

## Known Security Considerations

### Web Scraping
- This add-on scrapes content from IndiaBix.com
- We use standard HTTP requests (no authentication required)
- We don't store or transmit credentials

### Data Storage
- All data is stored locally in your Anki database
- No cloud services or external servers are used
- No telemetry or analytics are collected

### Dependencies
- We use minimal third-party dependencies
- All dependencies are listed in `requirements.txt`
- Dependencies: `beautifulsoup4`, `requests`, `lxml`

## Disclosure Policy

When a security vulnerability is fixed:
1. We will release a patch version
2. We will publish a security advisory on GitHub
3. We will update the CHANGELOG with security notes
4. We will notify users through the GitHub release notes

## Contact

For security-related questions that don't require immediate attention, you can:
- Open a regular GitHub issue (non-sensitive topics only)
- Contact the maintainer through GitHub

Thank you for helping keep IndiaBix Flashcard Generator secure! 🔒
