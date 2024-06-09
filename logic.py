import json

class DialogueProcessor:
    def __init__(self, employee_file, customer_file, keywords_file):
        self.employee_dialogues, self.customer_dialogues = self.load_data(employee_file, customer_file)
        self.keywords = self.load_keywords(keywords_file)
        self.update_unclassified_keywords()

    def load_data(self, employee_file, customer_file):
        employee_dialogues = self._load_json(employee_file)
        customer_dialogues = self._load_json(customer_file)
        
        # Convert all text to lowercase
        self._convert_to_lowercase(employee_dialogues, 'employee_text')
        self._convert_to_lowercase(customer_dialogues, 'customer_text')
        
        return employee_dialogues, customer_dialogues
    
    def _load_json(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
    
    def _convert_to_lowercase(self, dialogues, key):
        for dialogue in dialogues:
            dialogue[key] = [text.lower() for text in dialogue[key]]
    
    def load_keywords(self, keywords_file):
        keywords = self._load_json(keywords_file)
        
        # Convert all keywords to lowercase
        for category in keywords:
            keywords[category] = [keyword.lower() for keyword in keywords[category]]
        
        return keywords
    
    def save_keywords(self, keywords_file='data/keywords.json'):
        with open(keywords_file, 'w', encoding='utf-8') as file:
            json.dump(self.keywords, file, ensure_ascii=False, indent=4)
    
    def get_text_by_call_id(self, dialogues, call_id, key):
        return next(dialogue[key] for dialogue in dialogues if dialogue['call_id'] == call_id)
    
    def update_unclassified_keywords(self):
        all_keywords = self._get_all_keywords()
        
        for dialogue in self.employee_dialogues + self.customer_dialogues:
            for sentence in dialogue.get('employee_text', []) + dialogue.get('customer_text', []):
                words = self.split_into_words_and_phrases(sentence)
                for word in words:
                    clean_word = word.strip(".,?!").lower()
                    if clean_word not in all_keywords and clean_word not in self.keywords['UNCLASSIFIED_KEYWORDS']:
                        self.keywords['UNCLASSIFIED_KEYWORDS'].append(clean_word)
        
        self.save_keywords()
    
    def _get_all_keywords(self):
        all_keywords = set()
        for key in self.keywords:
            if key != 'UNCLASSIFIED_KEYWORDS':
                all_keywords.update(self.keywords[key])
        return all_keywords
    
    def split_into_words_and_phrases(self, sentence):
        # Split the sentence into words and phrases based on the keyword list
        words = sentence.lower().split()
        phrases = []
        skip_next = False
        for i in range(len(words) - 1):
            if skip_next:
                skip_next = False
                continue
            two_word_phrase = f"{words[i]} {words[i+1]}"
            if self.is_phrase_in_keywords(two_word_phrase):
                phrases.append(two_word_phrase)
                skip_next = True
            else:
                phrases.append(words[i])
        if not skip_next:
            phrases.append(words[-1])
        return phrases
    
    def is_phrase_in_keywords(self, phrase):
        for category in self.keywords:
            if phrase in self.keywords[category]:
                return True
        return False

    def classify_keyword(self, keyword, category):
        self.keywords[category].append(keyword)
        self.keywords['UNCLASSIFIED_KEYWORDS'].remove(keyword)
        self.save_keywords()

    def is_positive_keyword(self, keyword):
        positive_categories = [
            'POSITIVE_FEEDBACK_KEYWORDS', 'THANKS_KEYWORDS', 
            'GREETING_KEYWORDS', 'FAREWELL_KEYWORDS'
        ]
        return any(keyword in self.keywords[category] for category in positive_categories)

    def is_negative_keyword(self, keyword):
        negative_categories = [
            'NEGATIVE_FEEDBACK_KEYWORDS', 'COMPLAINTS_KEYWORDS'
        ]
        return any(keyword in self.keywords[category] for category in negative_categories)
