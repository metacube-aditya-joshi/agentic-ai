import json
from pathlib import Path
from .FileModes import FILE_MODES


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def open_json(filename, action, data=None):
    if action not in FILE_MODES:
        raise ValueError("Invalid action. Choose: read, write, append")

    file_path = DATA_DIR / filename

    # Ensure data directory exists
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # ---------------- READ ----------------
    if action == "read":
        if not file_path.exists() or file_path.stat().st_size == 0:
            return []

        with open(file_path, FILE_MODES["read"], encoding="utf-8") as f:
            return json.load(f)

    # ---------------- WRITE ----------------
    if action == "write":
        with open(file_path, FILE_MODES["write"], encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        return

    # ---------------- APPEND ----------------
    existing = []

    if file_path.exists() and file_path.stat().st_size > 0:
        with open(file_path, FILE_MODES["read"], encoding="utf-8") as f:
            existing = json.load(f)

    if not isinstance(existing, list):
        raise ValueError("Append requires JSON array")

    existing.append(data)

    with open(file_path, FILE_MODES["write"], encoding="utf-8") as f:
        json.dump(existing, f, indent=4)
