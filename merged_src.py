
# File: src/analysis/dialogue_act.py

import spacy
import logging
from typing import List, Dict

# Load a spaCy model for language processing
nlp = spacy.load('es_core_news_sm')

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define a more extensive list of keywords for dialogue acts classification in Spanish
QUESTION_KEYWORDS = [
    'preguntar', 'cuestionar', 'indagar', 'inquirir', 'aclarar', 'consultar', 'dudar', 'qué', 'cómo', 
    'por qué', 'cuándo', 'dónde', 'cuál', 'quién', 'quiénes', 'de quién', 'podría', 'podrías', 
    'podríamos', 'podrían', 'sería', 'serías', 'seríamos', 'serían', 'debería', 'deberías', 'deberíamos', 
    'deberían', 'es', 'son', 'hace', 'hacen', 'puede', 'pueden', 'podría', 'puedes', 'puedo', 'permitiría', 
    'debe', 'deben'
]

THANKS_KEYWORDS = [
    'gracias', 'agradecer', 'agradezco', 'agradecido', 'gratitud', 'agradecida', 'muy agradecido', 
    'muchas gracias', 'mil gracias', 'gracias de verdad', 'te agradezco', 'le agradezco', 'les agradezco', 
    'se lo agradezco'
]

GREETING_KEYWORDS = [
    'saludar', 'hola', 'buenos días', 'buenas tardes', 'buenas noches', 'saludos', 'buen día', 'qué tal', 
    'cómo estás', 'cómo está', 'qué gusto', 'mucho gusto', 'encantado de conocerte', 'encantado de conocerle', 
    'cómo te va', 'cómo le va', 'qué hay', 'hola a todos', 'buenas'
]

FAREWELL_KEYWORDS = [
    'adiós', 'hasta luego', 'nos vemos', 'cuídate', 'cuídese', 'hasta pronto', 'hasta la próxima', 
    'nos vemos pronto', 'nos vemos después', 'chau', 'chao', 'adiós por ahora', 'nos vemos mañana', 
    'despedida', 'que tengas buen día', 'que tenga buen día', 'hasta la próxima vez', 'paz y amor', 
    'nos vemos en otra ocasión', 'me despido'
]

STATEMENT_KEYWORDS = [
    'decir', 'contar', 'informar', 'mencionar', 'comentar', 'explicar', 'describir', 'afirmar', 'asegurar', 
    'declarar', 'anunciar', 'expresar', 'manifestar', 'relatar', 'revelar', 'opinar', 'argumentar', 'responder', 
    'contestar', 'comunicar', 'divulgar', 'compartir', 'transmitir', 'detallar', 'resumir', 'informar', 
    'recalcar', 'enfatizar', 'subrayar', 'exponer', 'pronunciar'
]

def classify_dialogue_act(text: str) -> str:
    """
    Classifies the dialogue act of a given text.

    :param text: The text to classify.
    :return: Dialogue act classification.
    """
    doc = nlp(text)
    if any(token.lemma_ in QUESTION_KEYWORDS for token in doc):
        return 'question'
    elif any(token.lemma_ in THANKS_KEYWORDS for token in doc):
        return 'thanks'
    elif any(token.lemma_ in GREETING_KEYWORDS for token in doc):
        return 'greeting'
    elif any(token.lemma_ in FAREWELL_KEYWORDS for token in doc):
        return 'farewell'
    elif any(token.lemma_ in STATEMENT_KEYWORDS for token in doc):
        return 'statement'
    else:
        return 'unknown'

def identify_dialogue_acts(dialogue: List[Dict[str, List[str]]]) -> List[Dict[str, List[str]]]:
    """
    Identifies dialogue acts in the provided dialogue.

    :param dialogue: List of dialogues to process.
    :return: List of dialogues with identified dialogue acts.
    """
    dialogue_acts = []
    for entry in dialogue:
        try:
            customer_acts = [classify_dialogue_act(text) for text in entry['customer_text']]
            employee_acts = [classify_dialogue_act(text) for text in entry['employee_text']]
            dialogue_acts.append({
                'call_id': entry['call_id'],
                'customer_id': entry['customer_id'],
                'employee_id': entry['employee_id'],
                'customer_acts': customer_acts,
                'employee_acts': employee_acts
            })
        except Exception as e:
            logging.error(f"Error processing dialogue acts for entry {entry['call_id']}: {e}")

    logging.info("Identified dialogue acts for all entries.")
    return dialogue_acts

