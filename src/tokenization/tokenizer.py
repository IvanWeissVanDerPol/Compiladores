import nltk
from nltk.tokenize import word_tokenize

# Download necessary NLTK tokenizer resources
nltk.download('punkt')

def tokenize_text(text):
    """
    Tokenizes the provided text into words.

    :param text: The text to tokenize.
    :return: List of tokens.
    """
    tokens = word_tokenize(text)
    return tokens

def tokenize_dialogue(dialogue):
    """
    Tokenizes the text in the provided dialogue.

    :param dialogue: List of dialogues to process.
    :return: List of dialogues with tokenized text.
    """
    for entry in dialogue:
        entry['customer_tokens'] = tokenize_text(entry['customer_text'])
        entry['employee_tokens'] = tokenize_text(entry['employee_text'])
    return dialogue

if __name__ == "__main__":
    sample_text = "Hola, buenos días. Esto es un ejemplo de tokenización de texto."
    print("Original text:", sample_text)
    print("Tokenized text:", tokenize_text(sample_text))
