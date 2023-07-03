import unittest
from utils.google_search import search_google

class TestGoogleSearch(unittest.TestCase):

    def setUp(self):
        self.query = "creative writing techniques"
        self.num_results = 5

    def test_search_google(self):
        results = search_google(self.query, self.num_results)
        self.assertIsNotNone(results)
        self.assertEqual(len(results), self.num_results)
        for result in results:
            self.assertIn(self.query, result.lower())

if __name__ == '__main__':
    unittest.main()