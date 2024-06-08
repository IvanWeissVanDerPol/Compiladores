import spacy
import logging
from typing import Optional

class CoReferenceResolutionError(Exception):
    """Custom exception for errors during co-reference resolution."""
    pass

# Load the spaCy model
nlp = spacy.load('es_core_news_sm')

def resolve_co_references(text: str) -> Optional[str]:
    """
    Resolves co-references in the provided text.

    :param text: The text for which to resolve co-references.
    :return: Text with co-references resolved.
    """
    logger = logging.getLogger(__name__)
    logger.info(f"Resolving co-references for text: {text}")

    try:
        doc = nlp(text)
        resolved_text = text

        for cluster in doc._.coref_clusters:
            main_mention = cluster.main.text
            for mention in cluster.mentions:
                if mention != cluster.main:
                    resolved_text = resolved_text.replace(mention.text, main_mention)
        
        return resolved_text
    except Exception as e:
        logger.error(f"Error resolving co-references in text '{text}': {e}")
        raise CoReferenceResolutionError(f"Error resolving co-references in text '{text}': {e}")

if __name__ == "__main__":
    sample_text = "John fue a la tienda. Él compró pan."
    print("Original text:", sample_text)
    resolved_text = resolve_co_references(sample_text)
    if resolved_text:
        print("Resolved text:", resolved_text)
