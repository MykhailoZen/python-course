def file_operations(operation_type, file_path, content=None):
    """
    Create a function that will work with files.
    The function should have 3 arguments:

    File operation type (writing to a file, reading from a file, etc.).
    File path (The path to the file with which the operation will be performed).
    Content (optional argument).
    The function must perform actions with the file. In the case of reading, the content of the file should be displayed to the user.
    Add error handling (try to handle all common input errors).
    """
    try:
        if operation_type == 'read':
            with open(file_path, 'r') as file:
                print(file.read())
        elif operation_type == 'write' and content is not None:
            with open(file_path, 'w') as file:
                file.write(content)
        else:
            print("Invalid operation or missing content for writing.")
    except FileNotFoundError:
        print("Error: The file was not found.")
    except IOError:
        print("Error: Problem reading or writing to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")