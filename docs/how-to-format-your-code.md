# How to Format Your Code

In this course, we use two tools to help ensure our code is well-formatted and adheres to common Python conventions: Black and Flake8. This guide will help you understand what these tools do and how to use them.

## Black

Black is a Python code formatter. It automatically reformats your code to make it more readable and consistent. It's like having an automated code reviewer that helps you follow Python's PEP 8 style guide.

To use Black in Visual Studio Code:

1. Install the Black extension from the Extensions view (`Ctrl+Shift+X`).
2. Open a Python file in the `src` directory.
3. Right-click anywhere in the file and select `Format Document`. Black will reformat your code.

You can also configure VS Code to automatically format your code every time you save a file. To do this, open the settings (`Ctrl+,`), search for "format on save", and check the box that says "Editor: Format On Save".

## Flake8

Flake8 is a tool for checking your Python code for errors, bugs, stylistic errors, and other problems. It's like having a more thorough automated code reviewer.

To use Flake8 in Visual Studio Code:

1. Install the Python extension from the Extensions view (`Ctrl+Shift+X`).
2. Open a Python file in the `src` directory.
3. If there are any issues with your code, you'll see a number in the bottom status bar indicating how many problems were found. Click on this number to see a list of the problems.
4. Click on a problem to see more details and get suggestions for how to fix it.

## Your Responsibility

For this course, you are responsible for ensuring that all Python code in the `src` directory is formatted correctly and does not produce any warnings or errors from Black or Flake8. Before submitting your assignments, please check your code with these tools and fix any issues they report.

Remember, these tools are here to help you write better code, not to make your life harder. If you're ever unsure about a warning or error, or if you're having trouble fixing a problem, don't hesitate to ask for help.
