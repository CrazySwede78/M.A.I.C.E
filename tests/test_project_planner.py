import unittest
from agents.project_planner import ProjectPlanner
from models.project import Project
from models.user_input import UserInput

class TestProjectPlanner(unittest.TestCase):

    def setUp(self):
        self.project_planner = ProjectPlanner()
        self.user_input = UserInput(subject="AI", keywords=["machine learning", "neural networks"], target_content_type="blog", word_count=1000)

    def test_create_project(self):
        project = self.project_planner.create_project(self.user_input)
        self.assertIsInstance(project, Project)
        self.assertEqual(project.subject, self.user_input.subject)
        self.assertEqual(project.keywords, self.user_input.keywords)
        self.assertEqual(project.target_content_type, self.user_input.target_content_type)
        self.assertEqual(project.word_count, self.user_input.word_count)

    def test_project_plan(self):
        project = self.project_planner.create_project(self.user_input)
        plan = self.project_planner.project_plan(project)
        self.assertIsInstance(plan, dict)
        self.assertIn('outline', plan)
        self.assertIn('parts', plan)
        self.assertIn('steps', plan)

if __name__ == '__main__':
    unittest.main()