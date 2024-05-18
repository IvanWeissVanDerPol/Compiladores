# Developer Guide

## Introduction
This guide provides an overview for developers to understand the MNLPTK codebase and contribute to its development. The project is organized to ensure modularity and ease of maintenance.

## Project Structure

- **data/**: Contains JSON files for customer and employee dialogues, and an example output Excel file.
- **src/**: Contains all source code for the project.
  - **main.py**: Entry point of the application.
  - **config.py**: Configuration settings.
  - **preprocessing/**: Modules for initial data preprocessing.
  - **tokenization/**: Modules for tokenization.
  - **analysis/**: Modules for analyzing tokenized data.
  - **utils/**: Utility functions and helpers.
  - **visualization/**: Modules for generating visual analytics.
  - **post_processing/**: Modules for post-processing tasks.
- **docs/**: Project documentation.
- **requirements.txt**: List of dependencies.

## Modules

### Preprocessing
- **read_files.py**: Functions to read and parse input JSON files.
- **remove_stop_words.py**: Functions to remove stop words from the text.
- **correct_spelling.py**: Functions to correct spelling errors in the text.

### Tokenization
- **tokenizer.py**: Main tokenizer class.
- **define_tokens.py**: Definitions of various tokens used for evaluation.
- **lexical_analysis.py**: Functions for lexical analysis.

### Analysis
- **emotional_tone.py**: Functions to detect the emotional tone of the conversation.
- **dialogue_act.py**: Functions to recognize dialogue acts.
- **scoring.py**: Functions to calculate scores based on tokens and emotional analysis.

### Utils
- **co_reference_resolution.py**: Functions to resolve co-references.
- **error_handling.py**: Functions to handle and correct errors.
- **fallback.py**: Fallback strategies for unknown tokens or unexpected input.

### Visualization
- **generate_charts.py**: Functions to create charts.
- **generate_graphs.py**: Functions to create graphs.
- **generate_heatmaps.py**: Functions to create heatmaps.

### Post-Processing
- **manual_adjustments.py**: Allows for manual adjustments of token classifications.
- **update_patterns.py**: Updates token patterns based on feedback and new data.

## Contribution Guidelines

1. **Fork the Repository**
2. **Create a Feature Branch**
3. **Commit Your Changes**
4. **Push to the Branch**
5. **Create a Pull Request**

Ensure your code follows the project's coding standards and includes appropriate documentation and tests.
