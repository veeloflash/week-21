import os, json
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def load_documents_from_json(path="dataset.json"):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    docs = [item["text"] for item in data]
    print("Loaded documents:", len(docs))
    assert len(docs) >= 50
    return docs

def encode_texts(texts):
    if isinstance(texts, str):
        texts = [texts]
    return model.encode(texts, convert_to_numpy=True)

documents = load_documents_from_json("dataset.json")
document_vectors = encode_texts(documents)
