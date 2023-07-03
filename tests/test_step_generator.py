```python
import unittest
from agents.step_generator import StepGenerator
from models.step import Step
from models.user_input import UserInput

class TestStepGenerator(unittest.TestCase):

    def setUp(self):
        self.step_generator = StepGenerator()
        self.user_input = UserInput(subject="Space Exploration", keywords=["Mars", "Rover", "NASA"], target_content_type="Blog Post", word_count=1000)

    def test_generate_step(self):
        step = self.step_generator.generate_step(self.user_input)
        self.assertIsInstance(step, Step)
        self.assertEqual(step.subject, self.user_input.subject)
        self.assertEqual(step.keywords, self.user_input.keywords)
        self.assertEqual(step.target_content_type, self.user_input.target_content_type)
        self.assertEqual(step.word_count, self.user_input.word_count)

    def test_step_content(self):
        step = self.step_generator.generate_step(self.user_input)
        self.assertIsNotNone(step.content)
        self.assertTrue(len(step.content.split()) <= self.user_input.word_count)

if __name__ == '__main__':
    unittest.main()
```