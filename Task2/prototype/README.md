# Prototype README

This prototype implements a Retrieval Augmented Generation (RAG) system for querying cyclone operation documents.

## Setup
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Commands
- `python rag_prototype.py ingest` – ingest documents in `docs/`.
- `python rag_prototype.py ask "<question>"` – ask a single question.
- `python rag_prototype.py chat` – interactive chat mode.
- `python rag_prototype.py eval` – run evaluation on `data/eval_questions.json`.

See the module docstrings for detailed usage.
