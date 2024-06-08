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