if __name__ == "__main__":
    sample_dialogue = [
        {"call_id": "1", "customer_id": "cust_001", "employee_id": "emp_001",
         "customer_text": ["Hola, tengo una pregunta sobre mi factura."],
         "employee_text": ["Claro, ¿cómo puedo ayudarte?"]}
    ]

    dialogue_acts = identify_dialogue_acts(sample_dialogue)
    print("Dialogue Acts:", dialogue_acts)

# File: src/analysis/emotional_tone.py

import logging
from textblob import TextBlob
from typing import List, Dict

def get_emotional_tone(text: str) -> str:
    """
    Determines the emotional tone of a given text.

    :param text: Text to analyze.
    :return: Emotional tone (positive, negative, neutral).
    """
    try:
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity

        if polarity > 0:
            return 'positive'
        elif polarity < 0:
            return 'negative'
        else:
            return 'neutral'
    except Exception as e:
        logging.error(f"Error analyzing emotional tone for text '{text}': {e}")
        return 'unknown'

def analyze_emotional_tone(dialogue: List[Dict[str, List[str]]]) -> List[Dict[str, List[str]]]:
    """
    Analyzes the emotional tone of the provided dialogue.

    :param dialogue: List of dialogues to process.
    :return: List of dialogues with analyzed emotional tone.
    """
    emotional_tones = []
    for entry in dialogue:
        try:
            customer_tones = [get_emotional_tone(text) for text in entry['customer_text']]
            employee_tones = [get_emotional_tone(text) for text in entry['employee_text']]
            emotional_tones.append({
                'call_id': entry['call_id'],
                'customer_id': entry['customer_id'],
                'employee_id': entry['employee_id'],
                'customer_tones': customer_tones,
                'employee_tones': employee_tones
            })
        except Exception as e:
            logging.error(f"Error analyzing emotional tones for entry {entry['call_id']}: {e}")

    return emotional_tones

if __name__ == "__main__":
    sample_dialogue = [
        {"call_id": "1", "customer_id": "cust_001", "employee_id": "emp_001",
         "customer_text": ["Estoy muy contento con su servicio."],
         "employee_text": ["Gracias por sus amables palabras."]}
    ]
    
    emotional_tones = analyze_emotional_tone(sample_dialogue)
    print("Emotional Tones:", emotional_tones)

# File: src/analysis/scoring.py

import logging
from typing import List, Dict

def score_text(text: str) -> int:
    """
    Scores the quality of a given text.

    The function evaluates the text based on the presence of positive and negative tokens.
    It counts the occurrences of positive and negative words and calculates a score based
    on their difference. The score is scaled and constrained to be between 0 and 100.

    :param text: The text to score.
    :return: A quality score (0 to 100).
    """
    positive_tokens = [
        "bueno", "excelente", "satisfecho", "contento", "maravilloso", "genial", "feliz", "agradable", "fantástico", 
        "increíble", "estupendo", "espléndido", "positivo", "brillante", "formidable", "satisfactorio", 
        "placentero", "encantador", "perfecto", "magnífico", "sensacional", "sorprendente", 
        "asombroso", "notable", "alucinante", "impresionante", "espectacular", "superior", "favorable", "encantado", 
        "entusiasta", "aliviado", "excepcional", "eficiente", "extraordinario", "positivamente"
    ]

    negative_tokens = [
        "malo", "desastre", "insatisfecho", "enojado", "terrible", "horrible", "descontento", "triste", "decepcionado", 
        "frustrado", "enfadado", "desagradable", "nefasto", "pésimo", "negativo", "desafortunado", "lamentable", 
        "desastroso", "molesto", "irritado", "desesperado", "infeliz", "desilusionado", "agotado", "harto", "cansado", 
        "falso", "deficiente", "desfavorable", "horrendo", "atroz", "desequilibrado", "desalmado", "fallido", 
        "inaceptable", "defraudado", "defectuoso", "incompetente", "ineficiente", "problemático", "doloroso", 
        "insoportable", "intolerable", "indignado", "iracundo", "perjudicial", "fatal", "injusto"
    ]

    try:
        positive_count = sum(1 for word in text.split() if word.lower() in positive_tokens)
        negative_count = sum(1 for word in text.split() if word.lower() in negative_tokens)
        
        score = (positive_count - negative_count) * 10
        return max(0, min(100, score))  # Ensure score is between 0 and 100
    except Exception as e:
        logging.error(f"Error scoring text '{text}': {e}")
        return 0

