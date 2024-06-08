# File: C:\Users\WEISSIVA\OneDrive\Documentos\Personal\porfolio website\Compiladores\MergedPythonCode.py


# File: C:\Users\WEISSIVA\OneDrive\Documentos\Personal\porfolio website\Compiladores\src\config.py
# Placeholder content


# File: C:\Users\WEISSIVA\OneDrive\Documentos\Personal\porfolio website\Compiladores\src\main.py
# Placeholder content


# File: C:\Users\WEISSIVA\OneDrive\Documentos\Personal\porfolio website\Compiladores\src\__init__.py


# File: C:\Users\WEISSIVA\OneDrive\Documentos\Personal\porfolio website\Compiladores\src\analysis\dialogue_act.py
# Placeholder content


# File: C:\Users\WEISSIVA\OneDrive\Documentos\Personal\porfolio website\Compiladores\src\analysis\emotional_tone.py
# Placeholder content


# File: C:\Users\WEISSIVA\OneDrive\Documentos\Personal\porfolio website\Compiladores\src\analysis\scoring.py
# Placeholder content


# File: C:\Users\WEISSIVA\OneDrive\Documentos\Personal\porfolio website\Compiladores\src\analysis\__init__.py
# Placeholder content


# File: C:\Users\WEISSIVA\OneDrive\Documentos\Personal\porfolio website\Compiladores\src\post_processing\manual_adjustments.py
# Placeholder content


# File: C:\Users\WEISSIVA\OneDrive\Documentos\Personal\porfolio website\Compiladores\src\post_processing\update_patterns.py
# Placeholder content


# File: C:\Users\WEISSIVA\OneDrive\Documentos\Personal\porfolio website\Compiladores\src\post_processing\__init__.py
# Placeholder content


# File: C:\Users\WEISSIVA\OneDrive\Documentos\Personal\porfolio website\Compiladores\src\preprocessing\correct_spelling.py
# Placeholder content
from textblob import TextBlob
import nltk

# Download necessary TextBlob corpora
nltk.download('punkt')

def correct_spelling(text):
    """
    Corrects spelling errors in the provided text.

    :param text: The text to correct.
    :return: Text with corrected spelling.
    """
    blob = TextBlob(text)
    corrected_text = str(blob.correct())
    return corrected_text

def correct_spelling_in_dialogue(dialogue):
    """
    Corrects spelling errors in the provided dialogue.

    :param dialogue: List of dialogues to process.
    :return: List of dialogues with corrected spelling.
    """
    for entry in dialogue:
        entry['customer_text'] = correct_spelling(entry['customer_text'])
        entry['employee_text'] = correct_spelling(entry['employee_text'])
    return dialogue

if __name__ == "__main__":
    sample_text = "Hola, buenos dias. Esto es un ejemplo de texto con errores de ortografia."
    print("Original text:", sample_text)
    print("Text with corrected spelling:", correct_spelling(sample_text))


# File: C:\Users\WEISSIVA\OneDrive\Documentos\Personal\porfolio website\Compiladores\src\preprocessing\read_files.py
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


# File: C:\Users\WEISSIVA\OneDrive\Documentos\Personal\porfolio website\Compiladores\src\preprocessing\remove_stop_words.py
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download the stop words from NLTK
nltk.download('stopwords')
nltk.download('punkt')

def remove_stop_words(text, language='spanish'):
    """
    Removes stop words from the provided text.

    :param text: The text from which to remove stop words.
    :param language: The language of the stop words to remove (default is 'spanish').
    :return: Text with stop words removed.
    """
    stop_words = set(stopwords.words(language))
    word_tokens = word_tokenize(text)

    filtered_text = [word for word in word_tokens if word.lower() not in stop_words]
    return ' '.join(filtered_text)

def remove_stop_words_from_dialogue(dialogue, language='spanish'):
    """
    Removes stop words from the provided dialogue.

    :param dialogue: List of dialogues to process.
    :param language: The language of the stop words to remove (default is 'spanish').
    :return: List of dialogues with stop words removed.
    """
    for entry in dialogue:
        entry['customer_text'] = remove_stop_words(entry['customer_text'], language)
        entry['employee_text'] = remove_stop_words(entry['employee_text'], language)
    return dialogue

