"""
This module provides some utility functions
for the Keycard class.
"""

import copy
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
    copy_keycard = copy.deepcopy(keycard)

    # Returns the deep copy of keycard
    return copy_keycard


def is_monotone(keycard: Keycard) -> bool:
    """
    Determines whether the keycard's code is monotone, i.e., either constantly
    increasing or decreasing.

    Parameters:
        keycard (Keycard): The keycard object to be examined.

    Returns:
        bool: True if the keycard's code is monotone, False otherwise.
    """
    code = keycard.code
    if len(code) == 1:
        return True

    for i in code:
        number_position = code.index(i)
        if number_position == -1:
            break

        after_number_position = number_position + 1
        remaining_list = code[after_number_position:]
        for j in remaining_list:
            if i in (j - 1, j + 1, j):
                return True

    return not True


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
    code = keycard.code
    size = len(code)
    if size == 1:
        return False
    for num1 in code:
        position_num1 = code.index(num1)
        remaining_list = code[position_num1 + 1 :]
        for num2 in remaining_list:
            if num1 + num2 == secret_num:
                return True

    return False


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


# lis = [-1, -5, -10, -1100, -900, -1101, -1102]
# test = Keycard(lis, any)
# print(not is_monotone(test))

# python -m src.keycard_utils to run this
