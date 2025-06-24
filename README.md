# python-tools

various python utilities

## delete_with_regex.py

A utility to delete files matching a specified regular expression pattern within a given directory and its subfolders. It includes a dry-run option to preview deletions.

### Usage

```bash
python delete_with_regex.py --path "YOUR_DIRECTORY_PATH" --regex "YOUR_REGEX_PATTERN" [--dry-run]
```

-   `--path`: The root directory to start the search from.
-   `--regex`: The regular expression pattern to match against file names.
-   `--dry-run`: (Optional) If set, the script will only list files that would be deleted without actually deleting them.

### Examples

**1. Delete files like `temp_00_en.png`:**

```bash
python delete_with_regex.py --path "c:\test" --regex "temp_.*\.png" --dry-run
```

**2. Delete files like `00.png`, `01.png`, but not `00_de.png` or `00_en.png`:**

```bash
python delete_with_regex.py --path "YOUR_DIRECTORY_PATH" --regex "^\d+\.png$" --dry-run
```

(Remember to replace `"YOUR_DIRECTORY_PATH"` with your actual path.)
