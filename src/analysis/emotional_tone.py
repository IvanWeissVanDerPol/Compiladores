import logging
from textblob import TextBlob
from typing import List, Dict, Union

class EmotionalToneError(Exception):
    """Custom exception for errors during emotional tone analysis."""
    pass

def get_emotional_tone(text: str) -> str:
    """
    Determines the emotional tone of a given text.

    Analyzes the sentiment polarity of the text and categorizes it as positive, negative, or neutral.

    :param text: Text to analyze.
    :return: Emotional tone (positive, negative, neutral).
    :raises EmotionalToneError: If an error occurs during emotional tone analysis.
    """
    logger = logging.getLogger(__name__)
    logger.info(f"Analyzing emotional tone for text: {text}")
    
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
        logger.error(f"Error analyzing emotional tone for text '{text}': {e}")
        raise EmotionalToneError(f"Error analyzing emotional tone for text '{text}': {e}")

def analyze_emotional_tone(dialogue: List[Dict[str, List[str]]]) -> List[Dict[str, Union[str, List[str]]]]:
    """
    Analyzes the emotional tone of the provided dialogue.

    This function iterates through a list of dialogue entries, analyzing the emotional tone of each piece of text.
    The original dialogue is kept unchanged, and a new list with analyzed emotional tones is returned.

    :param dialogue: List of dialogues to process.
    :return: List of dialogues with analyzed emotional tones.
    """
    emotional_tones = []
    logger = logging.getLogger(__name__)
    logger.info("Starting emotional tone analysis")
    
    for entry in dialogue:
        try:
            new_entry = entry.copy()
            new_entry['customer_tones'] = [get_emotional_tone(text) for text in entry['customer_text']]
            new_entry['employee_tones'] = [get_emotional_tone(text) for text in entry['employee_text']]
            emotional_tones.append(new_entry)
        except KeyError as e:
            logger.error(f"Missing key in entry {entry}: {e}")
        except EmotionalToneError as e:
            logger.error(f"EmotionalToneError in entry {entry}: {e}")
        except Exception as e:
            logger.error(f"Unexpected error in entry {entry}: {e}")

    logger.info("Completed emotional tone analysis")
    return emotional_tones

if __name__ == "__main__":
    sample_dialogue = [
        {"call_id": "1", "customer_id": "cust_001", "employee_id": "emp_001",
         "customer_text": ["Estoy muy contento con su servicio."],
         "employee_text": ["Gracias por sus amables palabras."]}
    ]
    
    emotional_tones = analyze_emotional_tone(sample_dialogue)
    print("Emotional Tones:", emotional_tones)
