import logging
from typing import List, Dict, Union

class ScoringError(Exception):
    """Custom exception for errors during scoring."""
    pass

def score_text(text: str) -> int:
    """
    Scores the quality of a given text.

    The function evaluates the text based on the presence of positive and negative tokens.
    It counts the occurrences of positive and negative words and calculates a score based
    on their difference. The score is scaled and constrained to be between 0 and 100.

    :param text: The text to score.
    :return: A quality score (0 to 100).
    :raises ScoringError: If an error occurs during scoring.
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

    logger = logging.getLogger(__name__)
    logger.info(f"Scoring text: {text}")
    
    try:
        positive_count = sum(1 for word in text.split() if word.lower() in positive_tokens)
        negative_count = sum(1 for word in text.split() if word.lower() in negative_tokens)
        
        score = (positive_count - negative_count) * 10
        return max(0, min(100, score))  # Ensure score is between 0 and 100
    except Exception as e:
        logger.error(f"Error scoring text '{text}': {e}")
        raise ScoringError(f"Error scoring text '{text}': {e}")

def score_dialogue_quality(dialogue: List[Dict[str, Union[str, List[str]]]]) -> List[Dict[str, Union[str, List[int]]]]:
    """
    Scores the quality of the provided dialogue.

    This function iterates through a list of dialogue entries, scoring the quality of each piece of text.
    The original dialogue is kept unchanged, and a new list with quality scores is returned.

    :param dialogue: List of dialogues to process.
    :return: List of dialogues with quality scores.
    """
    scored_dialogues = []
    logger = logging.getLogger(__name__)
    logger.info("Starting dialogue quality scoring")
    
    for entry in dialogue:
        try:
            new_entry = entry.copy()
            new_entry['customer_scores'] = [score_text(text) for text in entry['customer_text']]
            new_entry['employee_scores'] = [score_text(text) for text in entry['employee_text']]
            scored_dialogues.append(new_entry)
        except KeyError as e:
            logger.error(f"Missing key in entry {entry}: {e}")
        except ScoringError as e:
            logger.error(f"ScoringError in entry {entry}: {e}")
        except Exception as e:
            logger.error(f"Unexpected error in entry {entry}: {e}")

    logger.info("Completed dialogue quality scoring")
    return scored_dialogues

if __name__ == "__main__":
    sample_dialogue = [
        {"call_id": "1", "customer_id": "cust_001", "employee_id": "emp_001",
         "customer_text": ["¿Puede ayudarme con mi cuenta?"],
         "employee_text": ["¡Por supuesto! ¿En qué necesita ayuda?"]}
    ]
    
    scored_dialogues = score_dialogue_quality(sample_dialogue)
    print("Scored Dialogues:", scored_dialogues)
