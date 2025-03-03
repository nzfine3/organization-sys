from datetime import datetime
from class_File import File

class Folder:
    def __init__(self, folder_name: str):
        self.folder_name = folder_name
        self.creation_date = datetime.now()
        self.files = []

    def get_folder_name(self) -> str:
        return self.folder_name
    def set_folder_name(self, new_folder_name) -> None:
        self.folder_name = new_folder_name
    
    def add_file(self, new_file) -> None:
        self.files.append(new_file)
    def ls(self) -> File:
        return self.files
    def get_file(self, file_name) -> File:
        for i in range(len(self.files)):
            if self.files[i].file_name == file_name:
                return self.files[i]
    def delete_file(self, file_name) -> None:
        for i in range(len(self.files)):
            if self.files[i].file_name == file_name:
                self.files.remove(i)
        
    def get_time_created(self) -> str:
        return self.creation_date