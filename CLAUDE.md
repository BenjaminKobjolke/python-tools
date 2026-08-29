# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

### Running Python utilities
```bash
# Run the delete_with_regex utility
python delete_with_regex.py --path "YOUR_DIRECTORY_PATH" --regex "YOUR_REGEX_PATTERN" [--dry-run]

# Activate virtual environment (Windows)
activate_environment.bat
```

### Development setup
```bash
# Install dependencies (Windows) - creates venv and installs packages
install.bat

# Manually create/activate virtual environment (Windows)
python -m venv venv
venv\Scripts\activate.bat
```

## Architecture

This repository contains standalone Python utilities designed for file management operations on Windows systems. Currently includes:

- **delete_with_regex.py**: A file deletion utility that uses regular expressions to match and delete files recursively within directories. Implements safety features including dry-run mode and comprehensive logging.

The codebase follows a simple script-based architecture where each utility is self-contained with its own argument parsing and logging setup. Windows batch files provide convenience wrappers for environment management.