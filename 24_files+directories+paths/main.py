# file = open("24_files+directories+paths/my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# with open("24_files+directories+paths/my_file.txt") as file:
#     contents = file.read()
#     print(contents)
# ==> replaces the need to close the file

# mode = "r" => default, read only mode
# mode = "w" => replaces existing file content, write only mode
# mode = "a" => append, adds to the file. 
# if a file does not exist and you open in it WRITE mode, python creates it for you

with open("24_files+directories+paths/my_file.txt", mode = "a") as file:
    file.append("New file.")