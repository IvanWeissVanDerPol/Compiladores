def fallback_response() -> str:
    """
    Returns a fallback response when the system cannot handle the request.
    
    :return: A fallback response message.
    """
    return "Lo siento, no entendí eso. ¿Puedes reformularlo?"

if __name__ == "__main__":
    # Example usage
    print(fallback_response())