def score_dialogue_quality(dialogue: List[Dict[str, List[str]]]) -> List[Dict[str, List[int]]]:
    """
    Scores the quality of the provided dialogue.

    :param dialogue: List of dialogues to process.
    :return: List of dialogues with quality scores.
    """
    scored_dialogues = []
    for entry in dialogue:
        try:
            customer_scores = [score_text(text) for text in entry['customer_text']]
            employee_scores = [score_text(text) for text in entry['employee_text']]
            scored_dialogues.append({
                'call_id': entry['call_id'],
                'customer_id': entry['customer_id'],
                'employee_id': entry['employee_id'],
                'customer_scores': customer_scores,
                'employee_scores': employee_scores
            })
        except Exception as e:
            logging.error(f"Error scoring dialogue quality for entry {entry['call_id']}: {e}")

    return scored_dialogues

if __name__ == "__main__":
    sample_dialogue = [
        {"call_id": "1", "customer_id": "cust_001", "employee_id": "emp_001",
         "customer_text": ["¿Puede ayudarme con mi cuenta?"],
         "employee_text": ["¡Por supuesto! ¿En qué necesita ayuda?"]}
    ]
    
    scored_dialogues = score_dialogue_quality(sample_dialogue)
    print("Scored Dialogues:", scored_dialogues)

# File: src/config.py

import os

class Config:
    """
    Configuration class for the project.
    """

    # Directory paths
    DATA_DIR = os.getenv('DATA_DIR', os.path.join(os.getcwd(), 'data'))
    MODELS_DIR = os.getenv('MODELS_DIR', os.path.join(os.getcwd(), 'models'))
    LOGS_DIR = os.getenv('LOGS_DIR', os.path.join(os.getcwd(), 'logs'))

    # Data files
    CUSTOMER_DIALOGUES_FILE = os.path.join(DATA_DIR, 'customer_dialogues.json')
    EMPLOYEE_DIALOGUES_FILE = os.path.join(DATA_DIR, 'employee_dialogues.json')

    # NLP model configurations
    SPACY_MODEL = os.getenv('SPACY_MODEL', 'es_core_news_sm')

    # Logging configurations
    LOG_FILE = os.getenv('LOG_FILE', os.path.join(LOGS_DIR, 'app.log'))
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

    @classmethod
    def create_directories(cls):
        """
        Creates the necessary directories if they don't exist.
        """
        os.makedirs(cls.DATA_DIR, exist_ok=True)
        os.makedirs(cls.MODELS_DIR, exist_ok=True)
        os.makedirs(cls.LOGS_DIR, exist_ok=True)

if __name__ == "__main__":
    Config.create_directories()
    print(f"Data directory: {Config.DATA_DIR}")
    print(f"Models directory: {Config.MODELS_DIR}")
    print(f"Logs directory: {Config.LOGS_DIR}")

# File: src/main.py

import logging
from preprocessing import read_dialogue_file, correct_spelling_in_dialogue, remove_stop_words_from_dialogue
from tokenization import tokenize_text
from analysis import identify_dialogue_acts, analyze_emotional_tone, score_dialogue_quality
from config import Config
from typing import List, Dict, Union

