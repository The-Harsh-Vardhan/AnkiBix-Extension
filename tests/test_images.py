from scraper import IndiaBixScraper

s = IndiaBixScraper()
result = s.scrape_url('https://www.indiabix.com/non-verbal-reasoning/analogy/', 1)

print(f'Total questions: {result["total"]}')

if result['questions']:
    q = result['questions'][0]
    print(f'\n{"="*80}')
    print(f'FIRST QUESTION ANALYSIS:')
    print(f'{"="*80}')
    print(f'Question text: {q["question"][:100]}...')
    print(f'Has images: {q.get("has_images", False)}')
    print(f'Number of options: {len(q["options"])}')
    print(f'Option labels: {list(q["options"].keys())}')
    print(f'Answer: {q["answer"]}')
    
    if q.get('has_images'):
        print(f'\n✅ IMAGE DETECTED!')
        print(f'Question HTML length: {len(q.get("question_html", ""))} characters')
        # Check for img tags
        import re
        img_tags = re.findall(r'<img[^>]+>', q.get("question_html", ""))
        print(f'Number of <img> tags: {len(img_tags)}')
        if img_tags:
            print(f'First image tag: {img_tags[0][:200]}...')
    
    print(f'\nOptions:')
    for key, val in q["options"].items():
        print(f'  {key}: {val[:50]}...' if len(val) > 50 else f'  {key}: {val}')
    
    print(f'\nExplanation: {q["explanation"][:100]}...' if q["explanation"] else '\nNo explanation')
    if q.get('explanation_html'):
        print(f'Explanation has HTML/images: Yes ({len(q["explanation_html"])} chars)')
