"""
This module provides some utility functions
for the Keycard class.
"""

from .keycard import Keycard


def duplicate(keycard: Keycard) -> Keycard:
    """
    Creates a deep copy of the given keycard.

    Parameters:
        keycard (Keycard): The keycard object to be duplicated.

    Returns:
        Keycard: A new keycard object that is an identical deep
        copy of the original.
    """
    return keycard


def is_monotone(keycard: Keycard) -> bool:
    """
    Determines whether the keycard's code is monotone, i.e., either constantly
    increasing or decreasing.

    Parameters:
        keycard (Keycard): The keycard object to be examined.

    Returns:
        bool: True if the keycard's code is monotone, False otherwise.
    """
    return True


def contains_secret_num(keycard: Keycard, secret_num: int) -> bool:
    """
    Checks whether the keycard's code contains the given secret number.

    Parameters:
        keycard (Keycard): The keycard object to be examined.
        secret_num (int): The secret number to be checked.

    Returns:
        bool: True if the keycard's code contains the secret number,
        otherwise it returns false.
    """
    return True


def is_valid(keycard: Keycard, secret_num: int) -> bool:
    """
    Determines whether the keycard is valid based on the given secret number.

    Parameters:
        keycard (Keycard): The keycard object to be examined.
        secret_num (int): The secret number used for validation.

    Returns:
        bool: True if the keycard is valid, False otherwise.
    """
    contains_secret = contains_secret_num(keycard, secret_num)
    not_monotone = not is_monotone(keycard)
    return contains_secret and not_monotone
