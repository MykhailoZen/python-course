# Practice:
# Create a function that will work with files.
# The function should have 3 arguments:
# File operation type (writing to a file, reading from a file, etc.).
# File path (The path to the file with which the operation will be performed).
# Content (optional argument).
# The function must perform actions with the file. In the case of reading, the content of the file should be displayed to the user.
# Add error handling (try to handle all common input errors).

operation_mode = ['r', 'w', 'a']


def file_operator(operation_mode: str, file_path: str, content: str = '' or None):
    """Hello,
    This function will allow to read file, append some data to file, write new data to file or clear it
    For work, function requires 2 mandatory arguments 'operation_mode', 'file_path' and one optional argument - 'content'
    'operation_mode' -> program allow to use such modes: 'r', 'w', 'a'
    'file_path' -> path to a file to work. Be sure to type it in a right way.
    'content' -> some data to write or append to file
    """
    try:
        with open(file_path, operation_mode) as my_file:
            if operation_mode == 'r':
                # read and print entire file
                print(f'Here the content of the {file_path}:\n')
                print(my_file.read())
            elif operation_mode == 'w' and content is not None:
                my_file.write(content + '\n')
                print(f'{file_path} has been changed')
                return True
            elif operation_mode == 'w' and content is None:
                print('file is cleared')
                pass
            elif operation_mode == 'a':
                print(f'Added new line to the {file_path}:\n')
                my_file.write(content + '\n')
                return True
            else:
                raise ValueError(
                    "Sorry, program allows only to choose one of these operation modes: 'read', 'write' and 'append'")

    except FileNotFoundError:
        print('Sorry, file is not found. Type a Valid path to file')
    except PermissionError:
        print('Permission denied!')
    except Exception as err:
        print(f"Ups, Something went wrong while opening the file! {err}")


# Some testing of the code:
# read dummy_text.txt file:
file_operator('r', 'dummy_text.txt')
# exception FileNotFoundError:
file_operator('r', 'dummtext.txt')
# #   add some new string to text in dummy_text.txt
file_operator('a', 'dummy_text.txt', 'Appending some text here, every run')
# if content is none, file is cleared:
file_operator('w', 'dummy2.txt')
# if content is not none, content is written:
file_operator('w', 'dummy2.txt', 'content is not None, write here something good')

