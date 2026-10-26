# ingest.py
"""Ingestion module for the RAG prototype.

- Loads PDFs, .txt, .md files from the DOCS_DIR.
- Extracts text per page using PyMuPDF (fitz) for PDFs and plain read for txt/md.
- Returns a list of dicts with keys: `doc_id`, `page_num`, `content`.
"""

import os
import fitz  # PyMuPDF
from .config import Config

def ingest_documents():
    docs_path = os.path.abspath(Config.DOCS_DIR)
    records = []
    for root, _, files in os.walk(docs_path):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            full_path = os.path.join(root, file)
            if ext == ".pdf":
                records.extend(_ingest_pdf(full_path))
            elif ext in {".txt", ".md"}:
                records.append({
                    "doc_id": file,
                    "page_num": 0,
                    "content": _read_text(full_path),
                })
    return records

def _ingest_pdf(path):
    doc = fitz.open(path)
    out = []
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text("text")
        if not text.strip():
            # Log pages with no text for potential OCR
            print(f"[WARN] Empty page {page_num+1} in {os.path.basename(path)}")
        out.append({
            "doc_id": os.path.basename(path),
            "page_num": page_num + 1,
            "content": text,
        })
    return out

def _read_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
