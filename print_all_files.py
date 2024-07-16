import os
import sys

def print_file_contents(file_path):
    print(f"\n--- {file_path} ---\n")
    with open(file_path, 'r', encoding='utf-8') as file:
        print(file.read())

def recursive_file_print(directory):
    for root, dirs, files in os.walk(directory):
        if 'venv' in dirs:
            dirs.remove('venv')  # Don't traverse 'venv' directory
        
        for file in files:
            if file.endswith(('.py', '.html', '.md', '.css', '.js')):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, directory)
                print_file_contents(relative_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)
    
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory")
        sys.exit(1)
    
    recursive_file_print(directory)