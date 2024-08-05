import os

def export_filenames(folder_path):
    # Create a new folder for exported filenames
    export_folder_path = os.path.join(folder_path, "exported_filenames")
    os.makedirs(export_folder_path, exist_ok=True)

    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        # Skip directories
        if os.path.isdir(os.path.join(folder_path, filename)):
            continue

        # Get the filename without extension
        file_name_without_extension = os.path.splitext(filename)[0]
        
        # Create a new .txt file with the filename (without extension) as its content
        txt_file_path = os.path.join(export_folder_path, f"{file_name_without_extension}.txt")
        with open(txt_file_path, "w", encoding="utf-8") as txt_file:
            txt_file.write(file_name_without_extension)

if __name__ == "__main__":
    # Specify the folder path where the script is placed
    folder_path = os.path.dirname(os.path.abspath(__file__))
    export_filenames(folder_path)
    print("Filenames have been exported as .txt files in the 'exported_filenames' folder.")
