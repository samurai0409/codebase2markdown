import os
import argparse
from pathlib import Path

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except UnicodeDecodeError:
        # If UTF-8 fails, try with ISO-8859-1
        with open(file_path, 'r', encoding='iso-8859-1') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file {file_path}: {str(e)}")
        return ""

def get_file_extension(file_path):
    return os.path.splitext(file_path)[1][1:]

def process_directory(directory_path, output_file, ignore_dirs=None, ignore_files=None):
    if ignore_dirs is None:
        ignore_dirs = ['.git', 'node_modules', 'venv', '__pycache__']
    if ignore_files is None:
        ignore_files = ['.gitignore', '.DS_Store']

    try:
        with open(output_file, 'w', encoding='utf-8') as md_file:
            for root, dirs, files in os.walk(directory_path):
                dirs[:] = [d for d in dirs if d not in ignore_dirs]
                
                for file in files:
                    if file in ignore_files:
                        continue
                    
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, directory_path)
                    
                    md_file.write(f"## {relative_path}\n\n")
                    md_file.write("```" + get_file_extension(file_path) + "\n")
                    md_file.write(read_file(file_path))
                    md_file.write("\n```\n\n")
    except IOError as e:
        print(f"Error writing to output file: {str(e)}")
        print("Please make sure you have write permissions for the output directory.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Convert a codebase to a markdown file for Claude knowledge base.")
    parser.add_argument("-d", "--directory", required=True, help="Path to the codebase directory")
    parser.add_argument("-m", "--markdown", required=True, help="Path to the output markdown file")
    parser.add_argument("--ignore-dirs", nargs="*", help="Additional directories to ignore")
    parser.add_argument("--ignore-files", nargs="*", help="Additional files to ignore")
    
    args = parser.parse_args()
    
    ignore_dirs = ['.git', 'node_modules', 'venv', '__pycache__']
    ignore_files = ['.gitignore', '.DS_Store']
    
    if args.ignore_dirs:
        ignore_dirs.extend(args.ignore_dirs)
    if args.ignore_files:
        ignore_files.extend(args.ignore_files)
    
    process_directory(args.directory, args.markdown, ignore_dirs, ignore_files)
    print(f"Markdown file created: {args.markdown}")

if __name__ == "__main__":
    main()
