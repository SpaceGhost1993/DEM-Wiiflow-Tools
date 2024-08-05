import os
import shutil
import re

def extract_and_create_folders(folder_path):
    # Regular expression pattern to match all text within parentheses
    pattern = re.compile(r'\((.*?)\)')
    
    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        # Find all matches of text within parentheses
        matches = pattern.findall(filename)
        if matches:
            # Join all matches to form the folder name
            folder_name = ' '.join(matches).strip()

            # Create the new folder if it doesn't exist
            new_folder_path = os.path.join(folder_path, folder_name)
            os.makedirs(new_folder_path, exist_ok=True)

            # Move the file to the new folder
            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(new_folder_path, filename)
            shutil.move(old_file_path, new_file_path)

if __name__ == "__main__":
    # Specify the folder path where the script is placed
    folder_path = os.path.dirname(os.path.abspath(__file__))
    extract_and_create_folders(folder_path)
    print("Files have been moved to their respective folders based on the content within parentheses.")
