"""
This module provides some utility functions
for the Keycard class.
"""

import copy
from .keycard import Keycard, AccessLevel


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
    size = len(code)
    if size == 1:
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

    return False


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
        if position_num1 == -1:
            break

        after_number_position = position_num1 + 1
        remaining_list = code[after_number_position:]
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


def convert_to_list(u_input: str):
    """This function will convert user input to list so the validation of
    code can be done.

    Parameters:
        u_input (string): The input of user.

    Returns:
        converted_list: The code list from user input."""
    converted_list = []
    for num in u_input.split(" "):
        converted_list.append(int(num))

    return converted_list


def check_access_level(p_access_level: str):
    """This function will check whether access level is green ,blue or red.

    Paarameters:
        p_access_level(str): The access level of the user.

    Returns:
        user_access_level(Enum): The enum of that access level.
        False(bool): if the condistions are not met."""

    if p_access_level.title() == "Green":
        user_access_level = AccessLevel.GREEN
        return user_access_level
    if p_access_level.title() == "Blue":
        user_access_level = AccessLevel.BLUE
        return user_access_level
    if p_access_level.title() == "Red":
        user_access_level = AccessLevel.RED
        return user_access_level
    return False


# lis = [-1, -5, -10, -1100, -900, -1101, -1102]
# test = Keycard(lis, any)
# print(not is_monotone(test))

# python -m src.keycard_utils to run this
