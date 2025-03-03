from class_File import File
from class_Folder import Folder

files = []
folders = []
def create_sys():
    if input("File / Folder\n").lower() == "file":
        pramname_create_file = input("File Name\n")
        pramtype_create_file = input("File Type\n")
        new_file = File(pramname_create_file, pramtype_create_file)
        files.append(new_file)
        if input("").lower() == "restart":
            state_layer1 = ""
            state_layer2 = ""
            askstate = True
            main_sys()
        else:
            main_sys()
    else:
        pramname_create_folder = input("Folder Name\n")
        new_folder = Folder(pramname_create_folder)
        folders.append(new_folder)
        if input("").lower() == "restart":
            state_layer1 = ""
            state_layer2 = ""
            askstate = True
            main_sys()
        else:
            None
create_sys()