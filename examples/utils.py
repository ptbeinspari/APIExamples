import json
import os
from typing import Any

DATA_DIR = "data"


def save_json(data: Any, folder: str, filename: str) -> None:
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(f'{DATA_DIR}/{folder}', exist_ok=True)
    path = os.path.join(f'{DATA_DIR}/{folder}', filename)
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)