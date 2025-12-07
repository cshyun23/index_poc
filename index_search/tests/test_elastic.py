import unittest
from src.vector_search.elastic_client import ElasticClient

class TestElasticClient(unittest.TestCase):

    def setUp(self):
        self.client = ElasticClient()

    def test_connection(self):
        self.assertTrue(self.client.ping())

    def test_index_creation(self):
        index_name = "test_index"
        self.client.create_index(index_name)
        self.assertTrue(self.client.index_exists(index_name))

    def test_vector_query(self):
        index_name = "test_index"
        query_vector = [0.1, 0.2, 0.3, 0.4, 0.5]
        results = self.client.vector_query(index_name, query_vector)
        self.assertIsInstance(results, list)

    def tearDown(self):
        index_name = "test_index"
        self.client.delete_index(index_name)

if __name__ == '__main__':
    unittest.main()