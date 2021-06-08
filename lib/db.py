import json
from pathlib import Path


def load_db():
    return json.loads(DB.read_text(encoding="utf8"))


def save_db(db):
    DB.write_text(json.dumps(db), encoding="utf8")


DB = Path(".katalog.json")
if not DB.exists():
    save_db({})
