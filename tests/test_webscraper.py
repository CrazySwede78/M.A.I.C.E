import unittest
from utils.webscraper import scrape_web

class TestWebScraper(unittest.TestCase):

    def setUp(self):
        self.url = "https://www.example.com"
        self.keywords = ["example", "test"]

    def test_scrape_web(self):
        result = scrape_web(self.url, self.keywords)
        self.assertIsInstance(result, dict)
        self.assertIn('content', result)
        self.assertIn('keywords_found', result)
        self.assertTrue(all(keyword in result['content'] for keyword in self.keywords))

if __name__ == '__main__':
    unittest.main()