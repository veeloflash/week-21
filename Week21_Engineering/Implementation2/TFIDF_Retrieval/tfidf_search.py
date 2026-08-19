import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from Week21_Engineering.shared.shared import documents

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)

def search(query, k=5):
    q = vectorizer.transform([query])
    scores = (X * q.T).toarray().flatten()
    idx = np.argsort(scores)[::-1][:k]
    return [(documents[i], float(scores[i])) for i in idx]
