"""
Test script to demonstrate question formatting
"""

import re

def format_question_text(text: str) -> str:
    """Format question text for better readability."""
    if not text:
        return ""
    
    has_code = any([
        '#include' in text,
        'int main()' in text,
        'printf(' in text,
        'return 0' in text,
        '{' in text and '}' in text,
    ])
    
    if has_code:
        text = re.sub(r'(#include[^>]*>)', r'\1\n', text)
        text = re.sub(r'(int main\(\))', r'\n\1', text)
        text = re.sub(r'({)', r'\1\n', text)
        text = re.sub(r'(})', r'\n\1', text)
        text = re.sub(r'(;)(?=\s*[a-zA-Z_])', r'\1\n', text)
        text = re.sub(r'(return \d+;)', r'\n\1', text)
        text = re.sub(r'\n{3,}', '\n\n', text)
    
    return text.strip()


# Test with your example
sample = "Point out the error, if any in the program.#include int main() { int i = 1; switch(i) { printf(\"This is c program.\"); case 1: printf(\"Case1\"); break; case 2: printf(\"Case2\"); break; } return 0; }"

print("=" * 80)
print("BEFORE FORMATTING:")
print("=" * 80)
print(sample)
print()

formatted = format_question_text(sample)

print("=" * 80)
print("AFTER FORMATTING:")
print("=" * 80)
print(formatted)
print()

print("=" * 80)
print("HOW IT WILL LOOK IN ANKI (with monospace font):")
print("=" * 80)
print("(Gray background, monospace font, proper line breaks)")
print()
for line in formatted.split('\n'):
    print(f"  {line}")