def main() -> None:
    # Create necessary directories
    Config.create_directories()

    # Configure logging
    logging.basicConfig(filename=Config.LOG_FILE, level=Config.LOG_LEVEL, format='%(asctime)s - %(levelname)s - %(message)s')
    
    try:
        # Read dialogues
        customer_dialogues: List[Dict[str, Union[str, List[str]]]] = read_dialogue_file(Config.CUSTOMER_DIALOGUES_FILE)
        employee_dialogues: List[Dict[str, Union[str, List[str]]]] = read_dialogue_file(Config.EMPLOYEE_DIALOGUES_FILE)

        # Correct spelling in dialogues
        corrected_customer_dialogues = correct_spelling_in_dialogue(customer_dialogues)
        corrected_employee_dialogues = correct_spelling_in_dialogue(employee_dialogues)

        # Remove stop words from dialogues
        customer_dialogues_no_stop = remove_stop_words_from_dialogue(corrected_customer_dialogues)
        employee_dialogues_no_stop = remove_stop_words_from_dialogue(corrected_employee_dialogues)

        # Tokenize dialogues
        tokenized_customer_dialogues = tokenize_text(customer_dialogues_no_stop)
        tokenized_employee_dialogues = tokenize_text(employee_dialogues_no_stop)

        # Analyze dialogue acts
        customer_dialogue_acts = identify_dialogue_acts(tokenized_customer_dialogues)
        employee_dialogue_acts = identify_dialogue_acts(tokenized_employee_dialogues)

        # Analyze emotional tone
        customer_emotional_tones = analyze_emotional_tone(customer_dialogue_acts)
        employee_emotional_tones = analyze_emotional_tone(employee_dialogue_acts)

        # Score dialogue quality
        customer_scores = score_dialogue_quality(customer_emotional_tones)
        employee_scores = score_dialogue_quality(employee_emotional_tones)

        # Display results
        logging.info("Customer Dialogues Analysis:")
        for dialogue in customer_scores:
            logging.info(dialogue)

        logging.info("\nEmployee Dialogues Analysis:")
        for dialogue in employee_scores:
            logging.info(dialogue)
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

# File: src/post_processing/manual_adjustments.py

import logging
from typing import List, Dict

def apply_manual_adjustments(dialogue: List[Dict[str, List[str]]]) -> List[Dict[str, List[str]]]:
    """
    Applies manual adjustments to the provided dialogue.

    :param dialogue: List of dialogues to process.
    :return: List of dialogues with manual adjustments applied.
    """
    try:
        for entry in dialogue:
            entry['customer_text'] = [text.replace("Hola", "Hello") for text in entry['customer_text']]
            entry['employee_text'] = [text.replace("Buenos días", "Good morning") for text in entry['employee_text']]
    except Exception as e:
        logging.error(f"Error applying manual adjustments: {e}")

    return dialogue

if __name__ == "__main__":
    sample_dialogue = [
        {"call_id": "1", "customer_id": "cust_001", "employee_id": "emp_001",
         "customer_text": ["Hola, tengo una consulta."],
         "employee_text": ["Buenos días, ¿en qué puedo ayudarle?"]}
    ]
    
    adjusted_dialogue = apply_manual_adjustments(sample_dialogue)
    print("Original Dialogue:", sample_dialogue)
    print("Adjusted Dialogue:", adjusted_dialogue)

# File: src/post_processing/update_patterns.py

import logging
from typing import List, Dict

def update_dialogue_patterns(dialogue: List[Dict[str, List[str]]], patterns: Dict[str, str]) -> List[Dict[str, List[str]]]:
    """
    Updates dialogue entries based on provided patterns.

    :param dialogue: List of dialogues to process.
    :param patterns: Dictionary with keys as patterns to find and values as patterns to replace with.
    :return: List of dialogues with updated patterns.
    """
    try:
        for entry in dialogue:
            entry['customer_text'] = [text.replace(pattern, replacement) for text in entry['customer_text'] for pattern, replacement in patterns.items()]
            entry['employee_text'] = [text.replace(pattern, replacement) for text in entry['employee_text'] for pattern, replacement in patterns.items()]
    except Exception as e:
        logging.error(f"Error updating dialogue patterns: {e}")

    return dialogue

if __name__ == "__main__":
    sample_dialogue = [
        {"call_id": "1", "customer_id": "cust_001", "employee_id": "emp_001",
         "customer_text": ["Hola, tengo una consulta."],
         "employee_text": ["Buenos días, ¿en qué puedo ayudarle?"]}
    ]
    
    patterns = {
        "Hola": "Hello",
        "Buenos días": "Good morning"
    }
    
    updated_dialogue = update_dialogue_patterns(sample_dialogue, patterns)
    print("Original Dialogue:", sample_dialogue)
    print("Updated Dialogue:", updated_dialogue)

# File: src/preprocessing/correct_spelling.py

from textblob import TextBlob
import nltk
import logging
from typing import List, Dict, Union

# Download necessary TextBlob corpora
nltk.download('punkt')

def correct_spelling(text: str) -> str:
    """
    Corrects spelling errors in the provided text.

    :param text: The text to correct.
    :return: Text with corrected spelling.
    """
    blob = TextBlob(text)
    corrected_text = str(blob.correct())
    return corrected_text

