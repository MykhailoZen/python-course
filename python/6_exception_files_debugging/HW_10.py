# Practice:
# Create a function that will work with files.
# The function should have 3 arguments:
# - File operation type (writing to a file, reading from a file, etc.).
# - File path (The path to the file with which the operation will be performed).
# - Content (optional argument).
# The function must perform actions with the file. In the case of reading,
# the content of the file should be displayed to the user.
# Add error handling (try to handle all common input errors).


def file_operation(operation_type, file_path, content=None):
    """
    This function allows you to perform file operations such as 'creation', 'read', 'write', 'extend'.
    The function takes 2 required (operation_type, file_path) arguments and 1 optional one (content).
    :param operation_type: 'r', 'r+', 'a+', 'w+', 'a', 'w', 'x'
    :param file_path: path to the file we want to work with
    :param content: the data we want to write to the file
    :return: returns nothing, only prints the result of the operation
    """
    operation = ('r', 'r+', 'a+', 'w+', 'a', 'w', 'x')

    try:
        with open(file_path, operation_type) as file:
            if operation_type in operation[:4] and content == None:
                file.seek(0)
                file_content = file.read()
                print("File content:")
                print(file_content)
            elif operation_type in operation[1:] and content:
                file.write(str(content) + '\n')
                print("Content has been written to the file successfully.")
            else:
                print('You do not specify the data to write to the file or something else went wrong.') # OK
    except ValueError as value_error:
        print(f"{value_error}. Invalid operation type. Please choose 'r', 'r+', 'a+', 'w+', 'a', 'w', 'x'.") # OK
    except FileNotFoundError as fnf_error:
        print(f"{fnf_error}. Please provide a valid file path.") # OK
    except PermissionError:
        print("Permission denied. You don't have permission to perform this operation on the file.") # OK
    except FileExistsError as fileexisterror:
        print(f'{fileexisterror}. Create a new file so as not to lose data in {file_path}.') # OK
    except OSError as ose_error:
        print(f"OSError occurred: {ose_error}") # OK
    except Exception as err:
        print(f"An error occurred: {err}")

# Example usage:
if __name__ == "__main__":
    # Writing to a file:
    file_operation('w', 'example.txt', 'Hello, world!')
    file_operation('w+', 'example.txt', 1000)

    # Extending a file:
    file_operation('a', 'example.txt', 'This is a new line.')
    file_operation('a+', 'example.txt', ['f', 'd', 's'])

    # Reading from a file:
    file_operation('r', 'example.txt')
    file_operation('r+', 'example.txt')

    # Creating file and writing:
    file_operation('x', 'example.txt', 'File was created!')
    file_operation('x', 'example_x.txt', 'File was created!')

    # Error handling example - Invalid operation type: OK
    file_operation('invalid', 'example.txt')

    # Error handling example - Invalid data type to write to file: OK
    file_operation('w', 'example.txt', None)
    file_operation('a', 'example.txt')

    # Error handling example - Bad file descriptor: OK
    file_operation('r', 10)
    file_operation('w', 11, 'Hello, world!')
    file_operation('a', 12, 'This is a new line.')

    # Error handling example - FileNotFoundError: OK
    file_operation('r', 'missing_file.txt')

    # Error handling example - PermissionError: OK
    # Precondition: chmod ugo=r test_read-only_file.txt
    file_operation('w', 'test_read-only_file.txt', 'Hello, world!')