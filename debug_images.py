import requests
from bs4 import BeautifulSoup

url = "https://www.indiabix.com/non-verbal-reasoning/analogy/"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

# Find first question container
question_divs = soup.find_all('div', class_='bix-div-container')
print(f"Found {len(question_divs)} question containers\n")

if question_divs:
    first_q = question_divs[0]
    
    print("=" * 80)
    print("FIRST QUESTION STRUCTURE:")
    print("=" * 80)
    
    # Check for images
    images = first_q.find_all('img')
    print(f"\n1. IMAGES FOUND: {len(images)}")
    for i, img in enumerate(images, 1):
        src = img.get('src', '')
        alt = img.get('alt', '')
        print(f"   Image {i}: {src}")
        print(f"   Alt text: {alt}")
    
    # Check question text area
    question_text_elem = first_q.find('div', class_='bix-td-qtxt')
    if question_text_elem:
        print(f"\n2. QUESTION TEXT AREA:")
        print(f"   Text: {question_text_elem.get_text(strip=True)[:100]}")
        q_images = question_text_elem.find_all('img')
        print(f"   Images in question: {len(q_images)}")
    
    # Check options
    option_rows = first_q.find_all('div', class_='bix-opt-row')
    print(f"\n3. OPTIONS FOUND: {len(option_rows)}")
    for i, option in enumerate(option_rows, 1):
        opt_text = option.get_text(strip=True)[:50]
        opt_images = option.find_all('img')
        print(f"   Option {i}: {opt_text}")
        if opt_images:
            print(f"      Images: {len(opt_images)}")
            for img in opt_images:
                print(f"        - {img.get('src', '')}")
    
    # Check answer
    answer_div = first_q.find('div', class_='bix-ans-option')
    if answer_div:
        print(f"\n4. ANSWER: {answer_div.get_text(strip=True)}")
    
    # Check explanation
    explanation_div = first_q.find('div', class_='bix-ans-description')
    if explanation_div:
        exp_text = explanation_div.get_text(strip=True)[:100]
        exp_images = explanation_div.find_all('img')
        print(f"\n5. EXPLANATION:")
        print(f"   Text: {exp_text}")
        print(f"   Images: {len(exp_images)}")
    
    print("\n" + "=" * 80)
    print("RAW HTML SAMPLE:")
    print("=" * 80)
    print(first_q.prettify()[:1500])
