import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import logging
from typing import List, Dict, Union

# Download the stop words and tokenization resources from NLTK
nltk.download('stopwords')
nltk.download('punkt')

def remove_stop_words(text: str, language: str = 'spanish') -> str:
    """
    Removes stop words from the provided text.

    This function uses the NLTK library to remove stop words from a text in a specified language.
    Stop words are common words that are usually filtered out in natural language processing.

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

    This function iterates through a list of dialogue entries, removing stop words
    from both customer and employee texts using the remove_stop_words function. The original
    dialogue is kept unchanged, and a new list with stop words removed is returned.

    :param dialogue: List of dialogues to process. Each dialogue is a dictionary that 
                     contains customer and employee texts.
    :param language: The language of the stop words to remove (default is 'spanish').
    :return: List of dialogues with stop words removed.
    :raises StopWordsRemovalError: If an error occurs during stop words removal.
    """
    logging.info("Starting stop words removal on dialogues")

    filtered_dialogue = []
    for entry in dialogue:
        filtered_entry = entry.copy()
        if 'customer_text' in entry:
            filtered_entry['customer_text'] = [remove_stop_words(text, language) for text in entry['customer_text']]
        else:
            logging.error(f"Missing 'customer_text' in entry: {entry}")
        if 'employee_text' in entry:
            filtered_entry['employee_text'] = [remove_stop_words(text, language) for text in entry['employee_text']]
        else:
            logging.error(f"Missing 'employee_text' in entry: {entry}")
        filtered_dialogue.append(filtered_entry)

    logging.info("Completed stop words removal on dialogues")
    return filtered_dialogue

if __name__ == "__main__":
    sample_dialogue = [
        {"customer_text": ["Hola, buenos días. Estoy llamando para hacer una consulta sobre mi factura."], "employee_text": ["Buenos días, ¿cómo puedo ayudarte?"]}
    ]
    
    filtered_dialogue = remove_stop_words_from_dialogue(sample_dialogue)
    print("Filtered Dialogue:", filtered_dialogue)
