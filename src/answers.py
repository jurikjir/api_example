# Description: Module that contains the function that generates answer
# In a separate file for possible future expansions for different
# answer generation algorithms.

from random import choice, randint
import string


def generate_answer() -> str:
    """
    Functions that generates a random string of characters
    from a set of ascii letters, digits and punctuation of 
    length between 10 and 1024 characters.

        Returns:
            str: a random string of characters
    """
    characters = [*string.ascii_letters, *string.digits, *string.punctuation]
    answer = ''.join(choice(characters) for _ in range(randint(10, 1024)))
    return answer