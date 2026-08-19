import numpy as np
from Week21_Engineering.shared.shared import documents, document_vectors, encode_texts
from Week21_Engineering.Implementation1.Similarity_Engine.similarity import cosine_similarity, euclidean_distance

def top_k(query, k=5):
    qv = encode_texts(query)[0]
    scores = []
    for i, dv in enumerate(document_vectors):
        s = cosine_similarity(qv, dv)
        scores.append((documents[i], float(s)))
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:k]

def euclidean_search(query, k=5):
    qv = encode_texts(query)[0]
    scores = []
    for i, dv in enumerate(document_vectors):
        d = euclidean_distance(qv, dv)
        scores.append((documents[i], float(d)))
    scores.sort(key=lambda x: x[1])
    return scores[:k]
