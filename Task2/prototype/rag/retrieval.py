# retrieval.py
"""Retrieval module for the RAG prototype.

- Performs hybrid dense + BM25 retrieval (placeholder implementation).
- Returns a list of candidate chunk dicts.
"""

from .config import Config

def hybrid_retrieve(query: str, top_k: int = Config.TOP_K_DENSE):
    """Placeholder that returns empty list of results.
    In a real implementation this would query ChromaDB and BM25.
    """
    print(f"[INFO] Retrieval called for query: {query}")
    return []
