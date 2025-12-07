# demo_query.py

import sys
from src.vector_search.elastic_client import ElasticClient
from src.hierarchical.classifier import Classifier
from src.llm.langchain_client import LangChainClient

def main():
    # Initialize Elasticsearch client
    elastic_client = ElasticClient()
    
    # Initialize hierarchical classifier
    classifier = Classifier()
    
    # Initialize LangChain client for LLM inference
    llm_client = LangChainClient()

    # Sample user query
    user_query = input("Enter your search query: ")

    # Perform vector search
    vector_results = elastic_client.vector_search(user_query)
    print("Vector Search Results:")
    for result in vector_results:
        print(result)

    # Perform hierarchical classification
    classification_results = classifier.classify(user_query)
    print("Hierarchical Classification Results:")
    for result in classification_results:
        print(result)

    # Use LLM to refine search results
    refined_results = llm_client.refine_results(user_query, vector_results, classification_results)
    print("Refined Results from LLM:")
    for result in refined_results:
        print(result)

if __name__ == "__main__":
    main()