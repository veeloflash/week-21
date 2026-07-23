import numpy as np

from src.shared import encode_texts, load_documents

texts = load_documents()
emb = encode_texts(texts)


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
