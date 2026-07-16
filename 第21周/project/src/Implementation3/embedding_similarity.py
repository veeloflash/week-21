import numpy as np
import os

try:
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("all-MiniLM-L6-v2")
except Exception:
    model = None

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_PATH = os.path.join(BASE_DIR, "dataset.txt")
texts = open(DATA_PATH, encoding="utf-8").read().splitlines()


def _encode_documents():
    if model is not None:
        return model.encode(texts, convert_to_numpy=True)

    vectors = []
    for text in texts:
        tokens = [token.lower() for token in text.replace("-", " ").split()]
        vector = np.zeros(32)
        for token in tokens:
            vector[abs(hash(token)) % 32] += 1.0
        norm = np.linalg.norm(vector)
        if norm > 0:
            vector = vector / norm
        vectors.append(vector)
    return np.vstack(vectors)


emb = _encode_documents()


def embedding_similarity_matrix():
    matrix = []
    for i in range(len(texts)):
        row = []
        for j in range(len(texts)):
            denom = np.linalg.norm(emb[i]) * np.linalg.norm(emb[j])
            sim = 0.0 if denom == 0 else float(np.dot(emb[i], emb[j]) / denom)
            row.append(sim)
        matrix.append(row)
    return matrix


def cosine():
    return embedding_similarity_matrix()
