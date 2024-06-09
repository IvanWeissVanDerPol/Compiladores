import json

def load_data():
    with open('employee_dialogues.json', 'r', encoding='utf-8') as f:
        employee_dialogues = json.load(f)
    with open('customer_dialogues.json', 'r', encoding='utf-8') as f:
        customer_dialogues = json.load(f)
    return employee_dialogues, customer_dialogues

employee_dialogues, customer_dialogues = load_data()
