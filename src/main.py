import logging
from preprocessing import read_dialogue_file, correct_spelling_in_dialogue, remove_stop_words_from_dialogue
from tokenization import tokenize_text, tokenize_dialogue
from analysis import identify_dialogue_acts, analyze_emotional_tone, score_dialogue_quality
from config import Config
from typing import List, Dict, Union

class DialogueProcessingError(Exception):
    """Custom exception for errors during dialogue processing."""
    pass

def main() -> None:
    # Create necessary directories
    Config.create_directories()

    # Configure logging
    logging.basicConfig(filename=Config.LOG_FILE, level=Config.LOG_LEVEL, format='%(asctime)s - %(levelname)s - %(message)s')

    logger = logging.getLogger(__name__)
    logger.info("Starting dialogue processing")
    
    try:
        logger.info("Reading customer dialogues")
        dialogues: List[Dict[str, Union[str, List[str]]]] = read_dialogue_file(Config.DIALOGUES_FILE)
        logger.info("Customer dialogues loaded successfully")

        logger.info("Correcting spelling in customer dialogues")
        dialogues_corrected = correct_spelling_in_dialogue(dialogues)
        logger.info("Spelling corrected in customer dialogues")

        logger.info("Removing stop words from customer dialogues")
        dialogues_no_stop = remove_stop_words_from_dialogue(dialogues_corrected)
        logger.info("Stop words removed from customer dialogues")


        logger.info("Tokenizing customer dialogues")
        dialogues_tokenized = tokenize_dialogue(dialogues_no_stop)
        logger.info("Customer dialogues tokenized")


        logger.info("Analyzing dialogue acts in customer dialogues")
        dialogue_acts = identify_dialogue_acts(dialogues_tokenized)
        logger.info("Dialogue acts analyzed in customer dialogues")

        logger.info("Analyzing emotional tone in customer dialogues")
        emotional_tones = analyze_emotional_tone(dialogue_acts)
        logger.info("Emotional tone analyzed in customer dialogues")

        logger.info("Scoring dialogue quality in customer dialogues")
        scores = score_dialogue_quality(emotional_tones)
        logger.info("Dialogue quality scored in customer dialogues")


        # Display results
        logger.info("Customer Dialogues Analysis:")
        for dialogue in scores:
            logger.info(dialogue)
            print(dialogue)


    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        raise DialogueProcessingError(f"Error: {e}")

if __name__ == "__main__":
    main()
