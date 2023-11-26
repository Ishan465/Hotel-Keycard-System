# you will need imports
# pylint: disable=import-error
from keycard_utils import is_valid
from keycard import Keycard

WELCOME_MESSAGE = """Welcome to the hotel Blue Moon. For security reasons we
provide keycards instead of keys. Don't worry if you lose your keycard
as we always create a deep copy of keycard. However this doesn't
mean that you become careless. Type help to get more info of keycards.
As you are our new customer you need to create a new keycard. 
The keycard should contain less than 16 numbers. Type help to know more
about keycard.
"""

HELP_MESSAGE = """ A keycard is a security token that grants you access
through electrically-powered doors. These systems require a keycard reader
(installed on the door) and you gain access by either tapping your card on
 the reader (proximity reader), swiping it (swipe reader), or inserting it.
Majority of the time you have to enter the code for first time and then you 
may use other options. In our hotel different we provide different types of
keycards according to the type of room.
"""


def convert_to_list(u_input):
    """This function will convert user input to list so the validation of
    code can be done"""
    converted_list = []
    for num in u_input.split(" "):
        converted_list.append(int(num))

    return converted_list


if __name__ == "__main__":
    print(WELCOME_MESSAGE)
    while True:
        try:
            user_input = input(
                "\nPlease enter your keycard code\
(seperated by space): "
            )
            if user_input.lower() == "help":
                print(HELP_MESSAGE)
                continue
            u_code = convert_to_list(user_input)
            secret_num = input("Please enter your secret num: ")
            secret_num = int(secret_num)
            """
            access_level = input('Please enter your access level: ')
            if (access_level.title() == 'Green') or\
               (access_level.title() == 'Blue') or\
               (access_level.title() == 'Blue'):
                print('checking your input with database')
            else:
                print('Please enter correct access level')
                continue
            """
            user_keycard = Keycard(code=u_code)

            if is_valid(user_keycard, secret_num):
                print("Your code is valid")
            else:
                print("code is not valid")

            print(u_code)
            break
        except ValueError:
            print("\nERROR!!! Please enter only numbers")
            continue
