from class_Folder import Folder
from class_File import File


files = []
folders = []


def main_sys():
    state_layer1 = ""
    state_layer2 = ""
    askstate = True
    if input("").lower() == "start":
            if askstate == True:
               state_layer1 = input("Edit / Create / View\n").lower()
            state_layer2 = input("File / Folder\n")
            if state_layer1 == "edit":
               if state_layer2 == "file":
                    name = input("File Name\n")
                    edit = input("Choose an option: Add Content, Delete Content, Find, or Find and Replace\n").lower()
                    if edit == "add content":
                         name = input("File Name\n")
                         for i in range(len(files)):
                              if files[i].get_file_name() == name:
                                   File.add_content(files[i], input("What content would you like to add?\n"))
                              if input("View?\n").lower() == "yes":
                                   askstate = False
                                   state_layer1 = "view"
                                   main_sys()
                              if input("").lower() == "restart":
                                   state_layer1 = ""
                                   state_layer2 = ""
                                   askstate = True
                                   main_sys()
                              else:
                                   exit()
                    elif edit == "delete content":
                         name = input("File Name\n")
                         for i in range(len(files)):
                              if files[i].lower() == name:
                                   delete_marker1 = input("Enter the lower range of characters to delete\n")
                                   delete_marker2 = input("Enter the upper range of characters to delete\n")
                                   File.delete_content(files[i], delete_marker1, delete_marker2)
                              if input("Would you like to view?\n").lower() == "yes":
                                   askstate = False
                                   state_layer1 = "view"
                                   main_sys()
                              if input("").lower() == "restart":
                                   state_layer1 = ""
                                   state_layer2 = ""
                                   askstate = True
                                   main_sys()
                              else:
                                   exit()
                    elif edit == "find":
                         name = input("File Name\n")
                         letter = input("Enter the letter you want to find\n")
                         for i in range(len(files)):
                              if files[i] == name:
                                   print("The letter ", letter, " appeared ", File.find(files[i], letter), " times")
                              if input("").lower() == "restart":
                                   state_layer1 = ""
                                   state_layer2 = ""
                                   askstate = True
                                   main_sys()
                              else:
                                   exit()
                    elif edit == "find and replace":
                         name = input("File Name\n")
                         letter_2 = input("Letter to be replaced\n")
                         letter = input("Replacing letter\n")
                         for i in range(len(files)):
                              if files[i].get_file_name() == name:
                                   File.find_and_replace(files[i], letter_2, letter)
               elif state_layer2 == "folder":
                    ask = input("Delete File, Add File?\n").lower()
                    if ask == "delete file":
                         name = input("Name of the folder\n")
                         for i in range(len(folders)):
                              if folders[i].get_folder_name() == name:
                                   name_file = input("Name of the file you would like to delete\n")
                                   for j in range(len(files)):
                                        if files[i].get_file_name() == name_file:
                                             Folder.delete_file(folders[i], files[j])
                         if input("Would you like to view").lower() == "yes":
                              state_layer1 = "view"
                              askstate = False
                              main_sys()
                         else:
                              if input("").lower() == "restart":
                                   state_layer1 = ""
                                   state_layer2 = ""
                                   askstate = True
                                   main_sys()
                              else:
                                   exit()
                    elif ask == "add file":
                         name = input("Name of the folder\n")
                         for i in range(len(folders)):
                              if folders[i].get_folder_name() == name:
                                   name_file = input("Name of the file you would like to delete\n")
                                   for j in range(len(files)):
                                        if files[j].get_file_name() == name_file:
                                             Folder.add_file(folders[i], files[j])
                         if input("Would you like to view?\n").lower() == "yes":
                              state_layer1 = "view"
                              askstate = False
                              main_sys()
                         else:
                              if input("").lower() == "restart":
                                   state_layer1 = ""
                                   state_layer2 = ""
                                   askstate = True
                                   main_sys()
                              else:
                                   exit()
               elif state_layer1 == "create":
                    if input("File / Folder").lower() == "file":
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
                              exit()
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
                         exit()
               elif state_layer1 == "view":
                    state_layer2 = input("File / Folder\n").lower()
                    if state_layer2 == "file":
                         name = input("Name of File\n").lower()
                         for i in range(len(files)):
                              if files[i].file_name.lower() == name:
                                   print("File Name: ", files[i].file_name, " File Type: ", files[i].file_type, "Date Created: ", files[i].time_created, " Size: ", len(files[i].content), " Characters")
                                   user_input = input("Would you like to get content, or find?\n").lower()
                                   if user_input == "get content":
                                        print("Content is\n", files[i].get_content())
                                   elif user_input == "find":
                                        letter = input("What letter would you like to replace?\n")
                                        print("The letter ", letter, " appeared ", File.find(files[i], letter), " times.")
                              if input("Would you like to edit something?\n").lower() == "yes":
                                   state_layer1 = "edit"
                                   askstate = False
                                   main_sys()
                              else:
                                   exit()
                    elif state_layer2 == "folder":
                         name = input("Name of Folder\n")
                         for i in range(len(folders)):
                              if folders[i].folder_name.lower() == name:
                                   print("Folder Name: ", folders[i].folder_name, " Date Created: ", folders[i].creation_date)
                              if input("Would you like to edit something?\n").lower() == "yes":
                                   state_layer1 = "edit"
                                   askstate = False
                                   main_sys()
                              else:
                                   exit()
main_sys()