if __name__ == "__main__":
    sample_text = "Hola, buenos días. Estoy llamando para hacer una consulta sobre mi factura."
    print("Original text:", sample_text)
    print("Text without stop words:", remove_stop_words(sample_text))


# File: C:\Users\WEISSIVA\OneDrive\Documentos\Personal\porfolio website\Compiladores\src\preprocessing\__init__.py
# This file makes the 'preprocessing' directory a Python package.
# It can be used to import functions from the module files easily.

from .read_files import read_json_file, read_dialogues, display_data_nicely
from .remove_stop_words import remove_stop_words, remove_stop_words_from_dialogue
from .correct_spelling import correct_spelling, correct_spelling_in_dialogue

__all__ = [
    'read_json_file',
    'read_dialogues',
    'remove_stop_words',
    'remove_stop_words_from_dialogue',
    'correct_spelling',
    'correct_spelling_in_dialogue'
]


# File: C:\Users\WEISSIVA\OneDrive\Documentos\Personal\porfolio website\Compiladores\src\tokenization\define_tokens.py
# Placeholder content


# File: C:\Users\WEISSIVA\OneDrive\Documentos\Personal\porfolio website\Compiladores\src\tokenization\lexical_analysis.py
# Placeholder content


# File: C:\Users\WEISSIVA\OneDrive\Documentos\Personal\porfolio website\Compiladores\src\tokenization\tokenizer.py
import nltk
from nltk.tokenize import word_tokenize

# Download necessary NLTK tokenizer resources
nltk.download('punkt')

def tokenize_text(text):
    """
    Tokenizes the provided text into words.

    :param text: The text to tokenize.
    :return: List of tokens.
    """
    tokens = word_tokenize(text)
    return tokens

def tokenize_dialogue(dialogue):
    """
    Tokenizes the text in the provided dialogue.

    :param dialogue: List of dialogues to process.
    :return: List of dialogues with tokenized text.
    """
    for entry in dialogue:
        entry['customer_tokens'] = tokenize_text(entry['customer_text'])
        entry['employee_tokens'] = tokenize_text(entry['employee_text'])
    return dialogue

if __name__ == "__main__":
    sample_text = "Hola, buenos días. Esto es un ejemplo de tokenización de texto."
    print("Original text:", sample_text)
    print("Tokenized text:", tokenize_text(sample_text))


# File: C:\Users\WEISSIVA\OneDrive\Documentos\Personal\porfolio website\Compiladores\src\tokenization\__init__.py
# Placeholder content


# File: C:\Users\WEISSIVA\OneDrive\Documentos\Personal\porfolio website\Compiladores\src\utils\co_reference_resolution.py
# Placeholder content


# File: C:\Users\WEISSIVA\OneDrive\Documentos\Personal\porfolio website\Compiladores\src\utils\error_handling.py
# Placeholder content


# File: C:\Users\WEISSIVA\OneDrive\Documentos\Personal\porfolio website\Compiladores\src\utils\fallback.py
# Placeholder content


# File: C:\Users\WEISSIVA\OneDrive\Documentos\Personal\porfolio website\Compiladores\src\utils\__init__.py
# Placeholder content


# File: C:\Users\WEISSIVA\OneDrive\Documentos\Personal\porfolio website\Compiladores\src\visualization\generate_charts.py
# Placeholder content


# File: C:\Users\WEISSIVA\OneDrive\Documentos\Personal\porfolio website\Compiladores\src\visualization\generate_graphs.py
# Placeholder content


# File: C:\Users\WEISSIVA\OneDrive\Documentos\Personal\porfolio website\Compiladores\src\visualization\generate_heatmaps.py
# Placeholder content


# File: C:\Users\WEISSIVA\OneDrive\Documentos\Personal\porfolio website\Compiladores\src\visualization\__init__.py
# Placeholder content


# File: C:\Users\WEISSIVA\OneDrive\Documentos\Personal\porfolio website\Compiladores\tests\test_correct_spelling.py
import unittest

