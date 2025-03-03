from datetime import datetime

class File:
    def __init__(self, file_name: str, file_type: str):
        self.file_name = file_name
        self.file_type = file_type
        self.time_created = datetime.now()
        self.content = []

    def get_file_name(self) -> str:
        return self.file_name
    def set_file_name(self, new_name: str) -> None:
        self.file_name = new_name
        
    def get_file_type(self) -> str:
        return self.file_type
    def set_file_type(self, new_file_type: str) -> None:
        self.file_type = new_file_type

    def get_time_created(self) -> str:
        return self.time_created

    def get_content(self) -> str:
        return ''.join(self.content)
    def add_content(self, added_content) -> None:
        self.content.append(list(added_content))
    def delete_content(self, range1, range2) -> None:
        for i in range(range1 - 1, range2 - 1):
            self.content.remove(i)
            
    def find(self, letter) -> int:
        times = 0
        for i in range(len(self.content)):
            if self.content[i] == letter:
                times + 1
            return times
    def find_and_replace(self, letter, replacing_letter) -> None:
        for i in range(len(self.content)):
            if self.content[i] == letter:
                del self.content[i]
                self.content.insert(i, replacing_letter)