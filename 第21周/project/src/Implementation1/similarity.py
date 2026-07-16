import numpy as np

try:
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("all-MiniLM-L6-v2")
except Exception:
    model = None


def _encode_texts(texts):
    if isinstance(texts, str):
        texts = [texts]

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


def cosine_similarity(text1, text2):
    v1 = _encode_texts(text1)[0]
    v2 = _encode_texts(text2)[0]
    denominator = np.linalg.norm(v1) * np.linalg.norm(v2)
    if denominator == 0:
        return 0.0
    return float(np.dot(v1, v2) / denominator)
