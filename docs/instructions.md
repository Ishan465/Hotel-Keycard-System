# Capstone Project

## Value (%)

This assignment is worth 20% of your course grade.

## Background

In the context of a larger program that simulates security access systems, we have created a `Keycard` class. This class represents a keycard used for access control and contains two main attributes:

- **code**: A list of integers representing the keycard's unique code.
- **access_level**: An enum that defines the access level of the keycard. It can be one of three values: Green, Blue, or Red.

As part of this project, you will need to complete functions that act on the `code` portion of the `Keycard` class. Here's an overview of the functions you'll be working on:

- **duplicate**: Creates a deep copy of a given keycard, preserving the code and access level.
- **is_monotone**: Determines if a keycard's code is monotone. We don't want users selecting simple code combinations so a monotone code should be considered invalid. A code is considered monotone if it is entirely non-increasing or entirely non-decreasing (e.g., [1, 2, 3, 4]) or decreasing (e.g., [9, 8, 7, 6]). The code [1, 1, 2, 2, 3, 4, 5, 5] would also be considered monotone. Non-monotone examples include [1, 3, 2, 4] and [5, 3, 4, 2].
- **contains_secret_number**: Checks if two elements of the keycard's code sum to a given secret number. This is a security measure to test for forged keycards. A keycard code should be considered valid only if this criteria is met. For example, if the secret number is 5, a code containing [1, 4] or [2, 3] would satisfy the condition but [1, 6, 7, 8] would not.

Finally, you'll be incorporating these functions into a creative narrative in the `story.py` file. Consider the context of the larger program and the role of keycards in a security system as you craft your story. Your narrative should prompt the user to select a keycard code and access level, and then unfold in a way that logically incorporates the above functions.

## Task

### Implementing `duplicate`

You are to implement a function `duplicate(keycard: Keycard) -> Keycard` that takes a `Keycard` object and returns a deep copy of it. This function will be used to create an identical copy of a keycard with all the same properties and access levels.

### Implementing `is_monotone`

Create a function `is_monotone(keycard: Keycard) -> bool` that takes a `Keycard` object and returns `True` if the keycard's code is monotone, i.e., entirely non-increasing or entirely non-decreasing. Otherwise, it returns `False`.

### Implementing `contains_secret_num`

Develop a function `contains_secret_num(keycard: Keycard, secret_num: int) -> bool` that takes a `Keycard` object and a secret number. It returns `True` if any two elements of the keycard's code sum to be equal to the secret number, otherwise, it returns `False`.

### Story Development

Create a story in the file `story.py` that revolves around the concept of keycards in a fictional setting. Prompt the user to enter their preferred keycard code and access level. Weave a narrative that creatively incorporates the above functions and the `is_valid` function within the context of the story.

## How to Complete This Assessment

1. Familiarize yourself with the `Keycard` class.
2. Begin by implementing the `duplicate`, `is_monotone`, and `contains_secret_num` functions in the `keycard_utils.py` file. Make sure to follow the specifications provided in the Task section.
3. In the `story.py` file, write the narrative for the story. Provide the user with some interesting prompts (be sure to handle exceptions related to user input) that allow them to use all the functions you have created.
4. Incorporate prompts to allow the user to enter their preferred keycard code and access level. Validate the user input and handle any edge cases.
5. Thoughtfully weave the `duplicate`, `is_monotone`, `contains_secret_num` and `is_valid` functions into the story to create a cohesive and engaging experience.
6. Ensure that all functions are implemented according to the specifications, and that the story provides a clear and interesting narrative.

## How to Submit Your Assessment

To submit your assessment via GitHub Classroom, follow these steps:

1. **Update Your Local Repository**
   - Ensure your local or codespace repository is up-to-date with the GitHub repository. You can do this by performing a pull request. In Visual Studio Code, you can click on the "..." button in the Source Control panel and then click "Pull".

2. **Commit Your Changes**
   - Make sure all your changes are committed to your codespace/local repository. You can do this in Visual Studio Code by going to the Source Control panel (click the Git icon in the left sidebar), staging your changes, and then committing them with a descriptive message.

3. **Push Your Changes**
   - Push your committed changes to your repository on GitHub. You can do this in Visual Studio Code by clicking the "..." button in the Source Control panel and then clicking "Push".

4. **Submit Your Repository in GitHub Classroom**
   - Go to the assignment page in GitHub Classroom.
   - Click the "Submit assignment" button.
   - In the "Submit your assignment" dialog, select the "Your work" tab.
   - Click the "Select repository" dropdown and select your forked repository.
   - Click the "Submit" button to submit your assignment.

Remember to submit a link to the GitHub repo containing your code through Moodle as well.

## Grading Rubric

### Results (70%)

- Your grade for this component is based on how many test cases your code passes. In most cases, if your code passes all test cases, you get the full 70%. You will be penalized if your screenshot output is incorrect/missing even if all the tests pass or if there are other major issues with your code.

### Class/Method/Variable Naming (10%)

| Points | Description                                                                                              |
| :----: | -------------------------------------------------------------------------------------------------------- |
|   1    | Excellent: Consistent, meaningful, and clear naming conventions for all classes, methods, and variables. |
|  0.75  | Good: Mostly consistent and meaningful naming conventions; minor inconsistencies or unclear names.       |
|  0.5   | Needs Improvement: Inconsistent naming conventions; some unclear or confusing names.                     |
|   0    | Poor: No clear naming conventions; many unclear or confusing names.                                      |

### Comments/Documentation (10%)

| Points | Description                                                                                                    |
| :----: | -------------------------------------------------------------------------------------------------------------- |
|   1    | Excellent: Comprehensive comments and documentation; easy to understand the purpose and functionality of code. |
|  0.5   | Needs Improvement: Some comments and documentation, but lacking clarity or detail in certain areas.            |
|   0    | Poor: No comments or documentation; difficult to understand the purpose and functionality of the code.         |

### Formatting (10%)

| Points | Description                                                      |
| :----: | ---------------------------------------------------------------- |
|   1    | No formatting is required during the formatting workflow.        |
|  0.25  | Minimal formatting is required during the formatting workflow.   |
|   0    | Extensive formatting is required during the formatting workflow. |

### Presentation

Your final grade will be scaled by the quality of your presentation and the creativity surrounding the story aspect of the project. Typically, you should receive a grade equivalent to your score based on the rubric elements above. However, if you miss your presentation, your grade will be halved so you will receive at most 50%. Other aspects of your presentation that can reduce your final grade are the following:

- Minimal effort put into the story component.
- You cannot clearly explain your code and rationale behind your design choices.
- You use advanced concepts that have not been introduced in class and cannot thoroughly explain how they work.

On the other hand, factors that will allow your presentation to scale your grade upwards include the following:

- Fun and creative story elements.
- You are able to explain your code clearly and concisely.
- Proper exception handling in `story.py`.
  
If you have any questions about this aspect of the grading, please ask.
