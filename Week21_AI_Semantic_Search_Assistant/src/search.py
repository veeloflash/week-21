import hashlib
import re

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

from src.data import DATASET, DOCUMENTS

TFIDF = TfidfVectorizer()
TFIDF_MATRIX = TFIDF.fit_transform(DOCUMENTS)
EMBEDDING_DIMENSION = 128

def encode_text(text):
    vector = np.zeros(EMBEDDING_DIMENSION, dtype=float)
    for token in re.findall(r"[a-z0-9]+", text.lower()):
        digest = hashlib.sha256(token.encode("utf-8")).digest()
        index = int.from_bytes(digest[:4], "big") % EMBEDDING_DIMENSION
        vector[index] += 1.0
    return vector

EMBEDDINGS = np.vstack([encode_text(text) for text in DOCUMENTS])

def cosine_similarity(first, second):
    """Compute cosine similarity with explicit dot product, norms, and zero handling."""
    dot_product = float(np.dot(first, second))
    first_norm = float(np.sqrt(np.dot(first, first)))
    second_norm = float(np.sqrt(np.dot(second, second)))
    denominator = first_norm * second_norm
    return 0.0 if denominator == 0 else dot_product / denominator

def euclidean_distance(first, second):
    return float(np.sqrt(np.sum((first - second) ** 2)))

def _results(scores, reverse=True, k=5):
    order = sorted(range(len(DATASET)), key=lambda index: scores[index], reverse=reverse)
    return [(DATASET[index]["text"], float(scores[index])) for index in order[:k]]

def tfidf_search(query, k=5):
    scores = (TFIDF_MATRIX * TFIDF.transform([query]).T).toarray().ravel()
    return _results(scores, k=k)

def cosine_search(query, k=5):
    query_vector = encode_text(query)
    scores = [cosine_similarity(query_vector, vector) for vector in EMBEDDINGS]
    return _results(scores, k=k)

def euclidean_search(query, k=5):
    query_vector = encode_text(query)
    distances = [euclidean_distance(query_vector, vector) for vector in EMBEDDINGS]
    return _results(distances, reverse=False, k=k)

def compare_rankings(query, k=5):
    return {"tfidf": tfidf_search(query, k), "cosine": cosine_search(query, k), "euclidean": euclidean_search(query, k)}