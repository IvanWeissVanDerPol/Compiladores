import spacy
import logging
from typing import List, Dict, Union

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

class DialogueActError(Exception):
    """Custom exception for errors during dialogue act classification."""
    pass

def classify_dialogue_act(text: str) -> str:
    """
    Classifies the dialogue act of a given text.

    This function analyzes the text using a spaCy model and classifies it into one of several dialogue acts 
    based on predefined keywords.

    :param text: The text to classify.
    :return: Dialogue act classification.
    :raises DialogueActError: If an error occurs during classification.
    """
    logger = logging.getLogger(__name__)
    logger.info(f"Classifying dialogue act for text: {text}")
    
    try:
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
    except Exception as e:
        logger.error(f"Error classifying dialogue act for text '{text}': {e}")
        raise DialogueActError(f"Error classifying dialogue act for text '{text}': {e}")

def identify_dialogue_acts(dialogue: List[Dict[str, List[str]]]) -> List[Dict[str, Union[str, List[str]]]]:
    """
    Identifies dialogue acts in the provided dialogue.

    This function iterates through a list of dialogue entries, classifying each piece of text as a specific 
    dialogue act. The original dialogue is kept unchanged, and a new list with identified dialogue acts is returned.

    :param dialogue: List of dialogues to process.
    :return: List of dialogues with identified dialogue acts.
    """
    dialogue_acts = []
    logger = logging.getLogger(__name__)
    logger.info("Starting dialogue act identification")
    
    for entry in dialogue:
        try:
            new_entry = entry.copy()
            new_entry['customer_acts'] = [classify_dialogue_act(text) for text in entry['customer_text']]
            new_entry['employee_acts'] = [classify_dialogue_act(text) for text in entry['employee_text']]
            dialogue_acts.append(new_entry)
        except KeyError as e:
            logger.error(f"Missing key in entry {entry}: {e}")
        except DialogueActError as e:
            logger.error(f"DialogueActError in entry {entry}: {e}")
        except Exception as e:
            logger.error(f"Unexpected error in entry {entry}: {e}")

    logger.info("Completed dialogue act identification")
    return dialogue_acts

if __name__ == "__main__":
    sample_dialogue = [
        {"call_id": "1", "customer_id": "cust_001", "employee_id": "emp_001",
         "customer_text": ["Hola, tengo una pregunta sobre mi factura."],
         "employee_text": ["Claro, ¿cómo puedo ayudarte?"]}
    ]

    dialogue_acts = identify_dialogue_acts(sample_dialogue)
    print("Dialogue Acts:", dialogue_acts)
