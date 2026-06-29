import json
import os
from datetime import datetime

HISTORY_FILE = "project_history.json"


def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []


def save_to_history(project, scores):
    history = load_history()
    entry = {
        "id": len(history) + 1,
        "title": project.get("title", "Untitled"),
        "domain": project.get("domain", ""),
        "description": project.get("description", ""),
        "scores": scores,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    history.append(entry)
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)


def clear_history():
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)