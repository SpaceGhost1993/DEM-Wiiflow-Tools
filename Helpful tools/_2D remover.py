import os
import shutil

def remove_2D_from_filenames(folder_path):
    new_folder = os.path.join(folder_path, "cleaned_filenames")
    os.makedirs(new_folder, exist_ok=True)

    for filename in os.listdir(folder_path):
        if filename.endswith('.txt') and '_2D' in filename:
            new_filename = filename.replace('_2D', '')
            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(new_folder, new_filename)
            shutil.copyfile(old_file_path, new_file_path)
            print(f"Copied and renamed '{filename}' to '{new_filename}'")

    print(f"All files have been processed and saved in the '{new_folder}' folder.")

if __name__ == "__main__":
    current_folder = os.getcwd()
    remove_2D_from_filenames(current_folder)
    print("Process completed. Press Enter to exit...")
    input()
