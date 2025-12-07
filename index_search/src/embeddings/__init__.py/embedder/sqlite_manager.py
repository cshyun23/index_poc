# File: /index-search-python/index-search-python/src/embeddings/embedder.py

import numpy as np
from sentence_transformers import SentenceTransformer

class Embedder:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)

    def create_embeddings(self, descriptions):
        return self.model.encode(descriptions, convert_to_tensor=True)

# File: /index-search-python/index-search-python/src/db/sqlite_manager.py

import sqlite3

class SQLiteManager:
    def __init__(self, db_name='index.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_schema()

    def create_schema(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS index_entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                embedding BLOB NOT NULL
            )
        ''')
        self.connection.commit()

    def insert_entry(self, description, embedding):
        self.cursor.execute('''
            INSERT INTO index_entries (description, embedding) VALUES (?, ?)
        ''', (description, embedding))
        self.connection.commit()

    def fetch_all_entries(self):
        self.cursor.execute('SELECT * FROM index_entries')
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()