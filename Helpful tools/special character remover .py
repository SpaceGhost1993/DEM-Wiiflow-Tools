import os

def clean_filename(filename):
    # Define characters to remove
    chars_to_remove = ['-', '_', ':']
    # Remove specified characters from the filename
    for char in chars_to_remove:
        filename = filename.replace(char, '')
    return filename

def main():
    # Prompt the user
    user_response = input("Do you want to remove characters like '-', '_', ':' from the .txt file names? (yes/no): ")
    if user_response.lower() != 'yes':
        print("Operation cancelled.")
        return

    # Current directory where the script is located
    current_dir = os.getcwd()

    # Process each .txt file in the current directory
    for filename in os.listdir(current_dir):
        if filename.endswith('.txt'):
            new_filename = clean_filename(filename)
            # Rename the .txt files in the same directory
            os.rename(os.path.join(current_dir, filename), os.path.join(current_dir, new_filename))

    print("Files have been processed and renamed in the same directory.")

if __name__ == "__main__":
    main()
