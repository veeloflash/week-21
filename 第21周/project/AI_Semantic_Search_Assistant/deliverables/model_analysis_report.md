# Model Analysis Report

## Why is Embedding better than Keyword Search?
Embedding-based retrieval can capture semantic relationships between words and phrases, so it can retrieve documents that use different vocabulary but express similar meaning. Keyword search is more literal and often misses paraphrases.

## Why is Cosine Similarity suitable for text?
Cosine similarity measures the angle between vectors, which makes it robust to document length differences. In text retrieval, it often reflects semantic closeness better than raw magnitude.

## When can Embedding fail?
Embedding can fail when the corpus is too small, the embeddings are too simplistic, or the query is ambiguous. It may also struggle with domain-specific terms that are underrepresented in the training data.

## How can we improve search quality?
- Use pretrained sentence-transformer models instead of a handcrafted embedding demo
- Add a vector database and approximate nearest neighbor search
- Combine lexical and semantic retrieval in a hybrid system
- Fine-tune the retriever on domain-specific data
