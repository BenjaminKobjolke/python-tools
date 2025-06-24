# System Patterns

## System Architecture

The `python-tools` project follows a simple, flat architecture where each utility is largely independent. There is no complex inter-module communication or service-oriented design.

```mermaid
graph TD
    A[User] --> B[Command Line Interface];
    B --> C{delete_with_regex.py};
    C --> D[os.walk (File System Traversal)];
    C --> E[re (Regex Matching)];
    C --> F[os.remove (File Deletion)];
    C --> G[logging (Output)];
```

## Key Technical Decisions

-   **Modularity:** Each utility is designed to be self-contained, minimizing dependencies between different scripts. This allows for easy addition, removal, or modification of individual tools without affecting others.
-   **Command-Line Interface (CLI):** `argparse` is used for robust and user-friendly command-line argument parsing, ensuring consistent input handling across utilities.
-   **Standard Library Focus:** Prioritize Python's standard library (`os`, `re`, `logging`, `argparse`) to reduce external dependencies and simplify deployment.
-   **Dry-Run Mechanism:** For any potentially destructive operation, a `--dry-run` flag is implemented to allow users to preview changes before execution, enhancing safety.

## Design Patterns in Use

-   **Command Pattern (Implicit):** Each script acts as a command, encapsulating a specific action (e.g., `delete_files_with_regex`).
-   **Strategy Pattern (Implicit):** The `dry_run` flag can be seen as a simple form of strategy, where the execution logic changes based on this flag (logging vs. actual deletion).

## Component Relationships

-   **`delete_with_regex.py`:**
    -   Relies on `argparse` for CLI argument handling.
    -   Uses `os.walk` to interact with the file system for directory traversal.
    -   Employs `re` for regular expression matching of file names.
    -   Utilizes `os.remove` for file deletion.
    -   Integrates `logging` for structured output and error reporting.

## Critical Implementation Paths

-   **File Traversal and Matching:** The `os.walk` combined with `re.compile` and `re.match` is a critical path for efficiently identifying target files.
-   **Error Handling for File Operations:** Robust `try-except` blocks around `os.remove` are crucial to prevent script crashes due to permission issues or other file system errors.
-   **Dry-Run Logic:** The conditional execution based on the `dry_run` flag is essential for the safety and usability of destructive utilities.
