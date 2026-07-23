import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

from src.shared import load_documents


docs = load_documents()
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(docs)


def search(query, top_k=5):
    if not query or not str(query).strip():
        return []
    q = vectorizer.transform([query])
    scores = (X * q.T).toarray().flatten()
    idx = np.argsort(scores)[::-1][:top_k]
    return [(docs[i], float(scores[i])) for i in idx]


def tfidf_search(query, top_k=5):
    return search(query, top_k=top_k)
