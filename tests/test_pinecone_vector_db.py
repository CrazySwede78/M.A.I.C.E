import unittest
from utils.pinecone_vector_db import use_pinecone

class TestPineconeVectorDB(unittest.TestCase):

    def setUp(self):
        self.vector_db = use_pinecone()

    def test_vector_db_connection(self):
        self.assertIsNotNone(self.vector_db, "Failed to connect to Pinecone Vector Database")

    def test_vector_db_insertion(self):
        test_data = {"id": "test", "vector": [1, 2, 3, 4, 5]}
        result = self.vector_db.insert(test_data)
        self.assertTrue(result, "Failed to insert data into Pinecone Vector Database")

    def test_vector_db_retrieval(self):
        test_id = "test"
        result = self.vector_db.retrieve(test_id)
        self.assertIsNotNone(result, "Failed to retrieve data from Pinecone Vector Database")

    def test_vector_db_deletion(self):
        test_id = "test"
        result = self.vector_db.delete(test_id)
        self.assertTrue(result, "Failed to delete data from Pinecone Vector Database")

if __name__ == '__main__':
    unittest.main()