import unittest
from agents.part_definer import PartDefiner
from models.part import Part, PartSchema

class TestPartDefiner(unittest.TestCase):

    def setUp(self):
        self.part_definer = PartDefiner()
        self.part = Part(subject="Test Subject", keywords=["test", "subject"], target_content_type="Fiction", word_count=500)
        self.part_schema = PartSchema()

    def test_define_part(self):
        result = self.part_definer.define_part(self.part)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, Part)

    def test_validate_part(self):
        part_data = self.part_schema.dump(self.part)
        result = self.part_definer.validate_part(part_data)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()