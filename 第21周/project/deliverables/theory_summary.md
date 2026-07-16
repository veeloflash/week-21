# Week 21 Theory Summary

## 1. What is semantic similarity?
Semantic similarity measures how closely two pieces of text express related meaning rather than merely sharing exact words. In this project, sentence embeddings are used to convert text into dense vectors so that similar ideas can be compared even when the wording differs.

## 2. Why compare TF-IDF with embeddings?
TF-IDF is a classical lexical method that works well when the same terms appear in the documents. Embedding-based methods capture broader semantic relationships and often perform better for paraphrases or conceptually related text. The comparison in this project highlights the difference between literal overlap and semantic meaning.

## 3. Why is prompt filtering important?
Prompt filtering improves safety and robustness by rejecting inputs that could trigger unsafe or unintended behavior. It also prevents overly long or manipulative inputs from degrading the results.

## 4. What is the value of the gradient descent demo?
The gradient descent demo illustrates how a simple prediction model can reduce error over repeated updates. Even though it is educational rather than a production model, it shows the core optimization principle behind many machine learning systems.

## 5. What are the limitations of embeddings?
Embeddings can fail on ambiguous words, short queries, or out-of-domain text. These limitations are important because semantic systems may produce plausible but incorrect results when context is insufficient.
