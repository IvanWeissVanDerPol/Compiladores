import os

class Config:
    """
    Configuration class for the project.
    """

    # Directory paths
    DATA_DIR = os.getenv('DATA_DIR', os.path.join(os.getcwd(), 'data'))
    MODELS_DIR = os.getenv('MODELS_DIR', os.path.join(os.getcwd(), 'models'))
    LOGS_DIR = os.getenv('LOGS_DIR', os.path.join(os.getcwd(), 'logs'))

    # Data files
    DIALOGUES_FILE = os.path.join(DATA_DIR, 'conversations.json')

    # NLP model configurations
    SPACY_MODEL = os.getenv('SPACY_MODEL', 'es_core_news_sm')

    # Logging configurations
    LOG_FILE = os.getenv('LOG_FILE', os.path.join(LOGS_DIR, 'app.log'))
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')

    @classmethod
    def create_directories(cls):
        """
        Creates the necessary directories if they don't exist.
        """
        os.makedirs(cls.DATA_DIR, exist_ok=True)
        os.makedirs(cls.MODELS_DIR, exist_ok=True)
        os.makedirs(cls.LOGS_DIR, exist_ok=True)

if __name__ == "__main__":
    Config.create_directories()
    print(f"Data directory: {Config.DATA_DIR}")
    print(f"Models directory: {Config.MODELS_DIR}")
    print(f"Logs directory: {Config.LOGS_DIR}")
