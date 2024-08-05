import tkinter as tk
from tkinter import filedialog
import os

def save_filenames_to_txt(filenames, output_file="output_filenames.txt"):
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            for idx, filename in enumerate(filenames):
                print(f"Processing file {idx + 1}/{len(filenames)}: {filename}")
                f.write(filename + '\n')
        print(f"Filenames saved to {output_file}")
        print(f"Total files listed: {len(filenames)}")
    except Exception as e:
        print(f"An error occurred while saving the filenames: {e}")

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Show directory dialog for selecting a folder
    directory = filedialog.askdirectory(title="Select a folder containing .txt files")

    if directory:
        try:
            print(f"Selected directory: {directory}")
            # Get all .txt files in the directory
            filenames = [f for f in os.listdir(directory) if f.endswith('.txt') and os.path.isfile(os.path.join(directory, f))]
            
            if not filenames:
                print("No .txt files found in the selected directory.")
                return

            # Sort the filenames alphabetically
            filenames.sort()

            # Display filenames and ask for confirmation
            print("Files found in the directory:")
            for filename in filenames:
                print(filename)

            confirm = input("Do you want to export these filenames to a .txt file? (yes/no): ").strip().lower()
            
            if confirm == 'yes':
                # Save filenames to the output file
                save_filenames_to_txt(filenames)
            else:
                print("Operation cancelled by user.")
        except Exception as e:
            print(f"An error occurred while processing the directory: {e}")
    else:
        print("No folder selected.")

    input("Press any key to exit...")

if __name__ == "__main__":
    main()
