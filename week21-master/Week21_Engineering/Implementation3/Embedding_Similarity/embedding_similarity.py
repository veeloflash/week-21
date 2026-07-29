import numpy as np
from Week21_Engineering.shared.shared import documents, document_vectors

def cosine():
    n = len(documents)
    m = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            a = document_vectors[i]
            b = document_vectors[j]
            denom = np.linalg.norm(a) * np.linalg.norm(b)
            m[i][j] = 0.0 if denom == 0 else float(np.dot(a, b) / denom)
    return m
