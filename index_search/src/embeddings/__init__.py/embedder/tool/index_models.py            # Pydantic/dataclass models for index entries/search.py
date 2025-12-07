# File: /index-search-python/index-search-python/src/embeddings/embedder.py

import numpy as np
from sentence_transformers import SentenceTransformer

class Embedder:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)

    def create_embeddings(self, descriptions):
        return self.model.encode(descriptions, convert_to_tensor=True)

# File: /index-search-python/index-search-python/src/llm/langchain_client.py

from langchain.chat_models import ChatOpenAI

class LangChainClient:
    def __init__(self, api_key, model_name='gpt-3.5-turbo'):
        self.client = ChatOpenAI(api_key=api_key, model_name=model_name)

    def query(self, prompt):
        response = self.client.chat([{"role": "user", "content": prompt}])
        return response['choices'][0]['message']['content']

# File: /index-search-python/index-search-python/src/models/index_models.py

from pydantic import BaseModel
from typing import List, Optional

class IndexEntry(BaseModel):
    id: int
    description: str
    country: str
    type: str
    level_1: str
    level_2: str
    level_3: str
    level_4: str
    embedding: Optional[List[float]] = None

# File: /index-search-python/index-search-python/src/services/ingest.py

from .embeddings.embedder import Embedder
from ..models.index_models import IndexEntry
import sqlite3

class IngestPipeline:
    def __init__(self, db_path):
        self.db_path = db_path
        self.embedder = Embedder()

    def ingest(self, descriptions):
        embeddings = self.embedder.create_embeddings(descriptions)
        entries = [IndexEntry(id=i, description=desc, embedding=embeddings[i].tolist()) for i, desc in enumerate(descriptions)]
        self.save_to_db(entries)

    def save_to_db(self, entries):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS index_entries (id INTEGER PRIMARY KEY, description TEXT, embedding BLOB)''')
        for entry in entries:
            cursor.execute('INSERT INTO index_entries (id, description, embedding) VALUES (?, ?, ?)', (entry.id, entry.description, entry.embedding))
        conn.commit()
        conn.close()