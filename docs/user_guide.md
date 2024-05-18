# User Guide

## Introduction
This guide provides instructions on how to use the MNLPTK to analyze and evaluate telephone call interactions. The tool processes dialogues to assess employee performance and customer experience.

## Preparing Data

1. **Format Your Data**:
   Ensure your data is formatted correctly in JSON files with the following structure:

   - `customer_dialogues.json`:
     ```
     [
       {
         "call_id": "1",
         "customer_id": "cust_001",
         "customer_text": "transcript of the customer's dialogue for call 1"
       },
       {
         "call_id": "2",
         "customer_id": "cust_002",
         "customer_text": "transcript of the customer's dialogue for call 2"
       }
     ]
     ```

   - `employee_dialogues.json`:
     ```
     [
       {
         "call_id": "1",
         "employee_id": "emp_001",
         "employee_text": "transcript of the employee's dialogue for call 1"
       },
       {
         "call_id": "2",
         "employee_id": "emp_002",
         "employee_text": "transcript of the employee's dialogue for call 2"
       }
     ]
     ```

2. **Place Data Files**:
   Place your `customer_dialogues.json` and `employee_dialogues.json` files in the `data` directory of the project.

## Running the Tokenizer

1. **Activate the Virtual Environment**:
   Make sure to activate the virtual environment if you have created one.
   ```
source venv/bin/activate # On Windows use venv\Scripts\activate
```
2. **Execute the Main Script**:
Run the main script to start the analysis:
```
python src/main.py
```

3. **Output**:
The results will be saved in an Excel file (`example_output.xlsx`) in the `data` directory. This file includes:
- Evaluation scores for employee performance and customer experience.
- List of tokens justifying the scores.
- Emotional tone analysis.
- Visual analytics (graphs, charts, heatmaps).

## Understanding the Results

### Evaluation Scores
- **Employee Performance Score**: A numerical score indicating the employee's adherence to performance criteria.
- **Customer Experience Score**: A numerical score reflecting the overall customer satisfaction.

### Tokens List
Detailed tokens identified in the conversation that justify the scores.

### Emotional Tone Analysis
Analysis of the emotional content of the conversation, providing insights into the emotional states of both the employee and the customer during the interaction.

### Visual Analytics
Visual representations of the analysis results, including:
- **Graphs**: Visualize various aspects of the conversation analysis.
- **Charts**: Display the distribution and frequency of different token types.
- **Heatmaps**: Show intensity and emotional tone over the course of the conversation.

## Additional Features

### Manual Adjustments
After the initial analysis, you can manually adjust the classification of neutral words to classify them as positive or negative. The system allows for updating token patterns based on user inputs and feedback.

## Troubleshooting

### Common Issues

1. **Missing Data Files**:
Ensure that the `customer_dialogues.json` and `employee_dialogues.json` files are present in the `data` directory.

2. **Incorrect JSON Format**:
Verify that the JSON files are correctly formatted. Use a JSON validator if necessary.

3. **Dependencies Not Installed**:
Make sure all dependencies are installed by running:
pip install -r requirements.txt

4. **Virtual Environment Not Activated**:
Activate the virtual environment if you are using one.