def correct_spelling_in_dialogue(dialogue: List[Dict[str, Union[str, List[str]]]]) -> List[Dict[str, Union[str, List[str]]]]:
    """
    Corrects spelling errors in the provided dialogue.

    :param dialogue: List of dialogues to process.
    :return: List of dialogues with corrected spelling.
    """
    for entry in dialogue:
        if 'customer_text' in entry:
            corrected_customer_text = [correct_spelling(text) for text in entry['customer_text']]
            entry['customer_text'] = corrected_customer_text
        elif 'employee_text' in entry:
            corrected_employee_text = [correct_spelling(text) for text in entry['employee_text']]
            entry['employee_text'] = corrected_employee_text
        else:
            logging.error(f"Missing '_text' in entry: {entry}")

    return dialogue

if __name__ == "__main__":
    sample_dialogue = [
        {"customer_text": ["Hola, buenos días.", "Esto es un ejemplo de texto con errores de ortografia."], "employee_text": ["Buenos días, ¿cómo puedo ayudarte?"]}
    ]
    
    corrected_dialogue = correct_spelling_in_dialogue(sample_dialogue)
    print("Corrected Dialogue:", corrected_dialogue)

# File: src/preprocessing/read_files.py

import json
import os
import logging
from typing import List, Dict

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

# File: src/preprocessing/remove_stop_words.py

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import logging
from typing import List, Dict, Union

# Download the stop words from NLTK
nltk.download('stopwords')
nltk.download('punkt')

def remove_stop_words(text: str, language: str = 'spanish') -> str:
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

def remove_stop_words_from_dialogue(dialogue: List[Dict[str, Union[str, List[str]]]], language: str = 'spanish') -> List[Dict[str, Union[str, List[str]]]]:
    """
    Removes stop words from the provided dialogue.

    :param dialogue: List of dialogues to process.
    :param language: The language of the stop words to remove (default is 'spanish').
    :return: List of dialogues with stop words removed.
    """
    for entry in dialogue:
        if 'customer_text' in entry:
            filtered_customer_text = [remove_stop_words(text, language) for text in entry['customer_text']]
            entry['customer_text'] = filtered_customer_text
        else:
            logging.error(f"Missing 'customer_text' in entry: {entry}")

        if 'employee_text' in entry:
            filtered_employee_text = [remove_stop_words(text, language) for text in entry['employee_text']]
            entry['employee_text'] = filtered_employee_text
        else:
            logging.error(f"Missing 'employee_text' in entry: {entry}")

    return dialogue

if __name__ == "__main__":
    sample_dialogue = [
        {"customer_text": ["Hola, buenos días. Estoy llamando para hacer una consulta sobre mi factura."], "employee_text": ["Buenos días, ¿cómo puedo ayudarte?"]}
    ]
    
    filtered_dialogue = remove_stop_words_from_dialogue(sample_dialogue)
    print("Filtered Dialogue:", filtered_dialogue)

# File: src/tokenization/define_tokens.py

import re
import logging
from typing import List, Dict

def define_tokens(text: str) -> List[Dict[str, str]]:
    """
    Defines tokens from the provided text. Each token is defined by its
    type and value. The function identifies words, punctuation, and numbers
    as different types of tokens.

    :param text: The text to tokenize and define tokens from.
    :return: A list of dictionaries where each dictionary represents a token
             with its type and value.
    """
    token_specification = [
        ('NUMBER', r'\b\d+\b'),           # Integer or decimal number
        ('WORD', r'\b\w+\b'),             # Words
        ('PUNCTUATION', r'[.,!?;:]'),     # Punctuation
        ('WHITESPACE', r'\s+'),           # Whitespace (not tokenized)
    ]
    
    token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
    tokens = []

    try:
        for match in re.finditer(token_regex, text):
            kind = match.lastgroup
            value = match.group()
            if kind != 'WHITESPACE':  # Ignore whitespace
                tokens.append({'type': kind, 'value': value})
    except Exception as e:
        logging.error(f"Error defining tokens for text '{text}': {e}")

    return tokens

