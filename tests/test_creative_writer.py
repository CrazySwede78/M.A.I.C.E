import unittest
from agents.creative_writer import CreativeWriter
from models.user_input import UserInput

class TestCreativeWriter(unittest.TestCase):

    def setUp(self):
        self.creative_writer = CreativeWriter()
        self.user_input = UserInput(subject="Space Exploration", keywords=["Mars", "Rover", "NASA"], target_content_type="Blog Post", word_count=1000)

    def test_generate_content(self):
        content = self.creative_writer.generate_content(self.user_input)
        self.assertIsNotNone(content)
        self.assertIsInstance(content, str)
        self.assertGreaterEqual(len(content.split()), self.user_input.word_count)

    def test_generate_parts(self):
        parts = self.creative_writer.generate_parts(self.user_input)
        self.assertIsNotNone(parts)
        self.assertIsInstance(parts, list)
        self.assertGreater(len(parts), 0)

    def test_generate_outline(self):
        outline = self.creative_writer.generate_outline(self.user_input)
        self.assertIsNotNone(outline)
        self.assertIsInstance(outline, dict)
        self.assertGreater(len(outline), 0)

    def test_generate_project_plan(self):
        project_plan = self.creative_writer.generate_project_plan(self.user_input)
        self.assertIsNotNone(project_plan)
        self.assertIsInstance(project_plan, dict)
        self.assertGreater(len(project_plan), 0)

    def test_merge_and_verify_content(self):
        content = self.creative_writer.generate_content(self.user_input)
        parts = self.creative_writer.generate_parts(self.user_input)
        merged_content = self.creative_writer.merge_and_verify_content(parts)
        self.assertEqual(content, merged_content)

if __name__ == '__main__':
    unittest.main()