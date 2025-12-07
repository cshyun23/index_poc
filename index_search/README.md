# Index Search Python Project

## Overview
This project implements an index searching application that utilizes two methods for searching: vector similarity and hierarchical classification. The application is designed to handle index descriptions and user queries efficiently, leveraging modern AI techniques and database management systems.

## Features
- **Vector Similarity Search**: Uses embeddings to represent index descriptions and performs searches based on vector similarity.
- **Hierarchical Classification**: Implements a four-level classification system to categorize index entries by country, type, and other criteria, utilizing a language model for enhanced matching.
- **Database Integration**: Utilizes SQLite for relational database management and Elasticsearch for vector search capabilities.
- **LLM Inference**: Integrates with LangChain's OpenAIChat class for language model inference to enhance search results.

## Project Structure
```
index-search-python
├── src
│   ├── main.py
│   ├── config.py
│   ├── embeddings
│   │   ├── __init__.py
│   │   └── embedder.py
│   ├── vector_search
│   │   ├── __init__.py
│   │   └── elastic_client.py
│   ├── hierarchical
│   │   ├── __init__.py
│   │   └── classifier.py
│   ├── db
│   │   ├── __init__.py
│   │   └── sqlite_manager.py
│   ├── llm
│   │   ├── __init__.py
│   │   └── langchain_client.py
│   ├── models
│   │   └── index_models.py
│   ├── services
│   │   ├── ingest.py
│   │   └── search.py
│   └── utils
│       └── helpers.py
├── tests
│   ├── test_embedder.py
│   ├── test_elastic.py
│   ├── test_sqlite.py
│   └── test_classifier.py
├── scripts
│   ├── ingest_sample.py
│   └── demo_query.py
├── requirements.txt
├── pyproject.toml
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd index-search-python
   ```
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
- To run the application, execute the main script:
  ```
  python src/main.py
  ```
- For data ingestion, use the provided script:
  ```
  python scripts/ingest_sample.py
  ```
- To demonstrate querying capabilities, run:
  ```
  python scripts/demo_query.py
  ```

## Testing
Unit tests are provided for each component of the application. To run the tests, use:
```
pytest tests/
```

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.