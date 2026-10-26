# generation.py
"""Generation module for the RAG prototype.

- Loads a free, CPU‑runnable LLM (Google Flan‑T5‑Base) via Hugging Face Transformers.
- Builds a prompt that includes the retrieved context and the user question.
- Generates an answer, enforces citation format, and falls back to extractive snippets when needed.
"""

from .config import Config
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline

# Lazy‑load the model only once per process
_model = None
_tokenizer = None

def _load_model():
    global _model, _tokenizer
    if _model is None:
        _tokenizer = AutoTokenizer.from_pretrained(Config.GENERATOR_MODEL)
        _model = AutoModelForSeq2SeqLM.from_pretrained(Config.GENERATOR_MODEL)
    return _model, _tokenizer

def _has_citation(text: str) -> bool:
    """Very naive check for a citation pattern like [doc_name, p.3]."""
    return "[" in text and ", p." in text and "]" in text

def generate_answer(question: str, retrieved_chunks: list[dict]) -> str:
    """Generate an answer using the LLM.

    If no chunks are retrieved, return a graceful "I don't know" message.
    If the model output lacks citations, fall back to an extractive answer built from the first two chunks.
    """
    if not retrieved_chunks:
        return "I could not find an answer in the provided documents."

    # Build a prompt that includes up to three chunks of context
    context = "\n".join(chunk["content"] for chunk in retrieved_chunks[:3])
    prompt = (
        f"Context:\n{context}\n\n"
        f"Question: {question}\n"
        "Answer (include citations in the form [doc_name, p.X]):"
    )

    # Load model and run inference on CPU (device=-1)
    model, tokenizer = _load_model()
    pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer, device=-1)
    result = pipe(prompt, max_length=256, do_sample=False)[0]["generated_text"].strip()

    # Ensure we have at least one citation; otherwise fallback to extractive snippets
    if not _has_citation(result):
        snippets = []
        for chunk in retrieved_chunks[:2]:
            citation = f"[{chunk['doc_id']}, p.{chunk['page_num']}]"
            snippets.append(f"{chunk['content'][:200]}... {citation}")
        return " ".join(snippets)

    return result
