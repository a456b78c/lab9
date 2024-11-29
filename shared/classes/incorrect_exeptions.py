import logging
class IncorrectCharacterException(Exception):
    def __init__(self, message="Incorrect character provided"):
        super().__init__(message)
        logging.error(message)
