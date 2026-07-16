import numpy as np
import os

try:
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("all-MiniLM-L6-v2")
except Exception:
    model = None

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_PATH = os.path.join(BASE_DIR, "dataset.txt")
docs = open(DATA_PATH, encoding="utf-8").read().splitlines()


def _encode_documents():
    if model is not None:
        return model.encode(docs, convert_to_numpy=True)

    vectors = []
    for text in docs:
        tokens = [token.lower() for token in text.replace("-", " ").split()]
        vector = np.zeros(32)
        for token in tokens:
            vector[abs(hash(token)) % 32] += 1.0
        norm = np.linalg.norm(vector)
        if norm > 0:
            vector = vector / norm
        vectors.append(vector)
    return np.vstack(vectors)


def _encode_query(query):
    if model is not None:
        return model.encode([query], convert_to_numpy=True)[0]

    tokens = [token.lower() for token in query.replace("-", " ").split()]
    vector = np.zeros(32)
    for token in tokens:
        vector[abs(hash(token)) % 32] += 1.0
    norm = np.linalg.norm(vector)
    if norm > 0:
        vector = vector / norm
    return vector


doc_vecs = _encode_documents()


def embedding_search(query, k=5):
    qv = _encode_query(query)
    scores = [float(np.dot(qv, dv) / (np.linalg.norm(qv) * np.linalg.norm(dv))) for dv in doc_vecs]
    idx = np.argsort(scores)[::-1][:k]
    return [(docs[i], scores[i]) for i in idx]


def search2(query, k=5):
    return embedding_search(query, k=k)
