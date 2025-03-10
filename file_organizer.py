import os
import shutil

# Define the directory to organize
directory_to_organize = "C:/Users/desnk/OneDrive/File Organizer"


# Define file type categories
file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Executables": [".exe", ".msi"],
    "Scripts": [".py", ".js", ".sh", ".bat"],
    "Others": []  # For files that don't match any category
}

def organize_files(directory):
    # Create folders for each category if they don't exist
    for category in file_categories:
        folder_path = os.path.join(directory, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Iterate over files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        _, file_extension = os.path.splitext(filename)
        file_extension = file_extension.lower()

        # Determine the category for the file
        category = "Others"
        for cat, extensions in file_categories.items():
            if file_extension in extensions:
                category = cat
                break

        # Move the file to the appropriate folder
        destination_folder = os.path.join(directory, category)
        shutil.move(file_path, os.path.join(destination_folder, filename))

        print(f"Moved: {filename} -> {category}")

if __name__ == "__main__":
    organize_files(directory_to_organize)
    print("File organization complete!")


