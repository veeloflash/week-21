def retrieval_metrics(results, expected_ids, id_by_text, k=5):
    retrieved = [id_by_text[text] for text, _ in results[:k]]
    expected = set(expected_ids)
    hits = sum(item in expected for item in retrieved)
    reciprocal_rank = next((1 / (index + 1) for index, item in enumerate(retrieved) if item in expected), 0.0)
    return {"hit_at_5": int(hits > 0), "precision_at_5": hits / k, "recall_at_5": hits / len(expected) if expected else 0.0, "mrr": reciprocal_rank}