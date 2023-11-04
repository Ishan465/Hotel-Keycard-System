# How to Start Coding

## Accepting the Assignment in GitHub Classroom

1. **Open the Assignment Link**: Click on the assignment link that you have been provided. This will take you to the assignment page in GitHub Classroom.

2. **Accept the Assignment**: Click on the "Accept this assignment" button. This will create a new repository in your GitHub account for the assignment.

3. **Open the Repository**: Click on the title of the new repository to open it.

## Using GitHub Codespaces

1. **Open the Repository in GitHub Codespaces**
   - Click the "Code" button and then click the "Open with Codespaces" dropdown.
   - Select "New codespace" or choose an existing codespace to open the repository in a web-based development environment.
   - Start coding in the codespace. Your changes will be saved in your forked repository. You can also commit and push your changes from the codespace.

## Working Locally in VSCode

1. **Clone the Repository to Your Local Drive**
   - Click the "Code" button and copy the HTTPS or SSH URL.
   - Open a terminal or command prompt on your local machine.
   - Navigate to the directory where you want to store the local copy of the repository.
   - Run the following command to clone the repository: `git clone <REPOSITORY_URL>`
   - Replace `<REPOSITORY_URL>` with the URL you copied earlier.

2. **Open the Repository in Visual Studio Code**
   - Open Visual Studio Code.
   - Click "Open Folder" or go to File > Open Folder.
   - Navigate to the directory where you cloned the repository, and select the folder containing the repository.
   - Click "Open" to open the repository in Visual Studio Code.

3. **Start Coding**
   - Once the repository is open in Visual Studio Code, you can start coding by opening or creating files in the Explorer panel on the left side.
   - To commit and push your changes to your forked repository, use the Source Control panel (click the Git icon in the left sidebar) to stage, commit, and push your changes.

## Recommended Visual Studio Code Extensions

- To improve your development experience in Visual Studio Code, consider installing the following recommended/required extensions:

  - *Python*: This extension provides support for Python syntax highlighting, IntelliSense, debugging, and more. It was developed and maintained by Microsoft.

  - *Pylance*: Pylance is a Python language server that provides rich functionality like type checking, auto imports, and more.

  - *Pylint*: Pylint is a Python static code analysis tool which looks for programming errors, helps enforcing a coding standard, sniffs for code smells and offers simple refactoring suggestions. It's highly configurable and can be customized to suit your coding style.

  - *Black*: Black is a Python code formatter. This extension integrates Black into VS Code.

  - *Flake8*: Flake8 is a great toolkit for checking your code base against coding style (PEP8), programming errors (like “library imported but unused” and “Undefined name”) and to check cyclomatic complexity.

## Running the Code via GUI

  1. Open the Python file you want to run in Visual Studio Code.
  2. Select the code you want to run.
  3. Right-click the selected code and click "Run Code" in the context menu. Alternatively, you can use the shortcut `Ctrl+Alt+N`.

## Running the Code via Terminal

  1. Open a terminal window.
  2. Navigate to the directory containing the Python file you want to run.
  3. Run the program by executing the following command:

      ```bash
      python <filename>.py
      ```
