# Configuration for the RAG prototype

class Config:
    """Central configuration holder.

    All paths are relative to the repository root.
    """

    # Directories
    DOCS_DIR = "Task2/prototype/docs"
    CHUNKS_DIR = "Task2/prototype/rag/chunks"
    INDEX_DIR = "Task2/prototype/rag/index"
    LOG_FILE = "Task2/prototype/query_logs.jsonl"

    # Model identifiers
    EMBEDDING_MODEL = "sentence-transformers/BAAI/bge-small-en-v1.5"
    FALLBACK_EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
    RERANKER_MODEL = "cross-encoder/ms-marco-MiniLM-L-6-v2"
    GENERATOR_MODEL = "google/flan-t5-base"

    # Retrieval parameters
    CHUNK_SIZE_TOKENS = 500
    CHUNK_OVERLAP_TOKENS = 80
    TOP_K_DENSE = 20
    TOP_K_RERANK = 4
    NO_ANSWER_THRESHOLD = 0.3  # similarity score below which we say "I don't know"

    # Guardrails
    SENSITIVE_KEYWORDS = [
        "bypass", "disable", "override", "password", "credential",
        "alarm", "interlock", "safety", "shutdown", "ignore previous instructions"
    ]
"
