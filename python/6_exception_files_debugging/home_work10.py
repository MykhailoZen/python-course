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
    except FileNotFoundError:
        print(f"File not found... Please check if {file_path} exists")
    except PermissionError:
        print(f"Check access to {file_path}. Can't read/write the file...")
    except FileExistsError:
        print(f"File {file_path} already exists")
    except Exception as err4:
        print("Error detected. Details: \n", err4)


print("The program allows you to read content of the file, or add some new data")
file_operations = ["r", "read", "w", "write", "a", "append", "x", "create", "exit"]

while True:
    operation_input = input("\nPlease, select needed operation: \n"
                            "x/create - create file\n"
                            "r/read - to read the content of file \n"
                            "w/write - to write content"
                            " (previous data will be erased) \n"
                            "a/append - to add new content to previous\n"
                            "exit to quit the program\n>>>").lower()
    if operation_input == "exit":
        print("Exit...")
        break
    if operation_input not in file_operations:
        print("Invalid operation.")
        continue
    file_name = input("Please, provide file name: \n>>>")
    if len(file_name) < 1:
        print("The file name can't be empty!")
        continue
    if operation_input in ['w', 'write', 'a', 'append']:
        content_to_write = input("What do you want to write to the file:\n>>>")

    work_with_files(operation_input, file_name, content_to_write)
