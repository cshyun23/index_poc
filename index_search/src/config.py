# Configuration settings for the index searching application

DATABASE_URI = "sqlite:///path/to/your/database.db"  # SQLite database connection string
ELASTICSEARCH_HOST = "http://localhost:9200"  # Elasticsearch server URL
EMBEDDING_MODEL = "text-embedding-model"  # Specify the embedding model to use
LLM_MODEL = "gpt-3.5-turbo"  # Specify the LLM model to use
INDEX_NAME = "your_index_name"  # Name of the Elasticsearch index
HIERARCHY_LEVELS = 4  # Number of levels in the hierarchical classification
BATCH_SIZE = 32  # Batch size for processing data
TIMEOUT = 30  # Timeout for database and API calls

# Add any additional configuration settings as needed