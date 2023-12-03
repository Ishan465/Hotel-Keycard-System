"""This is the module for using all the functions and creating a program"""

# python -m src.story to run this
from .keycard_utils import is_valid, convert_to_list, check_access_level
from .keycard import Keycard

WELCOME_MESSAGE = """Welcome to the Hotel Blue Moon. For security reasons we
provide keycards instead of keys. Don't worry if you lose your keycard
as we always create a deep copy of keycard. However this doesn't
mean that you become careless. Type help to get more info of keycards.
As you are our new customer you need to create a new keycard.
The keycard should contain less than 16 numbers.
\nType help to know more about keycard. Type requirements to know the\
requirements of your code. If you started the process of creating keycard
and then changed mind to stay in our hotel you can press 'q' to exit the
program
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
* Your code must not be monotone which means that it should not be
 continuosly increasing or decreasing
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
            if user_input.lower() == "q":
                print("Thanks for your visit have a great day")
                break

            converted_code = convert_to_list(user_input)

            secret_num = int(
                input("Please enter your preferred secret number: ")
            )

            u_access_level = input(
                "Please enter your preferred access level(green, blue, red)\
(default is green): "
            )

            check_level = check_access_level(u_access_level)

            print('Checking your code with our database...')
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
                print(
                    "\nERROR!!! Code not valid. Please review the requirements"
                )

            break
        except ValueError:
            print(
                "\nERROR!!! Code not valid. Please review the requirements"
            )
            continue

# python -m src.story to run this
