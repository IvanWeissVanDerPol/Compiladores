import os
import json
from io import StringIO
from contextlib import redirect_stdout
import pytest
from src.preprocessing.read_files import read_json_file, read_dialogues, display_data_nicely

@pytest.fixture(scope='module')
def setup_files():
    customer_file_path = 'data/customer_dialogues.json'
    employee_file_path = 'data/employee_dialogues.json'
    customer_data = [
        {
            "call_id": "1",
            "customer_id": "cust_001",
            "customer_text": "Hola, buenos días."
        }
    ]
    employee_data = [
        {
            "call_id": "1",
            "employee_id": "emp_001",
            "employee_text": "Buenos días, ¿cómo puedo ayudarle?"
        }
    ]
    os.makedirs('data', exist_ok=True)
    with open(customer_file_path, 'w', encoding='utf-8') as f:
        json.dump(customer_data, f)
    with open(employee_file_path, 'w', encoding='utf-8') as f:
        json.dump(employee_data, f)
    
    yield customer_file_path, employee_file_path, customer_data, employee_data
    
    os.remove(customer_file_path)
    os.remove(employee_file_path)

def test_read_json_file(setup_files):
    customer_file_path, _, customer_data, _ = setup_files
    data = read_json_file(customer_file_path)
    assert isinstance(data, list)
    assert data == customer_data

def test_read_json_file_nonexistent():
    with pytest.raises(FileNotFoundError):
        read_json_file('data/nonexistent.json')

def test_read_json_file_invalid():
    invalid_file_path = 'data/invalid.json'
    with open(invalid_file_path, 'w', encoding='utf-8') as f:
        f.write("Invalid JSON")
    try:
        with pytest.raises(ValueError):
            read_json_file(invalid_file_path)
    finally:
        os.remove(invalid_file_path)

def test_read_dialogues_customer(setup_files):
    _, _, customer_data, _ = setup_files
    data = read_dialogues(file_name='customer_dialogues.json')
    assert isinstance(data, list)
    assert data == customer_data

def test_read_dialogues_employee(setup_files):
    _, _, _, employee_data = setup_files
    data = read_dialogues(file_name='employee_dialogues.json')
    assert isinstance(data, list)
    assert data == employee_data

def test_display_data_nicely(setup_files):
    _, _, customer_data, _ = setup_files
    f = StringIO()
    with redirect_stdout(f):
        display_data_nicely(customer_data, "Customer Dialogues")
    output = f.getvalue()
    assert "Customer Dialogues" in output
    assert "Entry 1" in output
    assert "Hola, buenos días." in output
