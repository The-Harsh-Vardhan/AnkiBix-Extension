"""
IndiaBix Web Scraper Module
Handles fetching and parsing questions from IndiaBix website
"""

import re
import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Optional
from urllib.parse import urlparse, urljoin


class IndiaBixScraper:
    """Scraper for IndiaBix questions"""
    
    def __init__(self, timeout: int = 30, user_agent: Optional[str] = None):
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': user_agent or 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def validate_url(self, url: str) -> bool:
        """Validate if the URL is from IndiaBix"""
        parsed = urlparse(url)
        return 'indiabix.com' in parsed.netloc.lower()
    
    def extract_category_from_url(self, url: str) -> str:
        """Extract category name from URL for tagging"""
        parsed = urlparse(url)
        path_parts = [p for p in parsed.path.split('/') if p]
        
        if len(path_parts) >= 2:
            category = path_parts[0].replace('-', ' ').title()
            subcategory = path_parts[1].replace('-', ' ').title()
            return f"{category}::{subcategory}"
        elif len(path_parts) >= 1:
            return path_parts[0].replace('-', ' ').title()
        
        return "IndiaBix"
    
    def fetch_page(self, url: str) -> Optional[BeautifulSoup]:
        """Fetch and parse a webpage"""
        try:
            response = self.session.get(url, timeout=self.timeout)
            response.raise_for_status()
            return BeautifulSoup(response.content, 'html.parser')
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch page: {str(e)}")
    
    def parse_question(self, question_div) -> Optional[Dict]:
        """Parse a single question from the page"""
        try:
            question_data = {}
            
            # Extract question text - look for bix-td-qtxt class
            question_text_elem = question_div.find('div', class_='bix-td-qtxt')
            
            if question_text_elem:
                # Remove script and style elements
                for script in question_text_elem(['script', 'style']):
                    script.decompose()
                question_data['question'] = question_text_elem.get_text(strip=True)
            else:
                return None
            
            # Extract options - look for bix-opt-row divs
            options = {}
            option_rows = question_div.find_all('div', class_='bix-opt-row')
            
            for i, option_row in enumerate(option_rows):
                # Get the option text
                option_text = option_row.get_text(strip=True)
                # Use A, B, C, D based on position
                label = chr(65 + i)  # 65 is ASCII for 'A'
                if option_text:
                    options[label] = option_text
            
            question_data['options'] = options
            
            # Extract answer
            answer_div = question_div.find('div', class_='bix-ans-option')
            if not answer_div:
                answer_div = question_div.find('span', class_='jq-hdnakqb')
            
            if answer_div:
                answer_text = answer_div.get_text(strip=True)
                # Extract just the option letter (A, B, C, D)
                answer_match = re.search(r'([A-D])', answer_text)
                if answer_match:
                    question_data['answer'] = answer_match.group(1)
                else:
                    question_data['answer'] = answer_text
            
            # Extract explanation
            explanation_div = question_div.find('div', class_='bix-ans-description')
            if not explanation_div:
                explanation_div = question_div.find('div', class_='bix-div-answer-description')
            
            if explanation_div:
                # Remove script and style elements
                for script in explanation_div(['script', 'style']):
                    script.decompose()
                question_data['explanation'] = explanation_div.get_text(strip=True)
            else:
                question_data['explanation'] = ""
            
            return question_data if question_data.get('question') else None
            
        except Exception as e:
            print(f"Error parsing question: {str(e)}")
            return None
    
    def scrape_section(self, url: str, max_pages: int = 10) -> List[Dict]:
        """Scrape all questions from a section (handles pagination)"""
        questions = []
        current_page = 1
        
        # Get all page URLs first
        page_urls = [url]  # Start with the first page
        
        try:
            # Fetch first page to find all pagination links
            print(f"Fetching page {current_page}: {url}")
            soup = self.fetch_page(url)
            
            if soup:
                # Find all pagination links with 6-digit format (IndiaBix style)
                all_links = soup.find_all('a', href=True)
                base_path = urlparse(url).path.rstrip('/')
                
                for link in all_links:
                    href = link.get('href')
                    # Match IndiaBix pagination: /category/subcategory/006001
                    if href and base_path in href and re.search(r'/\d{6}$', href):
                        full_url = urljoin(url, href)
                        if full_url not in page_urls:
                            page_urls.append(full_url)
                
                # Limit to max_pages
                page_urls = page_urls[:max_pages]
                print(f"Found {len(page_urls)} pages to scrape")
        
        except Exception as e:
            print(f"Error finding pagination: {str(e)}")
        
        # Now scrape all pages
        for page_num, page_url in enumerate(page_urls, 1):
            try:
                if page_num > 1:
                    print(f"Fetching page {page_num}: {page_url}")
                    soup = self.fetch_page(page_url)
                # else: already fetched the first page
                
                if not soup:
                    continue
                
                # Find all question containers
                question_divs = soup.find_all('div', class_='bix-div-container')
                
                if not question_divs:
                    print(f"No questions found on page {page_num}")
                    continue
                
                page_questions = 0
                for q_div in question_divs:
                    parsed_q = self.parse_question(q_div)
                    if parsed_q:
                        questions.append(parsed_q)
                        page_questions += 1
                
                print(f"Found {page_questions} questions on page {page_num}")
                
            except Exception as e:
                print(f"Error on page {page_num}: {str(e)}")
                continue
        
        return questions
    
    def scrape_url(self, url: str, max_pages: int = 10) -> Dict:
        """
        Main scraping function that returns all data
        
        Returns:
            Dict with 'questions', 'category', and 'total' keys
        """
        if not self.validate_url(url):
            raise ValueError("Invalid IndiaBix URL")
        
        category = self.extract_category_from_url(url)
        questions = self.scrape_section(url, max_pages)
        
        return {
            'questions': questions,
            'category': category,
            'total': len(questions),
            'url': url
        }


def test_scraper():
    """Test function for the scraper"""
    scraper = IndiaBixScraper()
    
    # Test URL
    test_url = "https://www.indiabix.com/general-knowledge/basic-general-knowledge/"
    
    try:
        result = scraper.scrape_url(test_url, max_pages=3)
        print(f"\nScraped {result['total']} questions from {result['category']}")
        
        if result['questions']:
            print("\nSample Question:")
            q = result['questions'][0]
            print(f"Q: {q['question']}")
            print(f"Options: {q['options']}")
            print(f"Answer: {q['answer']}")
            print(f"Explanation: {q['explanation'][:100]}...")
    
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    test_scraper()
