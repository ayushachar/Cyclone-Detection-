# index.py
"""Index module for the RAG prototype.

- Stores embeddings in a local ChromaDB collection.
- Provides functions to add chunks and query.
"""

from .config import Config

def get_collection():
    """Placeholder returning a dummy collection object."""
    class DummyCollection:
        def add(self, ids, embeddings, metadatas, documents):
            print("[INFO] Added", len(ids), "documents to collection")
        def query(self, query_embeddings, n_results):
            # Return dummy results
            return {"ids": [], "distances": [], "documents": []}
    return DummyCollection()
