from scraper import IndiaBixScraper

# Test with C programming questions that have complex explanations
scraper = IndiaBixScraper()
result = scraper.scrape_url('https://www.indiabix.com/c-programming/control-instructions/', 1)

if result['questions']:
    q = result['questions'][0]
    print("="*80)
    print("QUESTION:")
    print("="*80)
    print(q['question'][:200])
    
    print("\n" + "="*80)
    print("ORIGINAL vs FORMATTED EXPLANATION:")
    print("="*80)
    
    # Show the formatted version
    print("\n📝 FORMATTED VERSION:")
    print("-"*80)
    print(q['explanation'])
    print("-"*80)
    
    print(f"\nExplanation length: {len(q['explanation'])} characters")
    print(f"Line breaks: {q['explanation'].count(chr(10))} found")
