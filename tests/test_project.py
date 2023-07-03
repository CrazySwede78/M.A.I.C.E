import unittest
from models.project import Project
from models.user_input import UserInput

class TestProject(unittest.TestCase):

    def setUp(self):
        self.user_input = UserInput(subject="AI", keywords=["machine learning", "neural networks"], target_content_type="blog", word_count=1000)
        self.project = Project(self.user_input)

    def test_create_project(self):
        self.assertEqual(self.project.subject, "AI")
        self.assertEqual(self.project.keywords, ["machine learning", "neural networks"])
        self.assertEqual(self.project.target_content_type, "blog")
        self.assertEqual(self.project.word_count, 1000)

    def test_project_plan(self):
        self.project.create_project_plan()
        self.assertIsNotNone(self.project.plan)

    def test_project_outline(self):
        self.project.create_outline()
        self.assertIsNotNone(self.project.outline)

    def test_project_parts(self):
        self.project.define_parts()
        self.assertIsNotNone(self.project.parts)

    def test_project_steps(self):
        self.project.generate_steps()
        self.assertIsNotNone(self.project.steps)

    def test_project_merge_verify(self):
        self.project.merge_verify()
        self.assertTrue(self.project.is_verified)

if __name__ == '__main__':
    unittest.main()