def define_tokens_in_dialogue(dialogue: List[Dict[str, str]]) -> List[Dict[str, List[Dict[str, str]]]]:
    """
    Defines tokens for the customer and employee text in the provided dialogue.

    :param dialogue: List of dialogue entries to process.
    :return: List of dialogue entries with tokens defined for customer and employee text.
    """
    tokenized_dialogue = []

    try:
        for entry in dialogue:
            customer_text = entry['customer_text']
            employee_text = entry['employee_text']
            customer_tokens = define_tokens(customer_text)
            employee_tokens = define_tokens(employee_text)

            tokenized_entry = {
                'call_id': entry['call_id'],
                'customer_id': entry['customer_id'],
                'customer_tokens': customer_tokens,
                'employee_id': entry['employee_id'],
                'employee_tokens': employee_tokens
            }
            tokenized_dialogue.append(tokenized_entry)
    except Exception as e:
        logging.error(f"Error defining tokens in dialogue: {e}")

    return tokenized_dialogue

if __name__ == "__main__":
    sample_text = "Hola, buenos días. Estoy llamando para hacer una consulta sobre mi factura."
    print("Original text:", sample_text)
    print("Defined tokens:", define_tokens(sample_text))

    sample_dialogue = [
        {
            "call_id": "1",
            "customer_id": "cust_001",
            "customer_text": "Hola, buenos días.",
            "employee_id": "emp_001",
            "employee_text": "Buenos días, ¿cómo puedo ayudarle?"
        }
    ]

    print("Original dialogue:", sample_dialogue)
    print("Tokenized dialogue:", define_tokens_in_dialogue(sample_dialogue))

# File: src/tokenization/lexical_analysis.py

import logging
from collections import Counter
from typing import List, Dict

def lexical_analysis(tokens: List[Dict[str, str]]) -> Dict[str, int]:
    """
    Performs lexical analysis on the provided tokens to count the occurrences
    of each type of token.

    :param tokens: A list of dictionaries where each dictionary represents a token
                   with its type and value.
    :return: A dictionary with token types as keys and their counts as values.
    """
    token_counts = Counter()

    try:
        for token in tokens:
            token_type = token['type']
            token_counts[token_type] += 1
    except Exception as e:
        logging.error(f"Error performing lexical analysis on tokens: {e}")

    return dict(token_counts)

def lexical_analysis_in_dialogue(dialogue: List[Dict[str, List[Dict[str, str]]]]) -> Dict[str, int]:
    """
    Performs lexical analysis on the tokens in the provided dialogue.

    :param dialogue: List of dialogue entries with tokens defined for customer and employee text.
    :return: A dictionary with token types as keys and their counts as values for the entire dialogue.
    """
    total_counts = Counter()

    try:
        for entry in dialogue:
            customer_tokens = entry['customer_tokens']
            employee_tokens = entry['employee_tokens']

            customer_counts = lexical_analysis(customer_tokens)
            employee_counts = lexical_analysis(employee_tokens)

            total_counts.update(customer_counts)
            total_counts.update(employee_counts)
    except Exception as e:
        logging.error(f"Error performing lexical analysis in dialogue: {e}")

    return dict(total_counts)

if __name__ == "__main__":
    sample_tokens = [
        {'type': 'WORD', 'value': 'Hola'},
        {'type': 'PUNCTUATION', 'value': ','},
        {'type': 'WORD', 'value': 'buenos'},
        {'type': 'WORD', 'value': 'días'},
        {'type': 'PUNCTUATION', 'value': '.'}
    ]

    print("Sample tokens:", sample_tokens)
    print("Lexical analysis:", lexical_analysis(sample_tokens))

    sample_dialogue = [
        {
            "call_id": "1",
            "customer_id": "cust_001",
            "customer_tokens": sample_tokens,
            "employee_id": "emp_001",
            "employee_tokens": sample_tokens
        }
    ]

    print("Sample dialogue:", sample_dialogue)
    print("Lexical analysis for dialogue:", lexical_analysis_in_dialogue(sample_dialogue))

# File: src/tokenization/tokenizer.py

import logging
import nltk
from nltk.tokenize import word_tokenize
from typing import List, Dict

# Download necessary NLTK tokenizer resources
nltk.download('punkt')

def tokenize_text(text: str) -> List[Dict[str, str]]:
    """
    Tokenizes the provided text into words and punctuation.

    :param text: The text to tokenize.
    :return: List of dictionaries where each dictionary represents a token with its type and value.
    """
    tokens = word_tokenize(text)
    tokenized_output = []

    try:
        for token in tokens:
            if token.isalpha():
                token_type = 'WORD'
            elif token.isdigit():
                token_type = 'NUMBER'
            else:
                token_type = 'PUNCTUATION'
            
            tokenized_output.append({'type': token_type, 'value': token})
    except Exception as e:
        logging.error(f"Error tokenizing text '{text}': {e}")

    return tokenized_output

