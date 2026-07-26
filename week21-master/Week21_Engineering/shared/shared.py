import os
import numpy as np

from sentence_transformers import SentenceTransformer

def load_documents(path="dataset.txt"):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        docs = [line.strip() for line in f.readlines() if line.strip()]
    return docs

_embedding_model = None

def get_embedding_model():
    global _embedding_model
    if _embedding_model is None:
        _embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    return _embedding_model


def encode_texts(texts):
    model = get_embedding_model()
    if isinstance(texts, str):
        texts = [texts]
    return model.encode(texts, convert_to_numpy=True)


def cosine_similarity(a, b):
    if isinstance(a, str):
        a = encode_texts(a)[0]
    if isinstance(b, str):
        b = encode_texts(b)[0]

    denom = np.linalg.norm(a) * np.linalg.norm(b)
    if denom == 0:
        return 0.0
    return float(np.dot(a, b) / denom)