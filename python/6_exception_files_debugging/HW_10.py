# Practice:
# Create a function that will work with files.
# The function should have 3 arguments:
# - File operation type (writing to a file, reading from a file, etc.).
# - File path (The path to the file with which the operation will be performed).
# - Content (optional argument).
# The function must perform actions with the file. In the case of reading, the content of the file should be displayed to the user.
# Add error handling (try to handle all common input errors).


import os

def file_operation(operation_type, file_path, content=None):
    try:
        if operation_type == 'read':
            with open(file_path, 'r') as file:
                file_content = file.read()
                print("File content:")
                print(file_content)
        elif operation_type == 'write':
            with open(file_path, 'w') as file:
                file.write(content)
                print("Content has been written to the file successfully.")
        elif operation_type == 'extend':
            with open(file_path, 'a') as file:
                file.write(content)
                print("Content has been appended to the file successfully.")
        elif operation_type == 'delete':
            os.remove(file_path)
            print("File has been deleted successfully.")
        else:
            print("Invalid operation type. Please choose 'read', 'write', 'extend', or 'delete'.")
    except FileNotFoundError as fnf_error:
        print(fnf_error)
        print("Please provide a valid file path.")
    except PermissionError:
        print("Permission denied. You don't have permission to perform this operation on the file.")
    except Exception as e:
        print("An error occurred:", e)

# Example usage:
if __name__ == "__main__":
    # Writing to a file
    file_operation('write', 'example.txt', 'Hello, world!')

    # Extending a file
    file_operation('extend', 'example.txt', '\nThis is a new line.')

    # Reading from a file
    file_operation('read', 'example.txt')

    # Error handling example - Invalid operation type
    file_operation('invalid', 'example.txt')

    # Other Exception
    file_operation('write', 'example.txt', None)

    # Deleting a file
    file_operation('delete', 'example.txt')