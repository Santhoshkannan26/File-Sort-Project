import os
import shutil

path = r"D:\FILE SORT PROJECT"

# File type folders
file_types = {
    "csv files": [".csv"],
    "images": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
    "text": [".txt", ".doc", ".docx", ".pdf"],
    "excel": [".xlsx", ".xls"],
    "videos": [".mp4", ".avi", ".mov", ".mkv"],
    "audio": [".mp3", ".wav", ".aac"],
    "archives": [".zip", ".rar", ".7z"],
    "code": [".py", ".java", ".cpp", ".js", ".html", ".css"],
    "others": []  # For unknown files
}

# Create folders if they don't exist
for folder in file_types:
    os.makedirs(os.path.join(path, folder), exist_ok=True)

# Move files
for file in os.listdir(path):
    file_path = os.path.join(path, file)
    
    if os.path.isfile(file_path):  # Ignore directories
        moved = False
        for folder, extensions in file_types.items():
            if file.lower().endswith(tuple(extensions)):
                shutil.move(file_path, os.path.join(path, folder, file))
                moved = True
                break
        
        if not moved:  # Move unknown files
            shutil.move(file_path, os.path.join(path, "others", file))
