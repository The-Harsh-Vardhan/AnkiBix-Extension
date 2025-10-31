"""
Debug script to inspect IndiaBix HTML structure
"""
import requests
from bs4 import BeautifulSoup

url = "https://www.indiabix.com/general-knowledge/basic-general-knowledge/"

print(f"Fetching: {url}")
response = requests.get(url, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
})

print(f"Status Code: {response.status_code}")

soup = BeautifulSoup(response.content, 'html.parser')

# Save HTML for inspection
with open('debug_page.html', 'w', encoding='utf-8') as f:
    f.write(soup.prettify())
print("✅ Saved HTML to debug_page.html")

# Look for common question patterns
print("\n=== Searching for Question Patterns ===")

# Pattern 1: Look for divs with 'question' in class
question_divs = soup.find_all('div', class_=lambda x: x and 'question' in str(x).lower())
print(f"Divs with 'question' in class: {len(question_divs)}")

# Pattern 2: Look for tables
tables = soup.find_all('table')
print(f"Total tables: {len(tables)}")

# Pattern 3: Look for ordered lists (ol)
lists = soup.find_all('ol')
print(f"Ordered lists: {len(lists)}")

# Pattern 4: Look for specific IndiaBix classes
indiabix_divs = soup.find_all('div', class_=lambda x: x and 'bix' in str(x).lower())
print(f"Divs with 'bix' in class: {len(indiabix_divs)}")

# Pattern 5: Find all unique div classes
all_divs = soup.find_all('div', class_=True)
unique_classes = set()
for div in all_divs:
    classes = div.get('class', [])
    unique_classes.update(classes)

print(f"\n=== All Unique Div Classes ===")
sorted_classes = sorted([c for c in unique_classes if 'question' in c.lower() or 'bix' in c.lower() or 'quiz' in c.lower()])
for cls in sorted_classes[:20]:
    print(f"  - {cls}")

# Try to find actual question text
print(f"\n=== Looking for Question Markers ===")
# Questions often start with numbers
numbered_elements = soup.find_all(text=lambda t: t and t.strip().startswith(('1.', '2.', '3.', '4.', '5.')))
print(f"Elements starting with numbers: {len(numbered_elements)}")
if numbered_elements:
    for elem in numbered_elements[:3]:
        parent = elem.parent
        print(f"\nParent tag: {parent.name}")
        print(f"Parent class: {parent.get('class')}")
        print(f"Text: {elem.strip()[:100]}")

print("\n✅ Debug complete! Check debug_page.html for full HTML")
