import unittest
from utils.openai_api import call_openai

class TestOpenaiApi(unittest.TestCase):

    def setUp(self):
        self.subject = "Artificial Intelligence"
        self.keywords = ["Machine Learning", "Neural Networks"]
        self.target_content_type = "Blog Post"
        self.word_count = 500

    def test_call_openai(self):
        response = call_openai(self.subject, self.keywords, self.target_content_type, self.word_count)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, str)
        self.assertGreaterEqual(len(response.split()), self.word_count)

if __name__ == '__main__':
    unittest.main()