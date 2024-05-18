import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download the stop words from NLTK
nltk.download('stopwords')
nltk.download('punkt')

def remove_stop_words(text, language='spanish'):
    """
    Removes stop words from the provided text.

    :param text: The text from which to remove stop words.
    :param language: The language of the stop words to remove (default is 'spanish').
    :return: Text with stop words removed.
    """
    stop_words = set(stopwords.words(language))
    word_tokens = word_tokenize(text)

    filtered_text = [word for word in word_tokens if word.lower() not in stop_words]
    return ' '.join(filtered_text)

def remove_stop_words_from_dialogue(dialogue, language='spanish'):
    """
    Removes stop words from the provided dialogue.

    :param dialogue: List of dialogues to process.
    :param language: The language of the stop words to remove (default is 'spanish').
    :return: List of dialogues with stop words removed.
    """
    for entry in dialogue:
        entry['customer_text'] = remove_stop_words(entry['customer_text'], language)
        entry['employee_text'] = remove_stop_words(entry['employee_text'], language)
    return dialogue

if __name__ == "__main__":
    sample_text = "Hola, buenos días. Estoy llamando para hacer una consulta sobre mi factura."
    print("Original text:", sample_text)
    print("Text without stop words:", remove_stop_words(sample_text))