def tokenize_dialogue(dialogue: List[Dict[str, str]]) -> List[Dict[str, List[Dict[str, str]]]]:
    """
    Tokenizes the text in the provided dialogue.

    :param dialogue: List of dialogues to process.
    :return: List of dialogues with tokenized text.
    """
    try:
        for entry in dialogue:
            entry['customer_tokens'] = [tokenize_text(text) for text in entry['customer_text']]
            entry['employee_tokens'] = [tokenize_text(text) for text in entry['employee_text']]
    except Exception as e:
        logging.error(f"Error tokenizing dialogue: {e}")

    return dialogue

if __name__ == "__main__":
    sample_text = "Hola, buenos días. Esto es un ejemplo de tokenización de texto."
    print("Original text:", sample_text)
    print("Tokenized text:", tokenize_text(sample_text))

    sample_dialogue = [
        {
            "call_id": "1",
            "customer_id": "cust_001",
            "customer_text": "Hola, buenos días.",
            "employee_id": "emp_001",
            "employee_text": "Buenos días, ¿cómo puedo ayudarle?"
        }
    ]

    print("Original dialogue:", sample_dialogue)
    tokenized_dialogue = tokenize_dialogue(sample_dialogue)
    print("Tokenized dialogue:", tokenized_dialogue)

# File: src/utils/co_reference_resolution.py

import spacy
import logging
from typing import Optional

# Load the spaCy model
nlp = spacy.load('es_core_news_sm')

def resolve_co_references(text: str) -> Optional[str]:
    """
    Resolves co-references in the provided text.

    :param text: The text for which to resolve co-references.
    :return: Text with co-references resolved.
    """
    try:
        doc = nlp(text)
        resolved_text = text

        for cluster in doc._.coref_clusters:
            main_mention = cluster.main.text
            for mention in cluster.mentions:
                if mention != cluster.main:
                    resolved_text = resolved_text.replace(mention.text, main_mention)
        
        return resolved_text
    except Exception as e:
        logging.error(f"Error resolving co-references in text '{text}': {e}")
        return None

if __name__ == "__main__":
    sample_text = "John fue a la tienda. Él compró pan."
    print("Original text:", sample_text)
    resolved_text = resolve_co_references(sample_text)
    if resolved_text:
        print("Resolved text:", resolved_text)

# File: src/utils/error_handling.py

import logging

def log_error(error_message: str) -> None:
    """
    Logs an error message.

    :param error_message: The error message to log.
    """
    logging.error(error_message)

def handle_error(error_message: str) -> None:
    """
    Handles an error by logging it and potentially taking other actions.

    :param error_message: The error message to handle.
    """
    log_error(error_message)
    # Additional error handling actions can be added here.

if __name__ == "__main__":
    # Example usage
    try:
        raise ValueError("An example error")
    except ValueError as e:
        handle_error(str(e))

# File: src/utils/fallback.py

def fallback_response() -> str:
    """
    Returns a fallback response when the system cannot handle the request.
    
    :return: A fallback response message.
    """
    return "Lo siento, no entendí eso. ¿Puedes reformularlo?"

if __name__ == "__main__":
    # Example usage
    print(fallback_response())

# File: src/visualization/generate_charts.py

import matplotlib.pyplot as plt

def generate_bar_chart(data, title='Bar Chart', xlabel='X-axis', ylabel='Y-axis'):
    """
    Generates a bar chart from the provided data.

    :param data: A dictionary with keys as labels and values as corresponding values.
    :param title: The title of the chart.
    :param xlabel: The label for the X-axis.
    :param ylabel: The label for the Y-axis.
    """
    labels = list(data.keys())
    values = list(data.values())
    
    plt.figure(figsize=(10, 6))
    plt.bar(labels, values, color='skyblue')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

if __name__ == "__main__":
    sample_data = {'A': 10, 'B': 20, 'C': 30, 'D': 40}
    generate_bar_chart(sample_data, title='Sample Bar Chart', xlabel='Category', ylabel='Value')

# File: src/visualization/generate_graphs.py

import matplotlib.pyplot as plt
import networkx as nx

