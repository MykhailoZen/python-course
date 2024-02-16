import os


def operation_with_file(file_type, file_path, content=None):
    """
        Create a function that will work with files.
        The function should have 3 arguments:
        File operation type (writing to a file, reading from a file, etc.).
        File path (The path to the file with which the operation will be performed).
        Content (optional argument).
        The function must perform actions with the file. In the case of reading,
        the content of the file should be displayed to the user.
        Add error handling (try to handle all common input errors).
    """
    try:
        if file_type == 'read':
            with open(file_path, 'r') as file:
                output_from_file = file.read()
                return f'File "{file_path}" includes: {output_from_file}'
        elif file_type == 'write':
            with open(file_path, 'w') as file:
                file.write('\n' + content)
                return f'In file "{file_path}" has been writing: {content}'
        elif file_type == "append":
            with open(file_path, 'a') as file:
                file.write('\n' + content)
                return f'In file "{file_path}" has been appending: {content}'
        elif file_type == 'clear':
            with open(file_path, 'w') as file:
                file.truncate(0)
                return f'File "{file_path}" has been cleared successfully.'
        elif file_type == 'delete':
            os.remove(file_path)
            return f'File "{file_path}" has been deleted successfully.'
        else:
            return 'Invalid file operation type. Please use "read", "write", "append", "clear", or "delete".'
    except FileNotFoundError as fn:
        return f'File "{file_path}" not found. Please provide a valid file path for "{file_type}" file. ' + str(fn)
    except PermissionError as per:
        return 'Permission denied. You may not have the necessary permissions to perform this operation. ' + str(per)
    except TypeError as te:
        return f'Unsupported type ' + str(te)
    except OSError as osr:
        return f'File "{file_path}". It could not be opened. Change name of file' + str(osr)
    except NameError as nr:
        return 'Input data must be a string. ' + str(nr)
    except Exception as e:
        return 'An error occurred: ' + str(e)


if __name__ == "__main__":
    # Read from file
    print(operation_with_file('read', 't.txt'))
    # Write to file
    print(operation_with_file('write', 'test.txt', 'Hi. It is test'))
    # Append to file
    print(operation_with_file('append', 'test.txt', 'Add information'))
    # Clear file
    print(operation_with_file('clear', 'text.txt'))
    # Delete file
    print(operation_with_file('delete', 'example.txt'))
    # Error handling: file not found
    print(operation_with_file('delete', 'test.txt'))
    # Error handling: invalid content type
    print(operation_with_file('write', 'test.txt', ['Hi. It is test2', 2]))
    print(operation_with_file('write', 'test.txt', None))
    # Error handling: invalid file path type
    print(operation_with_file('write', 5, '78'))
    # Error handling: invalid file operation type
    print(operation_with_file(5, 'test5.txt', '78'))
    print(operation_with_file('de', 'test.txt'))
