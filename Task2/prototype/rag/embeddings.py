# embeddings.py
"""Embeddings module for the RAG prototype.

- Provides function to compute embeddings for text chunks using the configured model.
- Falls back to a second model if the primary fails.
"""

from .config import Config

def get_embedding_model():
    """Return the model name to use for embeddings."""
    return Config.EMBEDDING_MODEL

def compute_embeddings(texts: list[str]):
    """Placeholder that returns dummy vectors.
    In a real implementation this would load the sentence-transformers model.
    """
    # Return list of zero vectors of length 768 as placeholder
    dim = 768
    return [[0.0] * dim for _ in texts]
