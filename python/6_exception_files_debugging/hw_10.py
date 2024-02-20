# Create a function that will work with files.
# The function should have 3 arguments:
# - File operation type (writing to a file, reading from a file, etc.).
# - File path (The path to the file with which the operation will be performed).
# - Content (optional argument).
# The function must perform actions with the file.
# In the case of reading, the content of the file should be displayed to the user.
# Add error handling (try to handle all common input errors).

def file_operation(operation_type, file_path, content=None):
    """
    This function that work with files.
    """
    try:
        with open(file_path, operation_type) as file:
            if operation_type == 'r':
                file_content = file.read()
                print(f'File content: \n{file_content}')
            elif operation_type == 'w' or operation_type == 'a' or operation_type == 'x':
                file.write(f"{content} \n")
                print('Content was added to file.')
    except FileNotFoundError:
        print('File not found')
    except PermissionError:
        print('Permission denied')
    except ValueError:
        print('Invalid operation type. Please choose: r, w, a or x')
    except FileExistsError:
        print("File already exists")


file_operation('', 'example.txt')
file_operation('r', 'example.txt')
file_operation('r', '')
file_operation('w', 'example.txt', 'Content was added to file')
file_operation('a', 'example.txt', 'Content was appended to file')
file_operation('x', 'example.txt', '')
file_operation('x', 'example_new.txt', 'Content was added to a new file')
file_operation('r', 'example_new.txt')