def generate_network_graph(graph_data, title='Network Graph'):
    """
    Generates a network graph from the provided graph data.

    :param graph_data: A dictionary with keys as nodes and values as lists of connected nodes.
    :param title: The title of the graph.
    """
    G = nx.Graph()
    
    for node, edges in graph_data.items():
        for edge in edges:
            G.add_edge(node, edge)
    
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='gray', linewidths=1, font_size=15)
    plt.title(title)
    plt.show()

if __name__ == "__main__":
    sample_graph_data = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D'], 'D': ['B', 'C']}
    generate_network_graph(sample_graph_data, title='Sample Network Graph')

# File: src/visualization/generate_heatmaps.py

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def generate_heatmap(data, title='Heatmap', xlabel='X-axis', ylabel='Y-axis'):
    """
    Generates a heatmap from the provided data.

    :param data: A 2D list or numpy array representing the heatmap data.
    :param title: The title of the heatmap.
    :param xlabel: The label for the X-axis.
    :param ylabel: The label for the Y-axis.
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(data, annot=True, fmt="d", cmap='YlGnBu')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

if __name__ == "__main__":
    sample_data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    generate_heatmap(sample_data, title='Sample Heatmap', xlabel='Category', ylabel='Value')

# File: src/__init__.py

# Make sure to import the submodules so they can be used as part of the package
from . import preprocessing
from . import analysis
from . import post_processing
from . import tokenization
from . import utils
from . import visualization

__all__ = [
    'preprocessing',
    'analysis',
    'post_processing',
    'tokenization',
    'utils',
    'visualization'
]

# File: src/analysis/__init__.py

# This file makes the 'analysis' directory a Python package.
# It can be used to import functions from the module files easily.

from .dialogue_act import identify_dialogue_acts, classify_dialogue_act
from .emotional_tone import analyze_emotional_tone, get_emotional_tone
from .scoring import score_dialogue_quality, score_text

__all__ = [
    'identify_dialogue_acts',
    'classify_dialogue_act',
    'analyze_emotional_tone',
    'get_emotional_tone',
    'score_dialogue_quality',
    'score_text'
]

# File: src/post_processing/__init__.py

# This file makes the 'post_processing' directory a Python package.
# It can be used to import functions from the module files easily.

from .manual_adjustments import apply_manual_adjustments
from .update_patterns import update_dialogue_patterns

__all__ = [
    'apply_manual_adjustments',
    'update_dialogue_patterns'
]

# File: src/preprocessing/__init__.py

# This file makes the 'preprocessing' directory a Python package.
# It can be used to import functions from the module files easily.

from .read_files import read_dialogue_file, read_dialogues, display_data_nicely
from .remove_stop_words import remove_stop_words, remove_stop_words_from_dialogue
from .correct_spelling import correct_spelling, correct_spelling_in_dialogue

__all__ = [
    'read_dialogue_file',
    'read_dialogues',
    'display_data_nicely',
    'remove_stop_words',
    'remove_stop_words_from_dialogue',
    'correct_spelling',
    'correct_spelling_in_dialogue'
]

# File: src/tokenization/__init__.py

# This file makes the 'tokenization' directory a Python package.
# It can be used to import functions from the module files easily.

from .define_tokens import define_tokens, define_tokens_in_dialogue
from .lexical_analysis import lexical_analysis, lexical_analysis_in_dialogue
from .tokenizer import tokenize_text, tokenize_dialogue

__all__ = [
    'define_tokens',
    'define_tokens_in_dialogue',
    'lexical_analysis',
    'lexical_analysis_in_dialogue',
    'tokenize_text',
    'tokenize_dialogue'
]

# File: src/utils/__init__.py

# This file makes the 'utils' directory a Python package.
# It can be used to import functions from the module files easily.

from .co_reference_resolution import resolve_co_references
from .error_handling import log_error, handle_error
from .fallback import fallback_response

__all__ = [
    'resolve_co_references',
    'log_error',
    'handle_error',
    'fallback_response'
]

# File: src/visualization/__init__.py

# This file makes the 'visualization' directory a Python package.
# It can be used to import functions from the module files easily.

from .generate_charts import generate_bar_chart
from .generate_graphs import generate_network_graph
from .generate_heatmaps import generate_heatmap

__all__ = [
    'generate_bar_chart',
    'generate_network_graph',
    'generate_heatmap'
]
