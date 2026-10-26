# rerank.py
"""Reranking module for the RAG prototype.

- Uses a cross‑encoder to rerank retrieved chunks (placeholder).
"""

from .config import Config

def rerank_chunks(query: str, candidates: list[dict]):
    """Placeholder that returns the input candidates unchanged.
    In a real implementation this would score with a cross‑encoder.
    """
    print(f"[INFO] Reranking {len(candidates)} candidates for query: {query}")
    return candidates
