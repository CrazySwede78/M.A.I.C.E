import unittest
from models.user_input import UserInput, UserInputSchema

class TestUserInput(unittest.TestCase):

    def setUp(self):
        self.user_input = UserInput()
        self.user_input_schema = UserInputSchema()

    def test_user_input_creation(self):
        data = {
            'subject': 'AI',
            'keywords': ['OpenAI', 'GPT-3'],
            'target_content_type': 'blog',
            'word_count': 1000
        }
        errors = self.user_input_schema.validate(data)
        self.assertEqual(len(errors), 0)

        user_input = self.user_input_schema.load(data)
        self.assertEqual(user_input.subject, 'AI')
        self.assertEqual(user_input.keywords, ['OpenAI', 'GPT-3'])
        self.assertEqual(user_input.target_content_type, 'blog')
        self.assertEqual(user_input.word_count, 1000)

    def test_user_input_invalid_data(self):
        data = {
            'subject': '',
            'keywords': [],
            'target_content_type': '',
            'word_count': -1
        }
        errors = self.user_input_schema.validate(data)
        self.assertNotEqual(len(errors), 0)

if __name__ == '__main__':
    unittest.main()