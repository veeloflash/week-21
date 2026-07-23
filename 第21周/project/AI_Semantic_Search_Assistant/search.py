import os
from typing import List, Dict, Any
from project.AI_Semantic_Search_Assistant.embedding import SimpleEmbedding
from project.AI_Semantic_Search_Assistant.similarity import cosine_similarity, euclidean_distance
from project.AI_Semantic_Search_Assistant.tfidf import TFIDFEngine


class SearchEngine:
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.documents = self._load_documents()
        self.embedding_model = SimpleEmbedding(self.documents)
        self.embedding_vectors = self.embedding_model.embed_documents()
        self.tfidf_engine = TFIDFEngine(self.documents)

    def _load_documents(self) -> List[str]:
        with open(self.data_path, "r", encoding="utf-8") as fh:
            return [line.strip() for line in fh if line.strip()]

    def _embed_query(self, query: str) -> List[float]:
        return self.embedding_model.embed(query)

    def search(self, query: str, top_k: int = 5) -> Dict[str, List[Dict[str, Any]]]:
        query_embedding = self._embed_query(query)
        tfidf_results = []
        embedding_results = []

        for idx, doc in enumerate(self.documents):
            tfidf_score = self.tfidf_engine.score(query, doc)
            cosine_score = cosine_similarity(query_embedding, self.embedding_vectors[idx])
            euclidean_score = euclidean_distance(query_embedding, self.embedding_vectors[idx])
            tfidf_results.append({"index": idx, "text": doc, "score": tfidf_score})
            embedding_results.append({"index": idx, "text": doc, "score": cosine_score, "euclidean": euclidean_score})

        tfidf_results.sort(key=lambda item: item["score"], reverse=True)
        embedding_results.sort(key=lambda item: item["score"], reverse=True)
        return {
            "tfidf": tfidf_results[:top_k],
            "embedding": embedding_results[:top_k],
        }
