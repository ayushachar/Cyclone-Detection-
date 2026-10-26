# rag_prototype.py
"""CLI entry point for the RAG prototype.

Usage:
  python rag_prototype.py ingest          # ingest documents
  python rag_prototype.py ask "question"   # ask a single question
  python rag_prototype.py chat            # interactive chat mode
  python rag_prototype.py eval            # run evaluation
"""

import argparse
from .rag import ingest, config

def main():
    parser = argparse.ArgumentParser(description="RAG prototype CLI")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("ingest", help="Ingest documents")
    ask_parser = subparsers.add_parser("ask", help="Ask a question")
    ask_parser.add_argument("question", type=str, help="Question to ask")
    subparsers.add_parser("chat", help="Interactive chat")
    subparsers.add_parser("eval", help="Run evaluation")

    args = parser.parse_args()
    if args.command == "ingest":
        records = ingest.ingest_documents()
        print(f"Ingested {len(records)} records")
    elif args.command == "ask":
        print(f"Would answer: {args.question}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
