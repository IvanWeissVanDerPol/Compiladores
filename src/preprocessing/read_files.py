import json
import os
import logging
from typing import List, Dict

class FileReadError(Exception):
    """Custom exception for errors during file reading."""
    pass

def read_json_file(file_path: str) -> List[Dict[str, List[str]]]:
    """
    Reads a JSON file and returns its contents.

    :param file_path: Path to the JSON file.
    :return: Parsed contents of the JSON file.
    :raises FileNotFoundError: If the file does not exist.
    :raises ValueError: If the file contains invalid JSON.
    """
    if not os.path.exists(file_path):
        logging.error(f"File not found: {file_path}")
        raise FileNotFoundError(f"Error: The file {file_path} does not exist.")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        logging.info(f"Success: Loaded data from {file_path}")
        return data
    except json.JSONDecodeError as e:
        logging.error(f"Error parsing JSON file {file_path}: {e}")
        raise ValueError(f"Error: Failed to parse JSON file {file_path}. Error: {e}")

def read_dialogue_file(file_path: str) -> List[Dict[str, List[str]]]:
    """
    Reads a dialogue JSON file and returns its contents.

    :param file_path: Path to the JSON file.
    :return: Parsed contents of the JSON file.
    """
    return read_json_file(file_path)

def read_dialogues(data_dir: str = 'data', file_name: str = 'customer_dialogues.json') -> List[Dict[str, List[str]]]:
    """
    Reads and parses a JSON file containing dialogues.

    :param data_dir: Directory where the JSON file is located.
    :param file_name: Name of the JSON file.
    :return: Parsed contents of the JSON file.
    """
    file_path = os.path.join(data_dir, file_name)
    return read_json_file(file_path)

def display_data_nicely(data: List[Dict[str, List[str]]], title: str = "Data") -> None:
    """
    Displays JSON data in a readable format.

    :param data: Data to be displayed.
    :param title: Title for the data being displayed.
    """
    print(f"\n{title}:\n{'=' * len(title)}")
    for index, item in enumerate(data, start=1):
        print(f"\nEntry {index}:")
        print(f"{'-' * 8}")
        for key, value in item.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    files_to_read = [
        ("customer_dialogues.json", "Customer Dialogues"),
        ("employee_dialogues.json", "Employee Dialogues")
    ]

    for file_name, title in files_to_read:
        try:
            data = read_dialogues(file_name=file_name)
            display_data_nicely(data, title)
        except Exception as e:
            logging.error(f"Error reading {file_name}: {e}")
