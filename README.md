# Codebase to Markdown Converter: User Guide

This documentation explains how to use the updated Codebase to Markdown Converter, which consists of two main components:
1. A Python script (`codebase_to_markdown.py`) that converts a codebase into a markdown file.
2. An HTML helper (`codebase_to_markdown_helper.html`) that generates the command to run the Python script.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Python Script: codebase_to_markdown.py](#python-script-codebase_to_markdownpy)
   - [Usage](#usage)
   - [Arguments](#arguments)
   - [Examples](#examples)
3. [HTML Helper: codebase_to_markdown_helper.html](#html-helper-codebase_to_markdown_helperhtml)
   - [How to Use](#how-to-use)
4. [Workflow](#workflow)
5. [Troubleshooting](#troubleshooting)

## Prerequisites
- Python 3.6 or higher installed on your system
- Basic familiarity with using the command line
- Write permissions for the output directory where you want to save the markdown file

## Python Script: codebase_to_markdown.py

### Usage
The script is run from the command line with the following basic syntax:

```
python codebase_to_markdown.py -d <codebase_directory> -m <output_markdown_file>
```

### Arguments
- `-d` or `--directory`: (Required) Path to the codebase directory you want to convert.
- `-m` or `--markdown`: (Required) Path where you want to save the output markdown file.
- `--ignore-dirs`: (Optional) Additional directories to ignore, space-separated.
- `--ignore-files`: (Optional) Additional files to ignore, space-separated.

### Examples
1. Basic usage:
   ```
   python codebase_to_markdown.py -d C:\Projects\MyApp -m C:\Output\myapp_docs.md
   ```

2. Ignoring additional directories and files:
   ```
   python codebase_to_markdown.py -d C:\Projects\MyApp -m C:\Output\myapp_docs.md --ignore-dirs build dist --ignore-files README.md LICENSE
   ```

## HTML Helper: codebase_to_markdown_helper.html

### How to Use
1. Open the `codebase_to_markdown_helper.html` file in a web browser.
2. Fill in the following fields:
   - Path to codebase_to_markdown.py: The full path to where you saved the Python script.
   - Path to your codebase: The full path to the codebase you want to convert.
   - Path for output markdown file: The full path where you want to save the resulting markdown file.
   - Directories to ignore: (Optional) Comma-separated list of additional directories to ignore.
   - Files to ignore: (Optional) Comma-separated list of additional files to ignore.
3. Click the "Generate Command" button.
4. Copy the generated command from the box that appears at the bottom of the page.

## Workflow
1. Save the Python script (`codebase_to_markdown.py`) and the HTML helper (`codebase_to_markdown_helper.html`) to your local machine.
2. Open the HTML helper in a web browser.
3. Fill in the required information in the HTML helper.
4. Generate the command using the HTML helper.
5. Copy the generated command.
6. Open a terminal or command prompt.
7. Paste and run the command in the terminal.
8. The script will generate a markdown file at the specified output location.

## Troubleshooting

### Permission Issues
- Ensure you have read permissions for the codebase directory and all its subdirectories and files.
- Make sure you have write permissions for the output directory where you want to save the markdown file.
- If you encounter a "Permission denied" error, try running the command prompt or terminal as an administrator.

### Encoding Issues
- The script now attempts to read files with UTF-8 encoding first, and if that fails, it tries ISO-8859-1 encoding.
- If you still encounter encoding errors, please check if your files use a different encoding and consider converting them to UTF-8.

### Path Issues
- Use forward slashes (/) or escaped backslashes (\\) in file paths to avoid issues.
- If a path contains spaces, ensure it's enclosed in quotes in the command.

### Large Codebases
- For very large codebases, the script may take some time to run. Be patient and allow it to complete.
- Ensure you have enough disk space at the output location for the generated markdown file.

### Other Issues
- If you encounter unexpected errors, check the error message printed by the script. It should provide more information about what went wrong.
- Verify that all paths are correct and that the files and directories exist.
- Make sure you're using Python 3.6 or higher.

If you continue to experience issues not covered in this troubleshooting guide, please contact the script's maintainer or seek help in relevant programming forums, providing the exact error message and steps to reproduce the issue.

Remember to always verify the contents of the generated markdown file to ensure all necessary code has been included and no sensitive information has been unintentionally captured.
