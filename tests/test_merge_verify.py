import unittest
from models.merge_verify import MergeVerify
from models.user_input import UserInput

class TestMergeVerify(unittest.TestCase):

    def setUp(self):
        self.user_input = UserInput(subject="AI", keywords=["Machine Learning", "Deep Learning"], target_content_type="Blog", word_count=1000)
        self.merge_verify = MergeVerify(self.user_input)

    def test_merge(self):
        self.merge_verify.merge()
        self.assertIsNotNone(self.merge_verify.merged_content, "Merged content should not be None after merge operation")

    def test_verify(self):
        self.merge_verify.merge()
        is_verified = self.merge_verify.verify()
        self.assertTrue(is_verified, "Verification failed for the merged content")

    def test_get_merged_content(self):
        self.merge_verify.merge()
        content = self.merge_verify.get_merged_content()
        self.assertEqual(content, self.merge_verify.merged_content, "Returned content is not equal to the merged content")

    def test_get_verification_status(self):
        self.merge_verify.merge()
        self.merge_verify.verify()
        status = self.merge_verify.get_verification_status()
        self.assertEqual(status, self.merge_verify.verification_status, "Returned status is not equal to the verification status")

if __name__ == '__main__':
    unittest.main()