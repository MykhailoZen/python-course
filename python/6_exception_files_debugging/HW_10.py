# Practice:
# Create a function that will work with files.
# The function should have 3 arguments:
# - File operation type (writing to a file, reading from a file, etc.).
# - File path (The path to the file with which the operation will be performed).
# - Content (optional argument).
# The function must perform actions with the file. In the case of reading,
# the content of the file should be displayed to the user.
# Add error handling (try to handle all common input errors).


import os

def check_content(content):
    if content != None:
        return True
    else:
        raise TypeError("Writing data must not be None")

def read_file(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
        print("File content:")
        print(file_content)

def write_file(file_path, content):
    if check_content(content):
        with open(file_path, 'w') as file:
            file.write(str(content) + '\n')
            print("Content has been written to the file successfully.")

def extend_file(file_path, content):
    if check_content(content):
        with open(file_path, 'a') as file:
            file.write(str(content) + '\n')
            print("Content has been appended to the file successfully.")

def delete_file(file_path):
    os.remove(file_path)
    print("File has been deleted successfully.")


def file_operation(operation_type, file_path, content=None):
    try:
        if operation_type == 'read':
            read_file(file_path)
        elif operation_type == 'write':
            write_file(file_path, content)
        elif operation_type == 'extend':
            extend_file(file_path, content)
        elif operation_type == 'delete':
            delete_file(file_path)
        else:
            raise ValueError("Invalid operation type. Please choose 'read', 'write', 'extend', or 'delete'.")
    except FileNotFoundError as fnf_error:
        print(fnf_error)
        print("Please provide a valid file path.")
    except PermissionError:
        print("Permission denied. You don't have permission to perform this operation on the file.")
    except TypeError as type_error:
        print("TypeError occurred:", type_error)
    except OSError as ose_error:
        print("OSError occurred:", ose_error)
    except Exception as err:
        print("An error occurred:", err)

# Example usage:
if __name__ == "__main__":
    # Writing to a file:
    file_operation('write', 'example.txt', 'Hello, world!')

    # Extending a file:
    file_operation('extend', 'example.txt', 'This is a new line.')
    file_operation('extend', 'example.txt', ['f', 'd', 's'])
    file_operation('extend', 'example.txt', 1000)

    # Reading from a file:
    file_operation('read', 'example.txt')

    # Deleting a file:
    file_operation('delete', 'example.txt')

    # Error handling example - Invalid operation type:
    file_operation('invalid', 'example.txt')

    # Error handling example - Invalid data type to write to file:
    file_operation('write', 'example.txt', None)
    file_operation('write', 'example.txt')

    # Error handling example - Bad file descriptor:
    file_operation('read', 10)
    file_operation('write', 11, 'Hello, world!')
    file_operation('extend', 12, 'This is a new line.')

    # Error handling example - FileNotFoundError:
    file_operation('delete', 'example.txt') # not checking FileNotFoundError if the file has not been deleted previously
    file_operation('read', 'example.txt')

    # Error handling example - PermissionError:
    # Precondition: chmod ugo=r test_read-only_file.txt
    file_operation('write', 'test_read-only_file.txt', 'Hello, world!')