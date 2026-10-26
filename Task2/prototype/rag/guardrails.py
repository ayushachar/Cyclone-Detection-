# guardrails.py
"""Guardrails module for the RAG prototype.

- Checks for unsafe queries (keyword based).
- Determines if retrieved context is sufficient (simple similarity placeholder).
- Enforces citation presence.
- Provides fallback responses.
"""

from .config import Config

UNSAFE_KEYWORDS = Config.SENSITIVE_KEYWORDS

def is_unsafe(query: str) -> bool:
    """Return True if the query contains any unsafe keyword."""
    lowered = query.lower()
    return any(kw in lowered for kw in UNSAFE_KEYWORDS)

def has_citations(answer: str) -> bool:
    """Very naive check for citation pattern `[doc, p.X]`."""
    return "[" in answer and ", p." in answer and "]" in answer

def guard_answer(question: str, answer: str, retrieved_chunks: list[dict]) -> str:
    """Apply guardrails to the generated answer.
    - If unsafe query -> refuse.
    - If no citations -> fallback to extractive snippets.
    - If no retrieved chunks -> "I don't know".
    """
    if is_unsafe(question):
        return "I’m sorry, I can’t help with that request."
    if not retrieved_chunks:
        return "I could not find an answer in the provided documents."
    if not has_citations(answer):
        # Simple extractive fallback: concatenate first two chunks with citations
        snippets = []
        for chunk in retrieved_chunks[:2]:
            citation = f"[{chunk['doc_id']}, p.{chunk['page_num']}]"
            snippets.append(f"{chunk['content'][:200]}... {citation}")
        return " ".join(snippets)
    return answer
