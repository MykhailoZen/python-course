def work_with_file(operation, file_path, content=None):
    """
    A function that works with a file and handles most common errors
    It has 3 arguments:
    1. File operation type (writing to a file, reading from a file, appending to file);
    In case of reading, the content of the file should be displayed to the user.
    2. File path (The path to the file with which the operation will be performed).
    3. Content(optional argument).
    """
    try:
        if operation == 'read':
            with open(file_path, 'r') as file:
                file_content = file.read()
                print(file_content)
        elif operation == 'write':
            with open(file_path, 'w') as file:
                file.write(content)
        elif operation == 'append':
            with open(file_path, 'a') as file:
                file.write(content)
        else:
            print("Invalid operation type. Use 'read', 'write', or 'append'.")
    except FileNotFoundError:
        print(f"File not found at path: {file_path}")
    except PermissionError:
        print(f"Permission denied for file: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


work_with_file('read', 'file_with_content.txt')
work_with_file('write', 'file_with_content.txt', 'Homework 10.\n')
work_with_file('append', 'file_with_content.txt', 'Adding content to the end of the file.\n')
