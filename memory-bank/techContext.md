# Tech Context

## Technologies Used

-   **Python 3.x:** The primary programming language for all utilities.
-   **Standard Library:**
    -   `argparse`: For parsing command-line arguments.
    -   `os`: For interacting with the operating system, including file system operations (e.g., `os.walk`, `os.remove`, `os.path.join`, `os.path.isdir`).
    -   `re`: For regular expression operations (compiling and matching patterns).
    -   `logging`: For structured output and error reporting.

## Development Setup

-   **Virtual Environments:** Recommended for dependency isolation (`venv`).
-   **Package Management:** `pip` for installing and managing Python packages.
-   **Code Formatting:** `black` for automatic code formatting (as per `.clinerules`).
-   **Linting:** `flake8` for static code analysis and adherence to PEP 8 (as per `.clinerules`).

## Technical Constraints

-   **Python Version:** Utilities are developed for Python 3.x. Compatibility with older Python versions is not guaranteed.
-   **Operating System:** While `os` module functions are generally cross-platform, specific behaviors might vary slightly between Windows, macOS, and Linux. The current environment is Windows.
-   **File System Permissions:** Operations like file deletion are subject to the user's file system permissions. Errors will be logged if permissions are insufficient.

## Dependencies

-   All current utilities primarily rely on Python's standard library, meaning no external `pip` dependencies are strictly required for basic functionality.
-   If future utilities introduce external dependencies, they will be managed via `requirements.txt`.

## Tool Usage Patterns

-   **CLI Execution:** All scripts are designed to be executed directly from the command line.
-   **Modular Scripting:** Each utility is a self-contained script, making it easy to run independently or integrate into larger workflows.
-   **Logging for Feedback:** Extensive use of the `logging` module ensures that users receive clear feedback on script progress, actions taken, and any errors encountered.
-   **Defensive Programming:** Input validation (e.g., checking if a path is a directory) and robust error handling are standard practices.
