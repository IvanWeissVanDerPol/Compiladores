from textblob import TextBlob
import nltk
import logging
from typing import List, Dict, Union
from spellchecker import SpellChecker

class SpellingCorrectionError(Exception):
    """Custom exception for errors during spelling correction."""
    pass

# Initialize the spell checker for Spanish
spell = SpellChecker(language='es')

# Download necessary TextBlob corpora
nltk.download('punkt')

def correct_spelling(text: str) -> str:
    """
    Corrects spelling errors in the provided text.

    :param text: The text to correct.
    :return: Text with corrected spelling.
    :raises SpellingCorrectionError: If an error occurs during spelling correction.
    """
    try:
        blob = TextBlob(text)
        words = blob.words
        corrected_words = []
        
        for word in words:
            corrected_word = spell.correction(word)
            corrected_words.append(corrected_word if corrected_word is not None else word)
        
        corrected_text = ' '.join(corrected_words)
        return corrected_text
    except Exception as e:
        logging.error(f"Error correcting spelling for text '{text}': {e}")
        raise SpellingCorrectionError(f"Error correcting spelling for text '{text}': {e}")

def correct_spelling_in_dialogue(dialogue: List[Dict[str, Union[str, List[str]]]]) -> List[Dict[str, Union[str, List[str]]]]:
    """
    Corrects spelling errors in the provided dialogue while keeping the original dialogue unchanged.

    :param dialogue: List of dialogues to process.
    :return: List of dialogues with corrected spelling.
    """
    logging.info("Starting spelling correction on dialogues")
    corrected_dialogue = []

    for entry in dialogue:
        new_entry = entry.copy()
        if 'customer_text' in entry:
            new_entry['customer_text'] = [correct_spelling(text) for text in entry['customer_text']]
        else:
            logging.error(f"Missing 'customer_text' in entry: {entry}")
        
        if 'employee_text' in entry:
            new_entry['employee_text'] = [correct_spelling(text) for text in entry['employee_text']]
        else:
            logging.error(f"Missing 'employee_text' in entry: {entry}")
        
        corrected_dialogue.append(new_entry)

    logging.info("Completed spelling correction on dialogues")
    return corrected_dialogue

if __name__ == "__main__":
    sample_dialogue = [
        {"customer_text": ["Hola, buenos días.", "Esto es un ejemplo de texto con errores de ortografia."], "employee_text": ["Buenos días, ¿cómo puedo ayudarte?"]}
    ]
    
    corrected_dialogue = correct_spelling_in_dialogue(sample_dialogue)
    print("Corrected Dialogue:", corrected_dialogue)
