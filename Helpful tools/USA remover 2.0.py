import os
import re
import shutil

def remove_parentheses_and_brackets(text):
    # Remove parentheses and brackets from the main part of the filename
    name_part = re.sub(r'[\(\[].*?[\)\]]', '', text).strip()
    
    # Remove any extra spaces before the file extension
    name_part = name_part.rstrip()

    return name_part

def rename_files_in_folder(folder_path):
    # Create a new folder for renamed files
    new_folder_path = os.path.join(folder_path, "renamed_files")
    os.makedirs(new_folder_path, exist_ok=True)

    # Iterate over all .txt files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            # Construct the full file path
            file_path = os.path.join(folder_path, filename)

            # Remove parentheses and brackets from the filename
            new_filename = remove_parentheses_and_brackets(os.path.splitext(filename)[0]) + ".txt"

            # Construct the new file path
            new_file_path = os.path.join(new_folder_path, new_filename)

            # Copy the file to the new folder with the new name
            shutil.copy(file_path, new_file_path)

if __name__ == "__main__":
    # Specify the folder path where the script is placed
    folder_path = os.path.dirname(os.path.abspath(__file__))
    rename_files_in_folder(folder_path)
    print("Files have been renamed and copied to the 'renamed_files' folder.")
