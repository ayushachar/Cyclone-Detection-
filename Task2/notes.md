# Task 2 Notes

*Architecture* – The pipeline consists of ingestion → chunking → embeddings → vector store (ChromaDB) + BM25 → hybrid retrieval → cross‑encoder rerank → LLM generation → output guardrails (unsafe query filter, citation check, no‑answer fallback).

*Chunking* – ~500 token chunks with 80 token overlap. Simple whitespace splitter; tables and numbered steps are kept intact by a naive heuristic (future work: regex‑based detection).

*Embeddings* – Primary model `sentence‑transformers/BAAI/bge-small-en-v1.5` with instruction prefix; fallback `all‑MiniLM‑L6‑v2`.

*Retrieval* – Dense search via ChromaDB, BM25 via `rank‑bm25`, fused with Reciprocal Rank Fusion. Top‑20 dense → rerank to top‑4.

*Guardrails* – Keyword‑based unsafe query detection, citation enforcement, similarity‑based no‑answer threshold (placeholder).

*Evaluation* – Placeholder evaluation writes a CSV with simple columns; real metrics will be added later.

*Next steps* – Implement real chunking heuristics, load actual models, add faithfulness NLI check, populate `docs/` with real or synthetic PDFs, run full end‑to‑end tests.
