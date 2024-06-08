import logging
from typing import List, Dict

class PatternUpdateError(Exception):
    """Custom exception for errors during pattern updates."""
    pass

def update_dialogue_patterns(dialogue: List[Dict[str, List[str]]], patterns: Dict[str, str]) -> List[Dict[str, List[str]]]:
    """
    Updates dialogue entries based on provided patterns.

    :param dialogue: List of dialogues to process.
    :param patterns: Dictionary with keys as patterns to find and values as patterns to replace with.
    :return: List of dialogues with updated patterns.
    """
    logger = logging.getLogger(__name__)
    logger.info("Starting pattern updates on dialogues")

    try:
        for entry in dialogue:
            entry['customer_text'] = [text.replace(pattern, replacement) for text in entry['customer_text'] for pattern, replacement in patterns.items()]
            entry['employee_text'] = [text.replace(pattern, replacement) for text in entry['employee_text'] for pattern, replacement in patterns.items()]
    except Exception as e:
        logger.error(f"Error updating dialogue patterns: {e}")
        raise PatternUpdateError(f"Error updating dialogue patterns: {e}")

    logger.info("Completed pattern updates on dialogues")
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
