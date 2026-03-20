import os, json
from config import CACHE_PATH

os.makedirs(CACHE_PATH, exist_ok=True)

def save_cache(key: str, value: dict):
    with open(os.path.join(CACHE_PATH, f"{key}.json"), "w") as f:
        json.dump(value, f)

def load_cache(key: str):
    path = os.path.join(CACHE_PATH, f"{key}.json")
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return None