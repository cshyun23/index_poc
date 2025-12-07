# File: /index-search-python/index-search-python/src/embeddings/embedder.py

import numpy as np
from sentence_transformers import SentenceTransformer

class Embedder:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)

    def create_embeddings(self, descriptions):
        return self.model.encode(descriptions, convert_to_tensor=True)

# File: /index-search-python/index-search-python/src/vector_search/elastic_client.py

from elasticsearch import Elasticsearch

class ElasticClient:
    def __init__(self, host='localhost', port=9200):
        self.client = Elasticsearch([{'host': host, 'port': port}])

    def index_document(self, index_name, doc_id, document):
        self.client.index(index=index_name, id=doc_id, body=document)

    def search_vector(self, index_name, vector, top_k=10):
        query = {
            "query": {
                "knn": {
                    "field": "vector_field",
                    "query_vector": vector,
                    "k": top_k
                }
            }
        }
        return self.client.search(index=index_name, body=query)

# File: /index-search-python/index-search-python/src/hierarchical/classifier.py

from langchain.llms import OpenAIChat

class Classifier:
    def __init__(self, llm_model='gpt-3.5-turbo'):
        self.llm = OpenAIChat(model=llm_model)

    def classify(self, input_text):
        prompt = f"Classify the following input into a 4-level hierarchy: {input_text}"
        response = self.llm(prompt)
        return response['choices'][0]['text'].strip()  # Assuming response format from LLM
