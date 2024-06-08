import logging
import nltk
from nltk.tokenize import word_tokenize
from typing import List, Dict, Union

class TokenizationError(Exception):
    """Custom exception for errors during tokenization."""
    pass

# Download necessary NLTK tokenizer resources
nltk.download('punkt')

def tokenize_text(text: str) -> List[Dict[str, str]]:
    """
    Tokenizes the provided text into words and punctuation.

    This function uses the NLTK library to tokenize the text into words, numbers, 
    and punctuation marks, and then classifies each token by its type.

    :param text: The text to tokenize.
    :return: List of dictionaries where each dictionary represents a token with its type and value.
    :raises TokenizationError: If an error occurs during tokenization.
    """
    try:
        tokens = word_tokenize(text)
        tokenized_output = []

        for token in tokens:
            if token.isalpha():
                token_type = 'WORD'
            elif token.isdigit():
                token_type = 'NUMBER'
            else:
                token_type = 'PUNCTUATION'
            
            tokenized_output.append({'type': token_type, 'value': token})
        
        return tokenized_output
    except Exception as e:
        logging.error(f"Error tokenizing text '{text}': {e}")
        raise TokenizationError(f"Error tokenizing text '{text}': {e}")

def tokenize_dialogue(dialogue: List[Dict[str, Union[str, List[str]]]]) -> List[Dict[str, Union[str, List[Dict[str, str]]]]]:
    """
    Tokenizes the text in the provided dialogue.

    This function iterates through a list of dialogue entries, tokenizing the customer and employee texts
    using the tokenize_text function. The original dialogue is kept unchanged, and a new list with tokenized
    texts is returned.

    :param dialogue: List of dialogues to process. Each dialogue is a dictionary that contains 
                     customer and employee texts.
    :return: List of dialogues with tokenized text.
    :raises TokenizationError: If an error occurs during tokenization.
    """
    logging.info("Starting tokenization on dialogues")

    tokenized_dialogue = []
    for entry in dialogue:
        tokenized_entry = entry.copy()
        if 'customer_text' in entry:
            tokenized_entry['customer_text'] = [tokenize_text(text) for text in entry['customer_text']]
        else:
            logging.error(f"Missing 'customer_text' in entry: {entry}")
        
        if 'employee_text' in entry:
            tokenized_entry['employee_text'] = [tokenize_text(text) for text in entry['employee_text']]
        else:
            logging.error(f"Missing 'employee_text' in entry: {entry}")
            
        tokenized_dialogue.append(tokenized_entry)

    logging.info("Completed tokenization on dialogues")
    return tokenized_dialogue

if __name__ == "__main__":
    sample_text = "Hola, buenos días. Esto es un ejemplo de tokenización de texto."
    print("Original text:", sample_text)
    print("Tokenized text:", tokenize_text(sample_text))

    sample_dialogue = [
        {
            "call_id": "1",
            "customer_id": "cust_001",
            "customer_text": ["Hola, buenos días."],
            "employee_id": "emp_001",
            "employee_text": ["Buenos días, ¿cómo puedo ayudarle?"]
        }
    ]

    print("Original dialogue:", sample_dialogue)
    tokenized_dialogue = tokenize_dialogue(sample_dialogue)
    print("Tokenized dialogue:", tokenized_dialogue)
