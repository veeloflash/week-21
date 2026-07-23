import math
import re
from collections import Counter
from typing import List, Dict, Tuple


class TFIDFEngine:
    def __init__(self, documents: List[str]):
        self.documents = documents
        self.tokenized_docs = [self._tokenize(doc) for doc in documents]
        self.idf = self._compute_idf(self.tokenized_docs)

    def _tokenize(self, text: str) -> List[str]:
        return re.findall(r"[a-zA-Z]{2,}", text.lower())

    def _compute_idf(self, tokenized_docs: List[List[str]]) -> Dict[str, float]:
        doc_count = len(tokenized_docs)
        df = Counter(token for doc in tokenized_docs for token in set(doc))
        return {token: math.log((1 + doc_count) / (1 + count)) + 1.0 for token, count in df.items()}

    def vectorize(self, text: str) -> Dict[str, float]:
        tokens = self._tokenize(text)
        counts = Counter(tokens)
        vector = {}
        for token, count in counts.items():
            if token in self.idf:
                vector[token] = count * self.idf[token]
        return vector

    def score(self, query: str, document: str) -> float:
        q_vec = self.vectorize(query)
        d_vec = self.vectorize(document)
        common_terms = set(q_vec) & set(d_vec)
        if not common_terms:
            return 0.0
        numerator = sum(q_vec[t] * d_vec[t] for t in common_terms)
        q_norm = math.sqrt(sum(v * v for v in q_vec.values()))
        d_norm = math.sqrt(sum(v * v for v in d_vec.values()))
        if q_norm == 0 or d_norm == 0:
            return 0.0
        return numerator / (q_norm * d_norm)
