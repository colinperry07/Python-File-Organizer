# File Organizer for Downloads

This Python script organizes files in the `Downloads` folder by automatically categorizing and moving them into specific subdirectories based on their file extensions.

### Features:
- **Categorizes Files**: The script sorts files into categories like text files, documents, images, audio, video, and archives.
- **Automatically Creates Directories**: If the necessary directories don't exist in the `Downloads` folder, they are automatically created.
- **File Sorting Based on Extensions**: Files are moved into the corresponding category directory based on their extensions.

---

### Requirements:

- Python 3.x
- No external libraries are required. The script uses built-in libraries like `os`, `shutil`, and `pathlib`.

---

### Setup & Usage:

1. **Clone or Download the Script**: 
   - Download the script or clone this repository to your local machine.

2. **Ensure Downloads Folder Exists**: 
   - The script is designed to work with the `Downloads` folder located in the home directory of your system. Make sure this folder exists and contains files you want to organize.

3. **Run the Script**:
   - Simply run the script in your terminal or command prompt:
     ```bash
     python organize_downloads.py
     ```

4. **How It Works**:
   - The script will look for specific file extensions in your `Downloads` folder.
   - It will then move files to folders based on the file type (e.g., `.txt` files will go to the "text_and_data" folder, `.pdf` files will go to the "documents" folder).
   - It will create any necessary category directories within the `Downloads` folder (if they don't already exist).

---

### Categories & Extensions:

The following categories and extensions are currently supported:

- **Text and Data**: `.txt`, `.csv`, `.json`, `.xml`, `.yaml`, `.yml`
- **Documents**: `.pdf`, `.docx`, `.xlsx`, `.pptx`
- **Code**: `.py`, `.js`, `.html`, `.css`
- **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`
- **Audio and Video**: `.mp3`, `.wav`, `.flac`, `.mp4`, `.avi`, `.mkv`, `.mov`
- **Archives**: `.zip`, `.tar`, `.gz`, `.rar`, `.7z`
