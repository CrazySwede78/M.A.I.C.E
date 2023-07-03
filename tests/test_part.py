import unittest
from models.part import Part
from agents.part_definer import PartDefiner

class TestPart(unittest.TestCase):

    def setUp(self):
        self.part_definer = PartDefiner()
        self.part = Part()

    def test_define_part(self):
        subject = "AI"
        keywords = ["Machine Learning", "Deep Learning"]
        target_content_type = "Blog"
        word_count = 1000

        defined_part = self.part_definer.define_part(subject, keywords, target_content_type, word_count)

        self.assertEqual(defined_part.subject, subject)
        self.assertEqual(defined_part.keywords, keywords)
        self.assertEqual(defined_part.target_content_type, target_content_type)
        self.assertEqual(defined_part.word_count, word_count)

    def test_part_data(self):
        self.part.subject = "AI"
        self.part.keywords = ["Machine Learning", "Deep Learning"]
        self.part.target_content_type = "Blog"
        self.part.word_count = 1000

        self.assertEqual(self.part.subject, "AI")
        self.assertEqual(self.part.keywords, ["Machine Learning", "Deep Learning"])
        self.assertEqual(self.part.target_content_type, "Blog")
        self.assertEqual(self.part.word_count, 1000)

if __name__ == '__main__':
    unittest.main()