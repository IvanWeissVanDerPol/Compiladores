
### `user_guide.md`

```markdown
# User Guide

## Introduction
This guide provides instructions for users on how to set up, run, and interpret the outputs of the project.

## Setup Instructions
1. **Clone the Repository**
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2. **Create and Activate a Virtual Environment**
    ```bash
    python3 -m venv myenv
    source myenv/bin/activate
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Download NLTK Data**
    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    ```

5. **Set Up Environment Variables**
    Create a `.env` file in the project root and add the following variables:
    ```plaintext
    DATA_DIR=data
    MODELS_DIR=models
    LOGS_DIR=logs
    SPACY_MODEL=es_core_news_sm
    LOG_FILE=logs/app.log
    LOG_LEVEL=INFO
    ```

## Running the Application
To run the main script and start the analysis, execute:
```bash
python src/main.py

Input Data
Ensure that your input data is in the data directory.
The expected format is JSON files with dialogues.
Output
The results of the analysis, including identified dialogue acts, emotional tones, and quality scores, are logged