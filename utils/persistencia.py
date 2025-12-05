
import json
from typing import Any
from pathlib import Path

def leer_json(path: str):
    """
    Reads a JSON file from the given path and returns its content.

    If the file does not exist, an empty list is returned. This function
    ensures safe loading of JSON data and prevents program crashes due to 
    missing files.

    Args:
        path (str): Path to the JSON file.

    Returns:
        Any: The parsed JSON content, or an empty list if the file is not found.
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def escribir_json(path: str, obj: Any):
    """
    Writes a Python object to a JSON file at the specified path.

    The JSON is written using UTF-8 encoding, with indentation for readability.
    This function is commonly used to persist updated data structures.

    Args:
        path (str): Path where the JSON file will be saved.
        obj (Any): Python object to serialize into JSON format.
    """
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)





def file_exists(filename: str) -> bool:
    """
    Checks whether a file exists at the given path.

    Args:
        filename (str): The file path to verify.

    Returns:
        bool: True if the file exists, False otherwise."""
    return Path(filename).is_file()

def get_filename_from_path(path: str) -> str:
    """
    Extracts and returns the file name from a full file path.

    This is useful for logging, display purposes, or processing file names 
    independently from their directory structure.

    Args:
        path (str): Full path of the file.

    Returns:
        str: The file name extracted from the path.
    """
    filename:str = Path(path).name
    return filename
