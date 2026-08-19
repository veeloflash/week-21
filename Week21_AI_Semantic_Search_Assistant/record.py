import os
import json
from datetime import datetime

TIMELINE_PATH = "timeline.json"

def _load_timeline():
    if not os.path.exists(TIMELINE_PATH):
        return []
    try:
        with open(TIMELINE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def _save_timeline(records):
    with open(TIMELINE_PATH, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)

def add_record(question, result=None, status="ok", ifsuccess=True, reason=""):
    records = _load_timeline()
    record = {
        "time": datetime.now().isoformat(),
        "question": question,
        "result": result,
        "status": status,
        "ifsuccess": ifsuccess,
        "reason": reason
    }
    records.append(record)
    _save_timeline(records)
    return record
