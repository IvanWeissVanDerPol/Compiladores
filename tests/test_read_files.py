import unittest
import os
import json
from io import StringIO
from contextlib import redirect_stdout
from src.preprocessing.read_files import read_json_file, read_dialogues, display_data_nicely

class TestReadFiles(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.customer_file_path = 'data/customer_dialogues.json'
        cls.employee_file_path = 'data/employee_dialogues.json'
        cls.customer_data = [
            {
                "call_id": "1",
                "customer_id": "cust_001",
                "customer_text": "Hola, buenos días."
            }
        ]
        cls.employee_data = [
            {
                "call_id": "1",
                "employee_id": "emp_001",
                "employee_text": "Buenos días, ¿cómo puedo ayudarle?"
            }
        ]
        os.makedirs('data', exist_ok=True)
        with open(cls.customer_file_path, 'w', encoding='utf-8') as f:
            json.dump(cls.customer_data, f)
        with open(cls.employee_file_path, 'w', encoding='utf-8') as f:
            json.dump(cls.employee_data, f)

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.customer_file_path)
        os.remove(cls.employee_file_path)

    def test_read_json_file(self):
        customer_data = read_json_file(self.customer_file_path)
        self.assertIsInstance(customer_data, list)
        self.assertEqual(customer_data, self.customer_data)

    def test_read_json_file_nonexistent(self):
        with self.assertRaises(FileNotFoundError):
            read_json_file('data/nonexistent.json')

    def test_read_json_file_invalid(self):
        invalid_file_path = 'data/invalid.json'
        with open(invalid_file_path, 'w', encoding='utf-8') as f:
            f.write("Invalid JSON")
        try:
            with self.assertRaises(ValueError):
                read_json_file(invalid_file_path)
        finally:
            os.remove(invalid_file_path)

    def test_read_dialogues_customer(self):
        customer_data = read_dialogues(file_name='customer_dialogues.json')
        self.assertIsInstance(customer_data, list)
        self.assertEqual(customer_data, self.customer_data)

    def test_read_dialogues_employee(self):
        employee_data = read_dialogues(file_name='employee_dialogues.json')
        self.assertIsInstance(employee_data, list)
        self.assertEqual(employee_data, self.employee_data)

    def test_display_data_nicely(self):
        f = StringIO()
        with redirect_stdout(f):
            display_data_nicely(self.customer_data, "Customer Dialogues")
        output = f.getvalue()
        self.assertIn("Customer Dialogues", output)
        self.assertIn("Entry 1", output)
        self.assertIn("Hola, buenos días.", output)

if __name__ == '__main__':
    unittest.main()
