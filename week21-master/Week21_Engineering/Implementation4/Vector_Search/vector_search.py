import numpy as np

from Week21_Engineering.shared.shared import encode_texts, load_documents


docs = load_documents()
doc_vecs = encode_texts(docs)


def _encode_query(query):
    return encode_texts(query)[0]


def vector_search(query, k=5):
    if not query or not str(query).strip():
        return []
    qv = _encode_query(query)
    scores = []
    for dv in doc_vecs:
        denom = np.linalg.norm(qv) * np.linalg.norm(dv)
        score = 0.0 if denom == 0 else float(np.dot(qv, dv) / denom)
        scores.append(score)
    idx = np.argsort(scores)[::-1][:k]
    return [(docs[i], float(scores[i])) for i in idx]


def euclidean_search(query, k=5):
    if not query or not str(query).strip():
        return []
    qv = _encode_query(query)
    scores = []
    for dv in doc_vecs:
        score = float(np.linalg.norm(qv - dv))
        scores.append(score)
    idx = np.argsort(scores)[:k]
    return [(docs[i], float(scores[i])) for i in idx]


def top_k(query, k=5):
    return vector_search(query, k=k)
