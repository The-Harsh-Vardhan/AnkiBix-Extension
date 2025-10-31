"""
Comprehensive Edge Case Testing for IndiaBix Scraper
Tests various scenarios to ensure robustness before publishing
"""

from scraper import IndiaBixScraper
import time

def print_separator(title):
    print("\n" + "="*80)
    print(f"  {title}")
    print("="*80)

def test_case(name, url, max_pages=1):
    """Test a specific URL and return results"""
    print(f"\n📝 Testing: {name}")
    print(f"   URL: {url}")
    
    try:
        scraper = IndiaBixScraper(timeout=30)
        result = scraper.scrape_url(url, max_pages=max_pages)
        
        print(f"   ✅ Success!")
        print(f"   Total questions: {result['total']}")
        print(f"   Category: {result['category']}")
        
        if result['questions']:
            q = result['questions'][0]
            print(f"   Sample question: {q['question'][:60]}...")
            print(f"   Options count: {len(q['options'])} - {list(q['options'].keys())}")
            print(f"   Answer: {q['answer']}")
            print(f"   Has images: {q.get('has_images', False)}")
            print(f"   Explanation: {'Yes' if q.get('explanation') else 'No'}")
        
        return True, result
        
    except Exception as e:
        print(f"   ❌ Error: {str(e)}")
        return False, str(e)


def main():
    print("\n🧪 INDIABIX SCRAPER - EDGE CASE TESTING")
    print("Testing various question types, formats, and edge cases\n")
    
    results = []
    
    # Test 1: Standard text-based questions (4 options)
    print_separator("TEST 1: Standard Text Questions (4 Options)")
    success, data = test_case(
        "General Knowledge - Text Only",
        "https://www.indiabix.com/general-knowledge/basic-general-knowledge/",
        max_pages=2
    )
    results.append(("Standard Text (4 options)", success))
    
    time.sleep(2)  # Be nice to the server
    
    # Test 2: Image-based questions (5 options)
    print_separator("TEST 2: Image-Based Questions (5 Options)")
    success, data = test_case(
        "Non-Verbal Reasoning - Images",
        "https://www.indiabix.com/non-verbal-reasoning/analogy/",
        max_pages=1
    )
    results.append(("Image-based (5 options)", success))
    
    time.sleep(2)
    
    # Test 3: Logical Reasoning
    print_separator("TEST 3: Logical Reasoning")
    success, data = test_case(
        "Logical Reasoning - Blood Relations",
        "https://www.indiabix.com/logical-reasoning/blood-relations/",
        max_pages=1
    )
    results.append(("Logical Reasoning", success))
    
    time.sleep(2)
    
    # Test 4: Aptitude with numbers/formulas
    print_separator("TEST 4: Aptitude Questions")
    success, data = test_case(
        "Aptitude - Numbers",
        "https://www.indiabix.com/aptitude/numbers/",
        max_pages=1
    )
    results.append(("Aptitude/Numbers", success))
    
    time.sleep(2)
    
    # Test 5: Technical questions
    print_separator("TEST 5: Technical Questions")
    success, data = test_case(
        "C Programming",
        "https://www.indiabix.com/c-programming/control-instructions/",
        max_pages=1
    )
    results.append(("C Programming", success))
    
    time.sleep(2)
    
    # Test 6: Data Interpretation (may have images/charts)
    print_separator("TEST 6: Data Interpretation")
    success, data = test_case(
        "Data Interpretation",
        "https://www.indiabix.com/data-interpretation/table-charts/",
        max_pages=1
    )
    results.append(("Data Interpretation", success))
    
    time.sleep(2)
    
    # Test 7: Verbal Ability
    print_separator("TEST 7: Verbal Ability")
    success, data = test_case(
        "Verbal Ability - Synonyms",
        "https://www.indiabix.com/verbal-ability/synonyms/",
        max_pages=1
    )
    results.append(("Verbal Ability", success))
    
    time.sleep(2)
    
    # Test 8: Engineering Mathematics
    print_separator("TEST 8: Engineering Questions")
    success, data = test_case(
        "Engineering Mathematics",
        "https://www.indiabix.com/technical-aptitude/area/",
        max_pages=1
    )
    results.append(("Engineering Math", success))
    
    time.sleep(2)
    
    # Test 9: Database questions
    print_separator("TEST 9: Database Questions")
    success, data = test_case(
        "Database - SQL",
        "https://www.indiabix.com/database/sql-server/",
        max_pages=1
    )
    results.append(("Database/SQL", success))
    
    time.sleep(2)
    
    # Test 10: Networking
    print_separator("TEST 10: Networking")
    success, data = test_case(
        "Networking Basics",
        "https://www.indiabix.com/networking/introduction/",
        max_pages=1
    )
    results.append(("Networking", success))
    
    # Test 11: Invalid URL handling
    print_separator("TEST 11: Invalid URL Handling")
    print("\n📝 Testing: Invalid URL")
    try:
        scraper = IndiaBixScraper()
        result = scraper.scrape_url("https://www.google.com", 1)
        print("   ❌ Should have raised error!")
        results.append(("Invalid URL handling", False))
    except ValueError as e:
        print(f"   ✅ Correctly rejected: {str(e)}")
        results.append(("Invalid URL handling", True))
    except Exception as e:
        print(f"   ⚠️  Unexpected error: {str(e)}")
        results.append(("Invalid URL handling", False))
    
    # Test 12: Empty/non-existent page
    print_separator("TEST 12: Non-Existent Page")
    success, data = test_case(
        "Non-existent page",
        "https://www.indiabix.com/nonexistent-category/fake-page/",
        max_pages=1
    )
    results.append(("Non-existent page", success if not success or (isinstance(data, dict) and data['total'] == 0) else False))
    
    # Print Summary
    print_separator("TEST SUMMARY")
    passed = sum(1 for _, success in results if success)
    total = len(results)
    
    print(f"\n📊 Results: {passed}/{total} tests passed\n")
    
    for test_name, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"   {status} - {test_name}")
    
    print("\n" + "="*80)
    
    if passed == total:
        print("🎉 ALL TESTS PASSED! Ready for production!")
    elif passed >= total * 0.8:
        print("⚠️  Most tests passed. Review failures before publishing.")
    else:
        print("❌ Multiple failures detected. Fix issues before publishing.")
    
    print("="*80 + "\n")
    
    # Additional checks
    print_separator("ADDITIONAL CHECKS")
    print("\n✓ Check these manually:")
    print("   1. [ ] All Python dependencies listed in requirements.txt")
    print("   2. [ ] manifest.json has correct metadata")
    print("   3. [ ] config.json has sensible defaults")
    print("   4. [ ] README.md is complete and accurate")
    print("   5. [ ] Code follows Anki add-on best practices")
    print("   6. [ ] No hardcoded paths or user-specific data")
    print("   7. [ ] Error messages are user-friendly")
    print("   8. [ ] GUI is responsive and intuitive")
    print("   9. [ ] Cards display correctly in Anki")
    print("   10. [ ] Images load properly in cards")
    print("   11. [ ] Works on Windows, Mac, and Linux")
    print("   12. [ ] Compatible with Anki 2.1.49+")
    print()


if __name__ == "__main__":
    main()
