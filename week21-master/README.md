# Week21_AI_Semantic_Search_Assistant

This project is a compact Flask-based semantic search assistant that compares TF-IDF, dense vector similarity, and a simple gradient descent demo in one runnable package.

## Overview

The application lets users submit a natural-language query and view multiple retrieval strategies side by side. It is intended as an educational product that shows how keyword-based search and embedding-style search behave on the same document corpus.

## Features

- Query input with prompt filtering
- TF-IDF ranking results
- Cosine similarity comparison
- Embedding-style retrieval results
- Simple gradient summury showing how it works, showing its loss, w and b.
- Failure analysis for ambiguous or out-of-domain queries
- Embedding search similarity

## Project Structure
Copied from Powershell.
```text
D:.
│  app.py
│  dataset.txt
│  prompt_filter.py
│  README.md
│  requirements.txt
│  Week21_Theory_Assignment.docx
│
├─static
│      app.css
│      app.js
│
├─templates
│      index.html
│
├─tests
│  │  test_product_flow.py
│  │  test_search.py
│  │
│  └─fixtures
│          sample_queries.json
│
└─Week21_Engineering
    ├─Implementation1
    │  └─Similarity_Engine
    │          similarity.py
    │
    ├─Implementation2
    │  └─TFIDF_Retrieval
    │          tfidf_search.py
    │
    ├─Implementation3
    │  └─Embedding_Similarity
    │          embedding_similarity.py
    │
    ├─Implementation4
    │  └─Vector_Search
    │          vector_search.py
    │
    ├─Implementation5
    │  └─Embedding_Search
    │          embedding_search.py
    │
    ├─Implementation6
    │  └─Gradient_Descent
    │          gradient_descent_demo.py
    │
    └─Implementation7
        └─Embedding_Failure_Analysis
                embedding_failure_analysis.py
```

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python app.py
```

Then open http://localhost:5000 and enter a query such as "machine learning", "semantic search", or "bank".

## Verification

The repository now includes:

- regression tests in the tests folder
- a testing report in deliverables/testing_results.md
- security and model analysis reports in deliverables/
- a user manual and architecture diagram

## Notes

The current implementation uses a deterministic fallback embedding strategy when a pretrained sentence-transformer model is unavailable, which makes the project reproducible in a classroom environment.

## Prompt Filtering

Added a strong pronpt filtering including, hidden symbels, random symbels and promopt ignoring, also a comparation of the system before filtering and system after filtering.  
The result increase from 50% to 100%

## Learn more
there are also information in project reflection.md, dataset.txt, example.png(3 of them) for see what is the result and requirement.txt.