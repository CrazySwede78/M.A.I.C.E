import unittest
from models.outline import Outline
from agents.outline_creator import OutlineCreator

class TestOutline(unittest.TestCase):

    def setUp(self):
        self.outline_creator = OutlineCreator()
        self.user_input = {
            'subject': 'AI',
            'keywords': ['Artificial Intelligence', 'Machine Learning'],
            'target_content_type': 'Blog Post',
            'word_count': 1000
        }

    def test_create_outline(self):
        outline = self.outline_creator.create_outline(self.user_input)
        self.assertIsInstance(outline, Outline)
        self.assertEqual(outline.subject, self.user_input['subject'])
        self.assertEqual(outline.keywords, self.user_input['keywords'])
        self.assertEqual(outline.target_content_type, self.user_input['target_content_type'])
        self.assertEqual(outline.word_count, self.user_input['word_count'])

    def test_outline_parts(self):
        outline = self.outline_creator.create_outline(self.user_input)
        self.assertGreater(len(outline.parts), 0)

    def test_outline_steps(self):
        outline = self.outline_creator.create_outline(self.user_input)
        for part in outline.parts:
            self.assertGreater(len(part.steps), 0)

if __name__ == '__main__':
    unittest.main()