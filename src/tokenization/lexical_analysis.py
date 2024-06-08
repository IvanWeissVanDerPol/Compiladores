import logging
from collections import Counter
from typing import List, Dict

class LexicalAnalysisError(Exception):
    """Custom exception for errors during lexical analysis."""
    pass

def lexical_analysis(tokens: List[Dict[str, str]]) -> Dict[str, int]:
    """
    Performs lexical analysis on the provided tokens to count the occurrences
    of each type of token.

    :param tokens: A list of dictionaries where each dictionary represents a token
                   with its type and value.
    :return: A dictionary with token types as keys and their counts as values.
    """
    token_counts = Counter()
    logger = logging.getLogger(__name__)
    logger.info("Starting lexical analysis on tokens")

    try:
        for token in tokens:
            token_type = token['type']
            token_counts[token_type] += 1
    except Exception as e:
        logger.error(f"Error performing lexical analysis on tokens: {e}")
        raise LexicalAnalysisError(f"Error performing lexical analysis on tokens: {e}")

    logger.info("Completed lexical analysis on tokens")
    return dict(token_counts)

def lexical_analysis_in_dialogue(dialogue: List[Dict[str, List[Dict[str, str]]]]) -> Dict[str, int]:
    """
    Performs lexical analysis on the tokens in the provided dialogue.

    :param dialogue: List of dialogue entries with tokens defined for customer and employee text.
    :return: A dictionary with token types as keys and their counts as values for the entire dialogue.
    """
    total_counts = Counter()
    logger = logging.getLogger(__name__)
    logger.info("Starting lexical analysis in dialogues")

    try:
        for entry in dialogue:
            customer_tokens = entry['customer_tokens']
            employee_tokens = entry['employee_tokens']

            customer_counts = lexical_analysis(customer_tokens)
            employee_counts = lexical_analysis(employee_tokens)

            total_counts.update(customer_counts)
            total_counts.update(employee_counts)
    except KeyError as e:
        logger.error(f"Missing key in entry {entry}: {e}")
    except LexicalAnalysisError as e:
        logger.error(f"LexicalAnalysisError in entry {entry}: {e}")
    except Exception as e:
        logger.error(f"Unexpected error in entry {entry}: {e}")

    logger.info("Completed lexical analysis in dialogues")
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
