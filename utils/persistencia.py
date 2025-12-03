"""
Simple persistence helpers for json files
"""
import json
from typing import Any
from pathlib import Path

def leer_json(path: str):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def escribir_json(path: str, obj: Any):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)

def file_exists(filename: str) -> bool:
    return Path(filename).is_file()

def get_filename_from_path(path: str) -> str:
    filename:str = Path(path).name
    return filename
