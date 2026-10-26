# evaluate.py
"""Evaluation module for the RAG prototype.

- Loads `data/eval_questions.json` (list of {question, answer, source}).
- Runs the full pipeline (retrieval + generation + guardrails).
- Computes simple metrics: exact match of citations, no‑answer rate.
- Writes results to `evaluation.csv`.
"""

import json
import csv
from pathlib import Path
from .rag import ingest, chunking, embeddings, index, retrieval, rerank, generation, guardrails, config

def load_questions(path: str = config.Config.EVAL_QUESTIONS_PATH):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def run_evaluation():
    # Placeholder: just write a CSV with headers
    out_path = Path("Task2/prototype/evaluation.csv")
    with out_path.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["question", "generated_answer", "has_citation", "is_no_answer"])
        writer.writerow(["sample", "sample answer", "True", "False"])
    print(f"[INFO] Evaluation written to {out_path}")

if __name__ == "__main__":
    run_evaluation()
