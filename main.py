import os, shutil
from pathlib import Path

home = Path.home()
downloads_path = home / 'Downloads'

# Get a list of files in the Downloads folder
download_items = os.listdir(downloads_path)
downloads = [f for f in download_items if os.path.isfile(downloads_path / f)]  # Full path to files

# Define categories and their associated extensions
text_and_data = ['.txt', '.csv', '.json', '.xml', '.yaml', '.yml']
documents = ['.pdf', '.docx', '.xlsx', '.pptx']
code = ['.py', '.js', '.html', '.css']
images = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
audio_and_video = ['.mp3', '.wav', '.flac', '.mp4', '.avi', '.mkv', '.mov']
archives = ['.zip', '.tar', '.gz', '.rar', '.7z']

# Group extensions under category names
type_groups = {
    'text_and_data': text_and_data,
    'documents': documents,
    'code': code,
    'images': images,
    'audio_and_video': audio_and_video,
    'archives': archives
}

# Create category directories inside Downloads folder
for category in type_groups:
    category_path = downloads_path / category
    category_path.mkdir(exist_ok=True)  # Create the folder if it doesn't exist

# Function to check the file type
def check_type(file):
    file_suffix = Path(file).suffix  # Get the file's extension
    for group, extensions in type_groups.items():
        if file_suffix in extensions:
            return group
    return None  # If no category matched

# Function to move file to its respective category folder
def move_file(source, destination):
    # Get the full path for source and destination
    source_path = downloads_path / source  # Full path to the source file
    destination_path = downloads_path / destination / Path(source).name  # Full destination path
    shutil.move(str(source_path), str(destination_path))  # Move file to the new folder

# Iterate through the files and move them to the right category folder
for i in downloads:
    category = check_type(i)
    if category:
        move_file(i, category)
