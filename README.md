# File Organizer Project

## Overview

The File Organizer is a Python script designed to help you organize files in a specified directory by categorizing them into predefined folders based on their file types. This tool is particularly useful for managing cluttered directories and ensuring that files are neatly sorted into appropriate categories.

## Features

- **Automatic File Categorization**: Files are automatically sorted into categories such as Images, Documents, Videos, Audio, Archives, Executables, Scripts, and Others.
- **Customizable Categories**: The script allows you to define your own file type categories and extensions.
- **Directory Creation**: The script creates necessary folders for each category if they do not already exist.
- **File Movement**: Files are moved to their respective category folders, keeping your directory organized.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/file-organizer.git
   cd file-organizer
   ```

2. **Install Python**:
   Ensure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

3. **Run the Script**:
   ```bash
   python file_organizer.py
   ```

## Usage

1. **Set the Directory**:
   Modify the `directory_to_organize` variable in the `file_organizer.py` script to point to the directory you want to organize.

2. **Run the Script**:
   Execute the script using Python. The script will automatically create the necessary folders and move files into their respective categories.

3. **Check the Output**:
   After running the script, your files will be organized into the appropriate folders within the specified directory.

## Customization

You can customize the file categories and their associated extensions by modifying the `file_categories` dictionary in the script. For example, to add a new category for "E-books" with `.epub` and `.mobi` extensions, you can update the dictionary as follows:

```python
file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Executables": [".exe", ".msi"],
    "Scripts": [".py", ".js", ".sh", ".bat"],
    "E-books": [".epub", ".mobi"],  # New category
    "Others": []  # For files that don't match any category
