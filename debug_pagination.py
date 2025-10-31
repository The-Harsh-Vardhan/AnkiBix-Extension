import requests
from bs4 import BeautifulSoup

url = "https://www.indiabix.com/general-knowledge/basic-general-knowledge/"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

# Find pagination elements
print("Looking for pagination...")
print("\n1. Links with 'next' text:")
next_links = soup.find_all('a', string=lambda x: x and 'next' in x.lower() if x else False)
for link in next_links[:5]:
    print(f"  {link.text.strip()} -> {link.get('href')}")

print("\n2. Links in pagination div:")
pagination = soup.find_all('div', class_=lambda x: x and 'pag' in x.lower() if x else False)
for pag in pagination[:3]:
    print(f"  Div class: {pag.get('class')}")
    links = pag.find_all('a')
    for link in links[:5]:
        print(f"    {link.text.strip()} -> {link.get('href')}")

print("\n3. All links with numeric patterns:")
all_links = soup.find_all('a', href=True)
numeric_links = [a for a in all_links if a.get('href') and any(c.isdigit() for c in a.get('href'))]
for link in numeric_links[:10]:
    href = link.get('href')
    if 'general-knowledge' in href and len(href) > 30:
        print(f"  {link.text.strip()[:20]:20} -> {href}")

print("\n4. Checking specific IndiaBix pagination format:")
import re
page_links = [a for a in all_links if a.get('href') and re.search(r'/\d{6}$', a.get('href'))]
print(f"Found {len(page_links)} links with 6-digit format")
for link in page_links[:5]:
    print(f"  {link.text.strip()} -> {link.get('href')}")
