import argparse
import os
import re
import logging

def setup_logging():
    """Sets up basic logging for the script."""
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def delete_files_with_regex(path: str, regex: str, dry_run: bool):
    """
    Deletes files matching a regex pattern in a given path, including subfolders.

    Args:
        path (str): The root directory to start the search from.
        regex (str): The regular expression pattern to match against file names.
        dry_run (bool): If True, only lists files that would be deleted without
                        actually deleting them.
    """
    setup_logging()
    logging.info(f"Starting file deletion utility in '{'dry-run' if dry_run else 'actual'}' mode.")
    logging.info(f"Searching in: {path}")
    logging.info(f"Matching regex: {regex}")

    try:
        compiled_regex = re.compile(regex)
    except re.error as e:
        logging.error(f"Invalid regex pattern '{regex}': {e}")
        return

    if not os.path.isdir(path):
        logging.error(f"Error: Path '{path}' is not a valid directory.")
        return

    files_found = 0
    files_deleted = 0

    for root, _, files in os.walk(path):
        for file_name in files:
            if compiled_regex.match(file_name):
                full_path = os.path.join(root, file_name)
                files_found += 1
                if dry_run:
                    logging.info(f"DRY RUN: Would delete '{full_path}'")
                else:
                    try:
                        os.remove(full_path)
                        logging.info(f"Deleted '{full_path}'")
                        files_deleted += 1
                    except OSError as e:
                        logging.error(f"Error deleting '{full_path}': {e}")
    
    if dry_run:
        logging.info(f"Dry run complete. Found {files_found} file(s) matching the regex.")
    else:
        logging.info(f"Deletion complete. Found {files_found} file(s) matching the regex, deleted {files_deleted}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Delete files matching a regex pattern in a specified directory and its subfolders."
    )
    parser.add_argument(
        "--path",
        type=str,
        required=True,
        help="The root directory to start the search from."
    )
    parser.add_argument(
        "--regex",
        type=str,
        required=True,
        help="The regular expression pattern to match against file names."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="If set, the script will only list files that would be deleted without actually deleting them."
    )

    args = parser.parse_args()
    delete_files_with_regex(args.path, args.regex, args.dry_run)
