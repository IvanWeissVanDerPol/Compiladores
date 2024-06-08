# Developer Guide

## Introduction
This guide provides instructions and best practices for developers working on the project. It includes setup instructions, coding standards, and descriptions of key components and their interactions.

## Setup Instructions
1. **Clone the Repository**
  \```bash
  git clone <repository-url>
  cd <repository-name>
  \```

2. **Create and Activate a Virtual Environment**
  \```bash
  python3 -m venv myenv
  source myenv/bin/activate
  \```

3. **Install Dependencies**
  \```bash
  pip install -r requirements.txt
  \```

4. **Download NLTK Data**
  \```python
  import nltk
  nltk.download('punkt')
  nltk.download('stopwords')
  \```

5. **Set Up Environment Variables**
  Configure environment variables for paths and settings in a `.env` file:
  \```plaintext
  DATA_DIR=data
  MODELS_DIR=models
  LOGS_DIR=logs
  SPACY_MODEL=es_core_news_sm
  LOG_FILE=logs/app.log
  LOG_LEVEL=INFO
  \```

## Project Structure
\```plaintext
├── src
│   ├── analysis
│   │   ├── dialogue_act.py
│   │   ├── emotional_tone.py
│   │   ├── scoring.py
│   ├── config.py
│   ├── main.py
│   ├── post_processing
│   │   ├── manual_adjustments.py
│   │   ├── update_patterns.py
│   ├── preprocessing
│   │   ├── correct_spelling.py
│   │   ├── read_files.py
│   │   ├── remove_stop_words.py
│   ├── tokenization
│   │   ├── define_tokens.py
│   │   ├── lexical_analysis.py
│   │   ├── tokenizer.py
│   ├── utils
│   │   ├── co_reference_resolution.py
│   │   ├── error_handling.py
│   │   ├── fallback.py
│   ├── visualization
│   │   ├── generate_charts.py
│   │   ├── generate_graphs.py
│   │   ├── generate_heatmaps.py
├── tests
│   ├── test_read_files.py
│   ├── test_remove_stop_words.py
│   ├── test_correct_spelling.py
│   ├── test_define_tokens.py
│   ├── test_lexical_analysis.py
│   ├── test_tokenizer.py
│   ├── test_dialogue_act.py
│   ├── test_emotional_tone.py
│   ├── test_scoring.py
│   ├── test_manual_adjustments.py
│   ├── test_update_patterns.py
│   ├── test_co_reference_resolution.py
│   ├── test_error_handling.py
│   ├── test_fallback.py
│   ├── test_generate_charts.py
│   ├── test_generate_graphs.py
│   ├── test_generate_heatmaps.py
│   ├── test_config.py
│   ├── test_main.py
├── requirements.txt
├── developer_guide.md
├── overview.md
├── user_guide.md
└── README.md
\```
## ## Coding Standards
- Follow PEP 8 guidelines for Python code.
- Use meaningful variable and function names.
- Write docstrings for all modules, classes, and functions.
- Ensure code is well-documented and commented.

## Key Components
- `src/config.py`: Contains configuration settings for the project.
- `src/main.py`: Main entry point of the application.
- `src/analysis`: Contains modules for analyzing dialogue acts, emotional tone, and scoring dialogue quality.
- `src/post_processing`: Contains modules for applying manual adjustments and updating dialogue patterns.
- `src/preprocessing`: Contains modules for reading files, correcting spelling, and removing stop words.
- `src/tokenization`: Contains modules for defining tokens, performing lexical analysis, and tokenizing text.
- `src/utils`: Contains utility modules for error handling, fallback responses, and co-reference resolution.
- `src/visualization`: Contains modules for generating charts, graphs, and heatmaps.

## Testing
- Unit tests are located in the `tests` directory.
- Run tests using pytest:
    ```bash
    pytest
    ```

## Logging
- Logging configuration is set in `src/config.py`.
- Logs are saved in the `logs` directory.

## Contributions
- Fork the repository and create a new branch for your feature or bugfix.
- Submit a pull request with a clear description of your changes.
- Ensure all tests pass before submitting the pull request.