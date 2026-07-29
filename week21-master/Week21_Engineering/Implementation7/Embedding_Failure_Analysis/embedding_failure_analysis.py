from Week21_Engineering.Implementation5.Embedding_Search.embedding_search import search2
from Week21_Engineering.Implementation4.Vector_Search.vector_search import top_k, euclidean_search
from Week21_Engineering.Implementation2.TFIDF_Retrieval.tfidf_search import search as tfidf_search

def find_failure_cases(query, expected_ids=None):
    if expected_ids is None:
        expected_ids = []

    emb = search2(query, 5)
    cos = top_k(query, 5)
    euc = euclidean_search(query, 5)
    tfidf = tfidf_search(query, 5)

    emb_ids = [r[0] for r in emb]
    cos_ids = [r[0] for r in cos]
    euc_ids = [r[0] for r in euc]
    tfidf_ids = [r[0] for r in tfidf]

    failures = []

    for eid in expected_ids:
        if eid not in emb_ids:
            failures.append({
                "summary": f"Expected document '{eid}' did not appear in the top‑5 results.",
                "query": query,
                "expected_document": eid,
                "analysis": {
                    "embedding_rank": emb_ids.index(eid) if eid in emb_ids else "not in top‑5",
                    "cosine_rank": cos_ids.index(eid) if eid in cos_ids else "not in top‑5",
                    "euclidean_rank": euc_ids.index(eid) if eid in euc_ids else "not in top‑5",
                    "tfidf_rank": tfidf_ids.index(eid) if eid in tfidf_ids else "not in top‑5"
                },
                "likely_reason": "The embedding model considers other documents more semantically similar.",
                "recommendation": "Improve dataset quality, add more relevant samples, or fine‑tune embeddings."
            })

    return failures