class Testtest_correct_spelling(unittest.TestCase):
    def test_example(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()


# File: C:\Users\WEISSIVA\OneDrive\Documentos\Personal\porfolio website\Compiladores\tests\test_define_tokens.py
import unittest

class Testtest_define_tokens(unittest.TestCase):
    def test_example(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()


# File: C:\Users\WEISSIVA\OneDrive\Documentos\Personal\porfolio website\Compiladores\tests\test_dialogue_act.py
import unittest

class Testtest_dialogue_act(unittest.TestCase):
    def test_example(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()


# File: C:\Users\WEISSIVA\OneDrive\Documentos\Personal\porfolio website\Compiladores\tests\test_emotional_tone.py
import unittest

class Testtest_emotional_tone(unittest.TestCase):
    def test_example(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()


# File: C:\Users\WEISSIVA\OneDrive\Documentos\Personal\porfolio website\Compiladores\tests\test_lexical_analysis.py
import unittest

class Testtest_lexical_analysis(unittest.TestCase):
    def test_example(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()


# File: C:\Users\WEISSIVA\OneDrive\Documentos\Personal\porfolio website\Compiladores\tests\test_read_files.py
import os
import json
from io import StringIO
from contextlib import redirect_stdout
import pytest
from src.preprocessing.read_files import read_json_file, read_dialogues, display_data_nicely

@pytest.fixture(scope='module')
def setup_files():
    customer_file_path = 'data/customer_dialogues.json'
    employee_file_path = 'data/employee_dialogues.json'
    customer_data = [
        {
            "call_id": "1",
            "customer_id": "cust_001",
            "customer_text": "Hola, buenos días."
        }
    ]
    employee_data = [
        {
            "call_id": "1",
            "employee_id": "emp_001",
            "employee_text": "Buenos días, ¿cómo puedo ayudarle?"
        }
    ]
    os.makedirs('data', exist_ok=True)
    with open(customer_file_path, 'w', encoding='utf-8') as f:
        json.dump(customer_data, f)
    with open(employee_file_path, 'w', encoding='utf-8') as f:
        json.dump(employee_data, f)
    
    yield customer_file_path, employee_file_path, customer_data, employee_data
    
    os.remove(customer_file_path)
    os.remove(employee_file_path)

def test_read_json_file(setup_files):
    customer_file_path, _, customer_data, _ = setup_files
    data = read_json_file(customer_file_path)
    assert isinstance(data, list)
    assert data == customer_data

def test_read_json_file_nonexistent():
    with pytest.raises(FileNotFoundError):
        read_json_file('data/nonexistent.json')

def test_read_json_file_invalid():
    invalid_file_path = 'data/invalid.json'
    with open(invalid_file_path, 'w', encoding='utf-8') as f:
        f.write("Invalid JSON")
    try:
        with pytest.raises(ValueError):
            read_json_file(invalid_file_path)
    finally:
        os.remove(invalid_file_path)

def test_read_dialogues_customer(setup_files):
    _, _, customer_data, _ = setup_files
    data = read_dialogues(file_name='customer_dialogues.json')
    assert isinstance(data, list)
    assert data == customer_data

def test_read_dialogues_employee(setup_files):
    _, _, _, employee_data = setup_files
    data = read_dialogues(file_name='employee_dialogues.json')
    assert isinstance(data, list)
    assert data == employee_data

def test_display_data_nicely(setup_files):
    _, _, customer_data, _ = setup_files
    f = StringIO()
    with redirect_stdout(f):
        display_data_nicely(customer_data, "Customer Dialogues")
    output = f.getvalue()
    assert "Customer Dialogues" in output
    assert "Entry 1" in output
    assert "Hola, buenos días." in output


# File: C:\Users\WEISSIVA\OneDrive\Documentos\Personal\porfolio website\Compiladores\tests\test_remove_stop_words.py
import unittest

class Testtest_remove_stop_words(unittest.TestCase):
    def test_example(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()


# File: C:\Users\WEISSIVA\OneDrive\Documentos\Personal\porfolio website\Compiladores\tests\test_scoring.py
import unittest

class Testtest_scoring(unittest.TestCase):
    def test_example(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()


# File: C:\Users\WEISSIVA\OneDrive\Documentos\Personal\porfolio website\Compiladores\tests\test_tokenizer.py
import unittest

class Testtest_tokenizer(unittest.TestCase):
    def test_example(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()


