# AI Semantic Search Assistant

## Project Introduction
AI Semantic Search Assistant is a compact educational project that demonstrates how a semantic search system can compare keyword-based retrieval and embedding-based retrieval on the same document corpus. The application accepts a natural-language query, filters unsafe prompts, generates embeddings, and returns the most relevant documents using both TF-IDF and embedding similarity.

## Features
- Natural-language query input
- Prompt filtering for basic safety checks
- TF-IDF retrieval
- Embedding-based retrieval
- Cosine similarity and Euclidean distance comparison
- Simple Flask web UI

## Project Structure
```text
AI_Semantic_Search_Assistant/
├── app.py
├── prompt_filter.py
├── embedding.py
├── similarity.py
├── tfidf.py
├── search.py
├── dataset.txt
├── templates/
│   └── index.html
├── tests/
│   └── test_search.py
└── deliverables/
```

## Installation
```bash
pip install flask
```

## Usage
```bash
python app.py
```
Then open http://localhost:5000 and enter a query such as "machine learning", "semantic search", or "prompt injection".

## Future Improvements
- Replace the simple deterministic embedding with a real pretrained sentence-transformer model
- Add a vector database and ANN indexing for large corpora
- Improve prompt filtering with policy and classifier-based defense
- Add logging, analytics, and evaluation metrics for search quality
