import json
import os
import pprint

def read_json_file(file_path):
    """
    Reads a JSON file and returns its contents.

    :param file_path: Path to the JSON file.
    :return: Parsed contents of the JSON file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Error: The file {file_path} does not exist.")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        print(f"Success: Loaded data from {file_path}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Error: Failed to parse JSON file {file_path}. Error: {e}")
    
    return data

def read_dialogues(data_dir='data', file_name='customer_dialogues.json'):
    """
    Reads and parses a JSON file containing dialogues.

    :param data_dir: Directory where the JSON file is located.
    :param file_name: Name of the JSON file.
    :return: Parsed contents of the JSON file.
    """
    file_path = os.path.join(data_dir, file_name)
    return read_json_file(file_path)

def display_data_nicely(data, title="Data"):
    """
    Displays JSON data in a readable format.

    :param data: Data to be displayed.
    :param title: Title for the data being displayed.
    """
    print(f"\n{title}:\n{'=' * len(title)}")
    if isinstance(data, list):
        for index, item in enumerate(data, start=1):
            print(f"\nEntry {index}:")
            print(f"{'-' * 8}")
            pp = pprint.PrettyPrinter(indent=4)
            pp.pprint(item)
    else:
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(data)

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
            print(f"Error reading {file_name}: {e}")
