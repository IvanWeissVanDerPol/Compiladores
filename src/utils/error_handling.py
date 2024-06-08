import logging

def log_error(error_message: str) -> None:
    """
    Logs an error message.

    :param error_message: The error message to log.
    """
    logging.error(error_message)

def handle_error(error_message: str) -> None:
    """
    Handles an error by logging it and potentially taking other actions.

    :param error_message: The error message to handle.
    """
    log_error(error_message)
    # Additional error handling actions can be added here.

if __name__ == "__main__":
    # Example usage
    try:
        raise ValueError("An example error")
    except ValueError as e:
        handle_error(str(e))
