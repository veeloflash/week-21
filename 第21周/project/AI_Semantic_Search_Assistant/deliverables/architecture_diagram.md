# Architecture Diagram

```text
User
  |
  v
Input Text
  |
  v
Prompt Filter
  |
  v
Embedding Generator
  |
  v
Search Engine
  |---------------------------|
  |                           |
  v                           v
TF-IDF Retrieval          Embedding Retrieval
  |                           |
  v                           v
Similarity Scoring       Similarity Scoring
  |                           |
  +-----------+---------------+
              |
              v
         Ranking and Top-5
              |
              v
           Web UI
```

## Module Responsibilities
- Prompt Filter: blocks obvious injection-style prompts and enforces input constraints
- Embedding Generator: converts text into simple bag-of-words style vectors for demo purposes
- TF-IDF Retrieval: ranks documents using statistical term relevance
- Similarity Scoring: computes cosine similarity and Euclidean distance
- Search Engine: coordinates retrieval and ranking for both methods
- Web UI: displays query input and results to the user
