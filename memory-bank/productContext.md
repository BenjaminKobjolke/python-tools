# Product Context

## Purpose

The `python-tools` project aims to provide a centralized repository for small, focused Python scripts that address common development and system administration tasks. This reduces the need for repetitive manual operations and promotes consistency across various workflows.

## Problems Solved

-   **Repetitive Tasks:** Automates tasks like file management (e.g., deleting files by regex), data manipulation, and system interactions.
-   **Inconsistency:** Provides standardized, tested utilities, reducing variations in how similar tasks are performed.
-   **Time Saving:** Speeds up development and operational tasks by offering ready-to-use scripts.

## How it Should Work

-   **Command-Line Interface:** All utilities should be runnable directly from the command line with clear, self-documenting arguments.
-   **Modularity:** Each utility should be a standalone script or a clearly defined module within the project.
-   **User Feedback:** Provide informative output, especially for destructive operations (e.g., dry-run mode, logging of actions).
-   **Error Handling:** Gracefully handle common errors (e.g., invalid paths, permission issues) and provide clear error messages.

## User Experience Goals

-   **Simplicity:** Easy to understand and use, even for users with basic Python knowledge.
-   **Reliability:** Utilities should perform their intended function consistently and without unexpected side effects.
-   **Safety:** Destructive operations must include safeguards like dry-run options.
-   **Discoverability:** Clear documentation (e.g., `README.md`, script help messages) to help users understand available tools and their usage.
