import os
import sys
import re

def sanitize_filename(filename):
    # Remove invalid characters for filenames
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

def split_txt_file(input_file):
    # Get the directory and filename without extension
    directory = os.path.dirname(input_file)

    # Open the input file and read lines
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Write each line to a separate .txt file
    for i, line in enumerate(lines):
        # Remove newline character and sanitize the filename
        sanitized_line = sanitize_filename(line.strip())
        # Create a filename for each line
        output_file = os.path.join(directory, f"{sanitized_line}.txt")
        with open(output_file, 'w', encoding='utf-8') as out_file:
            out_file.write(line)

    print(f"Split {len(lines)} lines into separate files in folder: {directory}")

if __name__ == "__main__":
    # Check if a file was dragged onto the script
    if len(sys.argv) != 2:
        print("Usage: Drag and drop a .txt file onto this script.")
        sys.exit(1)

    input_file_path = sys.argv[1]

    if not os.path.isfile(input_file_path) or not input_file_path.endswith('.txt'):
        print("Please provide a valid .txt file.")
        sys.exit(1)

    split_txt_file(input_file_path)
