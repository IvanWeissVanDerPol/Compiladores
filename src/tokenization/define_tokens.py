import re
import logging
from typing import List, Dict

class TokenDefinitionError(Exception):
    """Custom exception for errors during token definition."""
    pass

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

    logger = logging.getLogger(__name__)
    logger.info(f"Defining tokens for text: {text}")

    try:
        for match in re.finditer(token_regex, text):
            kind = match.lastgroup
            value = match.group()
            if kind != 'WHITESPACE':  # Ignore whitespace
                tokens.append({'type': kind, 'value': value})
    except Exception as e:
        logger.error(f"Error defining tokens for text '{text}': {e}")
        raise TokenDefinitionError(f"Error defining tokens for text '{text}': {e}")

    logger.info(f"Completed defining tokens for text: {text}")
    return tokens

def define_tokens_in_dialogue(dialogue: List[Dict[str, str]]) -> List[Dict[str, List[Dict[str, str]]]]:
    """
    Defines tokens for the customer and employee text in the provided dialogue.

    :param dialogue: List of dialogue entries to process.
    :return: List of dialogue entries with tokens defined for customer and employee text.
    """
    tokenized_dialogue = []
    logger = logging.getLogger(__name__)
    logger.info("Starting token definition in dialogues")

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
    except KeyError as e:
        logger.error(f"Missing key in entry {entry}: {e}")
    except TokenDefinitionError as e:
        logger.error(f"TokenDefinitionError in entry {entry}: {e}")
    except Exception as e:
        logger.error(f"Unexpected error in entry {entry}: {e}")

    logger.info("Completed token definition in dialogues")
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
