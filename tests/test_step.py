import unittest
from models.step import Step
from agents.step_generator import StepGenerator

class TestStep(unittest.TestCase):

    def setUp(self):
        self.step_generator = StepGenerator()
        self.step = Step()

    def test_generate_step(self):
        subject = "AI"
        keywords = ["Artificial Intelligence", "Machine Learning"]
        target_content_type = "Blog Post"
        word_count = 500

        generated_step = self.step_generator.generate_step(subject, keywords, target_content_type, word_count)

        self.assertIsInstance(generated_step, Step)
        self.assertEqual(generated_step.subject, subject)
        self.assertEqual(generated_step.keywords, keywords)
        self.assertEqual(generated_step.target_content_type, target_content_type)
        self.assertEqual(generated_step.word_count, word_count)

    def test_step_data(self):
        self.step.subject = "AI"
        self.step.keywords = ["Artificial Intelligence", "Machine Learning"]
        self.step.target_content_type = "Blog Post"
        self.step.word_count = 500

        self.assertEqual(self.step.subject, "AI")
        self.assertEqual(self.step.keywords, ["Artificial Intelligence", "Machine Learning"])
        self.assertEqual(self.step.target_content_type, "Blog Post")
        self.assertEqual(self.step.word_count, 500)

if __name__ == '__main__':
    unittest.main()