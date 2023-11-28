# you will need imports
# python -m src.story to run this
from .keycard_utils import is_valid
from .keycard import Keycard, AccessLevel

WELCOME_MESSAGE = """Welcome to the Hotel Blue Moon. For security reasons we
provide keycards instead of keys. Don't worry if you lose your keycard
as we always create a deep copy of keycard. However this doesn't
mean that you become careless. Type help to get more info of keycards.
As you are our new customer you need to create a new keycard. 
The keycard should contain less than 16 numbers.
\nType help to know more about keycard. Type requirements to know the\
requirements of your code
"""

HELP_MESSAGE = """ A keycard is a security token that grants you access
through electrically-powered doors. These systems require a keycard reader
(installed on the door) and you gain access by either tapping your card on
 the reader (proximity reader), swiping it (swipe reader), or inserting it.
Majority of the time you have to enter the code for first time and then you 
may use other options. In our hotel different we provide different types of
keycards according to the type of room.
"""
REQUIREMENTS = """Below are the requirements of your keycard
* Your code must contain numbers only.
* The length of code must be between 1 and 16
* Your code must not be monotone i.e 1,2,3
* Your secret number must be a single number
* Your secret number should be addition of any 2 numbers in code
* Negative numbers are allowed
* Currently you can choose access level from green, blue, red
  but in the near future we may provide more options 
* Once your code is valid your code will be highlighted with your
  access level color.
"""

ADVICE = """Always remember your code. Do not share it with anyone.
 You can take photo of the code and your secret number given below.
 Remember that your code will glow with the colour of your access level"""


def convert_to_list(u_input: str):
    """This function will convert user input to list so the validation of
    code can be done"""
    converted_list = []
    for num in u_input.split(" "):
        converted_list.append(int(num))

    return converted_list


def check_access_level(p_access_level: str):
    """This function will check whether access level is green ,blue or red"""

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


if __name__ == "__main__":
    print(WELCOME_MESSAGE)
    while True:
        try:
            user_input = input(
                "\nPlease enter your preferred keycard code\
(seperated by space): "
            )
            if user_input.lower() == "help":
                print(HELP_MESSAGE)
                continue
            if user_input.lower() == "requirements":
                print(REQUIREMENTS)
                continue
            converted_code = convert_to_list(user_input)
            secret_num = int(
                input("Please enter your preferred secret number: ")
            )
            u_access_level = input(
                "Please enter your preferred access level: "
            )

            check_level = check_access_level(u_access_level)

            if check_level:
                print("Checking your input with our database...")
            else:
                print("Please enter correct access level(green, blue, red)")
                continue

            ENTER = input("Press 'Enter' key to continue ")

            user_keycard = Keycard(
                code=converted_code, access_level=check_level
            )

            if is_valid(user_keycard, secret_num):
                print("\nYour code is valid. You can start using your keycard")
                print(ADVICE)
                print(f"Your code: {user_keycard}")
                print(f"Your secret number: {secret_num}")

            else:
                print("\nERROR!!! Code is not valid. Entry not allowed")

            break
        except ValueError:
            print(
                "\nERROR!!! Please enter only numbers and code should have\
length less than 16"
            )
            continue
