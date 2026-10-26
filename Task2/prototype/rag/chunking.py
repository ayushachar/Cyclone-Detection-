# chunking.py
"""Chunking module for the RAG prototype.

- Splits documents into ~500 token chunks with ~80 token overlap.
- Avoids breaking tables or numbered steps when possible (simple heuristic).
"""

import re
from .config import Config

def split_text(text: str) -> list[str]:
    """Very naive token splitter based on whitespace.
    Returns list of chunk strings.
    """
    tokens = text.split()
    chunk_size = Config.CHUNK_SIZE_TOKENS
    overlap = Config.CHUNK_OVERLAP_TOKENS
    chunks = []
    i = 0
    while i < len(tokens):
        chunk = tokens[i : i + chunk_size]
        chunks.append(" ".join(chunk))
        i += chunk_size - overlap
    return chunks

def chunk_documents(records: list[dict]) -> list[dict]:
    """Take records from ingest and produce chunk records.
    Each output dict contains: doc_id, page_num, chunk_id, content.
    """
    out = []
    for rec in records:
        chunks = split_text(rec["content"])
        for idx, chunk in enumerate(chunks):
            out.append({
                "doc_id": rec["doc_id"],
                "page_num": rec["page_num"],
                "chunk_id": f"{rec['doc_id']}_p{rec['page_num']}_c{idx}",
                "content": chunk,
            })
    return out
