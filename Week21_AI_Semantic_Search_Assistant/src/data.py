import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATASET_PATH = ROOT / "data" / "dataset.json"

def load_dataset():
    with DATASET_PATH.open(encoding="utf-8") as handle:
        records = json.load(handle)
    if len(records) < 50:
        raise ValueError("The product dataset must contain at least 50 records.")
    return records

DATASET = load_dataset()
DOCUMENTS = [record["text"] for record in DATASET]
DOCUMENT_IDS = [record["id"] for record in DATASET]