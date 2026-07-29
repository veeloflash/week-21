import numpy as np
from Week21_Engineering.shared.shared import encode_texts

def cosine_similarity(a, b):
    if isinstance(a, str):
        a = encode_texts(a)[0]
    if isinstance(b, str):
        b = encode_texts(b)[0]
    denom = np.linalg.norm(a) * np.linalg.norm(b)
    return 0.0 if denom == 0 else float(np.dot(a, b) / denom)

def euclidean_distance(a, b):
    if isinstance(a, str):
        a = encode_texts(a)[0]
    if isinstance(b, str):
        b = encode_texts(b)[0]
    return float(np.linalg.norm(a - b))
