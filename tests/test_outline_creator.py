import unittest
from agents.outline_creator import OutlineCreator
from models.outline import Outline
from models.user_input import UserInput

class TestOutlineCreator(unittest.TestCase):

    def setUp(self):
        self.outline_creator = OutlineCreator()
        self.user_input = UserInput(subject="AI", keywords=["Machine Learning", "Deep Learning"], target_content_type="Blog", word_count=1000)

    def test_create_outline(self):
        outline = self.outline_creator.create_outline(self.user_input)
        self.assertIsInstance(outline, Outline)
        self.assertEqual(outline.subject, self.user_input.subject)
        self.assertEqual(outline.keywords, self.user_input.keywords)
        self.assertEqual(outline.target_content_type, self.user_input.target_content_type)
        self.assertEqual(outline.word_count, self.user_input.word_count)

    def test_update_outline(self):
        outline = self.outline_creator.create_outline(self.user_input)
        new_keywords = ["Neural Networks", "AI Ethics"]
        updated_outline = self.outline_creator.update_outline(outline, new_keywords)
        self.assertEqual(updated_outline.keywords, new_keywords)

    def test_delete_outline(self):
        outline = self.outline_creator.create_outline(self.user_input)
        self.outline_creator.delete_outline(outline)
        self.assertIsNone(outline.subject)
        self.assertIsNone(outline.keywords)
        self.assertIsNone(outline.target_content_type)
        self.assertIsNone(outline.word_count)

if __name__ == '__main__':
    unittest.main()