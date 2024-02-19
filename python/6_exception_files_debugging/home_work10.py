"""
Create a function that will work with files.
The function should have 3 arguments:

File operation type (writing to a file, reading from a file, etc.).
File path (The path to the file with which the operation will be performed).
Content (optional argument).
The function must perform actions with the file. In the case of reading, the content of the file should be displayed to
the user.
Add error handling (try to handle all common input errors).
"""
operation_input = ''
file_name = ''
content_needed = ['w', 'write', 'a', 'append']
content_to_write = None


def work_with_files(operation_type, file_path, content=None):
    """
    The function allows you to work with files: create, read, write, or append content.

    Parameters:
        operation_type (str): The type of operation to perform (e.g., 'read', 'write', 'append', 'create').
        file_path (str): The path to the file to be operated on.
        content (optional): The content to write or append to the file.
    """
    try:
        if operation_type == "x" or operation_type == "create":
            with open(file_path, 'x') as file:
                print(f"File '{file_path}' created successfully")
        if operation_type == "read" or operation_type == "r":
            with open(file_path, 'r') as file:
                content = file.read()
                print(content)
        elif operation_type == "write" or operation_type == "w":
            with open(file_path, 'w') as file:
                content = file.write(content)
                print("File saved...")
        elif operation_type == "append" or operation_type == "a":
            with open(file_path, 'a') as file:
                content = file.write(content)
                print("File saved...")
    except FileNotFoundError as err1:
        print(f"File not found... Please check if {file_path} exists")
    except PermissionError as err2:
        print(f"Check access to {file_path}. Can't read/write the file...")
    except FileExistsError as err3:
        print(f"File {file_path} already exists")


print("The program allows you to read content of the file, or add some new data")
file_operations = ["r", "read", "w", "write", "a", "append", "x", "create", "exit"]

while operation_input not in file_operations or len(file_name) < 1:
    operation_input = input("Please, select needed operation: \n"
                            "x/create - create file\n"
                            "r/read - to read the content of file \n"
                            "w/write - to write content"
                            " (previous data will be erased) \n"
                            "a/append - to add new content to previous\n"
                            "exit to quit the program\n>>>").lower()
    if operation_input == "exit":
        print("Exit...")
        break
    file_name = input("Please, provide file name: \n>>>")
    if len(file_name) < 1:
        print("The file name can't be empty!")
    if operation_input in content_needed:
        content_to_write = input("What do you want to write to the file:\n>>>")

    work_with_files(operation_input, file_name, content_to_write)
