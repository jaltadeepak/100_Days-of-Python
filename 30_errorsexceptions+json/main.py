# IndexError
# fruit_list = ["Apple", "Pear", "Banana"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text+5)

# TRY, EXCEPT, ELSE, FINALLY, RAISE
# try: something that might cause an exception
# except: do this if there was an exception
# else: if there were no exceptions
# finally: do this no matter what happens
# raise: raise an errortype

try:
    file = open(r"C:\Code\100 Days of Python - Angela Yu\30_errorsexceptions+json\a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open(r"C:\Code\100 Days of Python - Angela Yu\30_errorsexceptions+json\a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")