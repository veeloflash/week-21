import numpy as np
from Week21_Engineering.shared.shared import documents, document_vectors, encode_texts

def search2(query, k=5):
    qv = encode_texts(query)[0]
    sims = np.dot(document_vectors, qv)
    idx = np.argsort(sims)[::-1][:k]
    return [(documents[i], float(sims[i])) for i in idx]
