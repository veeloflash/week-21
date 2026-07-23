import re
import math
from typing import List, Dict


class SimpleEmbedding:
    def __init__(self, documents: List[str]):
        self.documents = documents
        self.vocab = self._build_vocab(documents)

    def _build_vocab(self, documents: List[str]) -> Dict[str, int]:
        vocab = {}
        for doc in documents:
            for token in self._tokenize(doc):
                if token not in vocab:
                    vocab[token] = len(vocab)
        return vocab

    def _tokenize(self, text: str) -> List[str]:
        return re.findall(r"[a-zA-Z]{2,}", text.lower())

    def embed(self, text: str) -> List[float]:
        tokens = self._tokenize(text)
        vector = [0.0] * len(self.vocab)
        for token in tokens:
            if token in self.vocab:
                vector[self.vocab[token]] += 1.0
        return vector

    def embed_documents(self) -> List[List[float]]:
        return [self.embed(doc) for doc in self.documents]
