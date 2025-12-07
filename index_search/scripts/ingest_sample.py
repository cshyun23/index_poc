# Sample input for the ingest pipeline
import json

def sample_data():
    return [
        {
            "id": 1,
            "title": "Sample Document 1",
            "description": "This is a sample document description for testing.",
            "country": "USA",
            "type": "Report",
            "category": "Finance",
            "sub_category": "Investment",
            "tags": ["finance", "investment", "report"]
        },
        {
            "id": 2,
            "title": "Sample Document 2",
            "description": "Another sample document for ingestion.",
            "country": "Canada",
            "type": "Article",
            "category": "Technology",
            "sub_category": "AI",
            "tags": ["technology", "AI", "article"]
        },
        {
            "id": 3,
            "title": "Sample Document 3",
            "description": "This document discusses environmental issues.",
            "country": "Australia",
            "type": "Research",
            "category": "Environment",
            "sub_category": "Climate Change",
            "tags": ["environment", "research", "climate"]
        }
    ]

if __name__ == "__main__":
    data = sample_data()
    print(json.dumps(data, indent=4))