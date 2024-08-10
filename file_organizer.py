import os
import shutil
from pathlib import Path
FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Audio': ['.mp3', '.wav', '.aac'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Archives': ['.zip', '.tar', '.rar', '.gz'],
    # Add more as needed
}
def organize_files(directory):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        
        if os.path.isfile(file_path):
            file_ext = Path(file).suffix.lower()
            moved = False
            
            for folder, extensions in FILE_TYPES.items():
                if file_ext in extensions:
                    folder_path = os.path.join(directory, folder)
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    
                    shutil.move(file_path, os.path.join(folder_path, file))
                    print(f"Moved {file} to {folder}/")
                    moved = True
                    break
            
            if not moved:
                print(f"File {file} did not match any category.")
if __name__ == "__main__":
    directory = input("Enter the directory you want to organize: ")
    if os.path.isdir(directory):
        organize_files(directory)
        print("Organization complete!")
    else:
        print("Invalid directory!")
