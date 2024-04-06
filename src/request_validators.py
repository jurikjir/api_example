# Description: This file contains functions that validate the request parameters.


def valid_id_length(id: str) -> bool:
    """
    A function that checks if the length of the id is greater than 0.

        Parameters:
            id (str): a unique identifier
        
        Returns:
            bool: True if the length of the id is greater than 0, False otherwise
    """
    return False if len(id) == 0 else True


def valid_question_max_length(question: str) -> bool:
    """
    A function that checks if the length of the question is less than or equal to 512.

        Parameters:
            question (str): a question
        
        Returns:
            bool: True if the length of the question is less than or equal to 512, False otherwise
    """
    return False if len(question) > 512 else True


def valid_question_min_length(question: str) -> bool:
    """
    A function that checks if the length of the question is greater than 0.
    
        Parameters:
            question (str): a question

        Returns:
            bool: True if the length of the question is greater than 0, False otherwise
    """
    return False if len(question) == 0 else True

