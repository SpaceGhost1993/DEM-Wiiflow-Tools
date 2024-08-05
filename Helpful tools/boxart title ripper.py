import os

def export_image_titles():
    current_dir = os.getcwd()
    export_dir = os.path.join(current_dir, "exported_titles")

    # Create the export directory if it doesn't exist
    if not os.path.exists(export_dir):
        os.makedirs(export_dir)

    # Walk through the directory
    for root, dirs, files in os.walk(current_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                relative_dir = os.path.relpath(root, current_dir)
                target_dir = os.path.join(export_dir, relative_dir)

                # Create subdirectories in the export directory if needed
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)

                # Write the title name to a text file
                title_name = os.path.splitext(file)[0]
                with open(os.path.join(target_dir, f"{title_name}.txt"), 'w', encoding='utf-8') as title_file:
                    title_file.write(title_name)

    print("Export complete!")

if __name__ == "__main__":
    export_image_titles()
