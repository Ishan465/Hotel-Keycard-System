"""
This module provides some utility functions
for the Keycard class.
"""

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
    code = [] + keycard.code
    access_level = keycard.access_level

    copy_keycard = Keycard(code, access_level)
    # Returns the deep copy of keycard
    return copy_keycard


def is_increasing(code: list) -> bool:
    """
    This functions checks whether the list is continuosly increasing.

    Parameters:
        code(list): The code of keycard.

    Returns: True if the list is constantly increasing, otherwise False.
    """
    num1 = code[0]  # First creating a variable num1 as first element of list

    for num2 in code:  # Using for loop to iterate in list
        if num2 == num1:
            continue
        if num2 > num1:  # If this conditions are met,
            num1 = num2  # set num1 as num 2 the continue the list
            continue
        # in this logic continue is very important because when the
        # num 2 reaches last element and above two conditions met for
        # whole loop then the loop will end and will return true
        if num2 < num1:
            return False

    return True  # If the conditions are met for whole list then return true


def is_decreasing(code: list) -> bool:
    """
    This functions checks whether the list is continuosly decreasing.

    Parameters:
        code(list): The code of keycard.

    Returns: True if the list is constantly decreasing, otherwise False
    """
    # The logic for this function is similar to is_increasing function
    num1 = code[0]

    for num2 in code:
        if num2 == num1:
            continue
        if num2 < num1:
            num1 = num2
            continue
        if num2 > num1:
            return False

    return True


def is_monotone(keycard: Keycard) -> bool:
    """
    Determines whether the keycard's code is monotone, i.e., either constantly
    increasing or decreasing.

    Parameters:
        keycard (Keycard): The keycard object to be examined.

    Returns:
        bool: True if the keycard's code is monotone, False otherwise.
    """
    code = keycard.code  # create a variable for code attribute of keycard
    size = len(code)  # check the length of list

    if (
        size == 1
    ):  # If it is 1 return true as there are no number to compare with
        return True  # and list of single element is not allowed

    result = is_increasing(code) or is_decreasing(code)
    # The result whether the list is monotonic will depend on is_increasing or
    # is decreasing function

    return result


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
    code = keycard.code  # create a variable for code attribute of keycard
    size = len(code)  # check the length of list

    if size == 1:  # If it is 1 return false as there are no number to add with
        return False  # and list of single element is not allowed

    for num1 in code:
        position_num1 = code.index(num1)  # finding the position of num1
        if position_num1 == -1:  # if it is last element then break as
            break  # we can not find next element which is necessary

        after_number_position = (
            position_num1 + 1
        )  # after number postion of num1
        remaining_list = code[
            after_number_position:
        ]  # created a new list excluding num1
        # I have excluded the num 1 because of the following reason:
        # lets say we have list as [1,3,2,4] and secret num as 2
        # technically the secret num is sum of two digits in a list which in
        # this case is false as we dont have "distinct" numbers that sum to 2
        # but if I included the first iterable number then it would consider
        # first number and return true as 1 will also be repeated in second
        # loop and 1+1 = 2 so i think this logical paradox will be created

        for (
            num2
        ) in (
            remaining_list
        ):  # used nested for loop for num 2 from remaning list
            if (
                num1 + num2 == secret_num
            ):  # if the condition is met then return true
                return True

    return False  # if none of the conditions are met return false


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
    # creates a variable for result of contains secret num
    not_monotone = not is_monotone(keycard)
    # creates a variable for result of not is_monotone
    # as we do not want the list to be monotone
    # if list is not monotone it will result false
    # so not is_monotone will be True

    result = contains_secret and not_monotone
    # result will be and logic of both the functions
    # that means both s
    return result


def convert_to_list(u_input: str):
    """
    Convert user input to list so the validation of code can be done.

    Parameters:
        u_input (string): The input of user.

    Returns:
        converted_list: The code list from user input.
    """
    converted_list = []  # creates an empty list
    for num in u_input.split(
        " "
    ):  # used for loop to iterate through user input seperated by space
        converted_list.append(int(num))  # appends the number to empty list

    return converted_list  # returns converted list


def check_access_level(p_access_level: str):
    """This function will check whether access level is green ,blue or red.

    Paarameters:
        p_access_level(str): The access level of the user.

    Returns:
        user_access_level(Enum): The enum of that access level.
        False(bool): if the condistions are not met."""

    if (
        p_access_level.title() == "Green"
    ):  # if user input is green return accesslevel green
        user_access_level = AccessLevel.GREEN
        return user_access_level
    if (
        p_access_level.title() == "Blue"
    ):  # if user input is blue return accesslevel blue
        user_access_level = AccessLevel.BLUE
        return user_access_level
    if (
        p_access_level.title() == "Red"
    ):  # if user red is green return accesslevel red
        user_access_level = AccessLevel.RED
        return user_access_level
    else:
        user_access_level = AccessLevel.GREEN  # default accesslevel is green
        return user_access_level


# few tests


# lis = [1, 2, 3, 4, 3, 5]
# lis = [1, 1, 1, 2, 3, 4, 1]
# lis = [1, 2, 3, 4, 1,3]
# sec = 5
# test = Keycard(lis, any)
# print(is_monotone(test))
# print(is_increasing(lis))
# print(is_decreasing(lis))
# print(contains_secret_num(test, sec))
# print(is_valid(test, sec))

# python -m src.keycard_utils to run this
