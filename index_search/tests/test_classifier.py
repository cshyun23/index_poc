import unittest
from src.hierarchical.classifier import HierarchicalClassifier
from src.llm.langchain_client import LangChainClient

class TestHierarchicalClassifier(unittest.TestCase):

    def setUp(self):
        self.classifier = HierarchicalClassifier()
        self.llm_client = LangChainClient()

    def test_classification_accuracy(self):
        query = "Sample query for classification"
        expected_classification = "Expected Classification"
        classification = self.classifier.classify(query)
        self.assertEqual(classification, expected_classification)

    def test_llm_integration(self):
        query = "What is the best classification for this query?"
        response = self.llm_client.get_response(query)
        self.assertIsNotNone(response)
        self.assertIn("classification", response)

    def test_hierarchical_structure(self):
        structure = self.classifier.get_hierarchical_structure()
        self.assertIsInstance(structure, dict)
        self.assertGreater(len(structure), 0)

if __name__ == '__main__':
    unittest.main()