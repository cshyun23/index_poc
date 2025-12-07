import unittest
import pytest
from src.embeddings.embedder import Embedder

class TestEmbedder(unittest.TestCase):

    def setUp(self):
        self.embedder = Embedder()

    def test_embedding_creation(self):
        description = "This is a test description."
        embedding = self.embedder.create_embedding(description)
        self.assertIsNotNone(embedding)
        self.assertEqual(len(embedding), self.embedder.embedding_dimension)

    def test_embedding_similarity(self):
        description1 = "This is a test description."
        description2 = "This is another test description."
        embedding1 = self.embedder.create_embedding(description1)
        embedding2 = self.embedder.create_embedding(description2)
        similarity = self.embedder.calculate_similarity(embedding1, embedding2)
        self.assertGreaterEqual(similarity, 0)

@pytest.mark.parametrize("q", EASY_QUERIES)
def test_easy_queries_nonempty(q):
    # 실제 시스템에 연결하여 분류/검색 결과를 검증하도록 확장 가능
    assert isinstance(q, str) and len(q) > 0

@pytest.mark.parametrize("q", MEDIUM_QUERIES)
def test_medium_queries_nonempty(q):
    assert isinstance(q, str) and len(q) > 0

@pytest.mark.parametrize("q", HARD_QUERIES)
def test_hard_queries_nonempty(q):
    assert isinstance(q, str) and len(q) > 0

if __name__ == '__main__':
    unittest.main()