import tkinter as tk
from tkinter import ttk
import re
from logic import DialogueProcessor

class DialogueClassifierApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dialogue Classifier")
        
        self.processor = DialogueProcessor('data/employee_dialogues.json', 'data/customer_dialogues.json', 'data/keywords.json')
        
        self.create_widgets()
        self.populate_call_ids()
    
    def create_widgets(self):
        self.call_id_selector = self.create_combobox(0, 0, 2, self.load_dialogues)
        self.employee_text_area = self.create_text_area(1, 0)
        self.customer_text_area = self.create_text_area(1, 1)
        self.keyword_selector = self.create_combobox(2, 0, 2, self.highlight_keyword)
        self.category_selector = self.create_category_selector(3, 0, 2)
        self.create_button(4, 0, 2, "Apply Category", self.apply_category)
    
    def create_combobox(self, row, col, colspan, event_handler):
        combobox = ttk.Combobox(self.root, state='readonly')
        combobox.grid(row=row, column=col, columnspan=colspan, padx=10, pady=10)
        combobox.bind("<<ComboboxSelected>>", event_handler)
        return combobox
    
    def create_text_area(self, row, col):
        text_area = tk.Text(self.root, height=15, width=60)
        text_area.grid(row=row, column=col, padx=10, pady=10)
        return text_area
    
    def create_category_selector(self, row, col, colspan):
        category_selector = ttk.Combobox(self.root, state='readonly', values=[
            "QUESTION_KEYWORDS", "THANKS_KEYWORDS", "GREETING_KEYWORDS", "FAREWELL_KEYWORDS",
            "STATEMENT_KEYWORDS", "APOLOGIES_KEYWORDS", "COMPLAINTS_KEYWORDS", "NEUTRAL_KEYWORDS",
            "SERVICE_INFORMATION_KEYWORDS", "POSITIVE_KEYWORDS", "NEGATIVE_KEYWORDS",
            "SUGGESTIONS_KEYWORDS"
        ])
        category_selector.grid(row=row, column=col, columnspan=colspan, padx=10, pady=10)
        return category_selector
    
    def create_button(self, row, col, colspan, text, command):
        button = tk.Button(self.root, text=text, command=command)
        button.grid(row=row, column=col, columnspan=colspan, padx=10, pady=10)
        return button
    
    def populate_call_ids(self):
        call_ids = [dialogue['call_id'] for dialogue in self.processor.employee_dialogues]
        self.call_id_selector['values'] = call_ids
        if call_ids:
            self.call_id_selector.current(0)
            self.load_dialogues()
    
    def load_dialogues(self, event=None):
        call_id = self.call_id_selector.get()
        employee_text = self.processor.get_text_by_call_id(self.processor.employee_dialogues, call_id, 'employee_text')
        customer_text = self.processor.get_text_by_call_id(self.processor.customer_dialogues, call_id, 'customer_text')
        
        self.display_text(self.employee_text_area, employee_text)
        self.display_text(self.customer_text_area, customer_text)
        
        self.load_unclassified_keywords()
    
    def display_text(self, text_area, text):
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, "\n".join(text))
    
    def load_unclassified_keywords(self):
        unclassified_keywords = self.processor.keywords['UNCLASSIFIED_KEYWORDS']
        self.keyword_selector['values'] = unclassified_keywords
        if unclassified_keywords:
            self.keyword_selector.current(0)
            self.highlight_keyword()
    
    def highlight_keyword(self, event=None):
        keyword = self.keyword_selector.get()
        self.highlight_text(self.employee_text_area, keyword)
        self.highlight_text(self.customer_text_area, keyword)
    
    def highlight_text(self, text_widget, keyword, tag_name="highlight", tag_bg="yellow"):
        # Remove any existing tags of the same name
        text_widget.tag_remove(tag_name, "1.0", tk.END)
        
        # Get the entire content of the text widget
        text = text_widget.get("1.0", tk.END)
        
        start_pos = 0  # Initialize the start index
        
        # Compile a regular expression pattern to match whole words
        pattern = re.compile(r'\b' + re.escape(keyword) + r'\b', re.IGNORECASE)
        
        # Loop through the text to find and highlight all occurrences of the keyword
        for match in pattern.finditer(text):
            start_pos = match.start()
            end_pos = match.end()
            
            # Convert the start and end positions to tkinter's index format
            start_index = f"1.0+{start_pos}c"
            end_index = f"1.0+{end_pos}c"
            
            # Add the tag to highlight the keyword
            text_widget.tag_add(tag_name, start_index, end_index)
        
        # Configure the tag's appearance
        text_widget.tag_config(tag_name, background=tag_bg)
                   
    def apply_category(self):
        keyword = self.keyword_selector.get()
        category = self.category_selector.get()
        if keyword and category:
            self.processor.classify_keyword(keyword, category)
            print(f"Keyword: {keyword}, Category: {category}")
            self.load_unclassified_keywords()

if __name__ == "__main__":
    root = tk.Tk()
    app = DialogueClassifierApp(root)
    root.mainloop()
