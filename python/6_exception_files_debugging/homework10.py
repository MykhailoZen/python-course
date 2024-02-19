# Practice:
# Create a function that will work with files.
# The function should have 3 arguments:
# File operation type (writing to a file, reading from a file, etc.).
# File path (The path to the file with which the operation will be performed).
# Content (optional argument).
# The function must perform actions with the file. In the case of reading, the content of the file should be displayed to the user.
# Add error handling (try to handle all common input errors).
import re
def file_operator(operation_mode, file_path, content=''):
    """Hello,
    This function will allow to read file, append some data to file, write new data to file or clear it
    For work, function requires 2 mandatory arguments 'operation_mode', 'file_path' and one optional argument - 'content'
    'operation_mode' -> program allow to use such modes: 'read', 'write', 'append', 'clear'
    'file_path' -> path to a file to work. Be sure to type it in a wright way.
    'content' -> some data to write or append to file
    """
    try:
        if operation_mode == 'read':
            with open(file_path, 'r') as reader:
                # read and print entire file
                print(f'Here the content of the {file_path}:\n')
                print(reader.read())
        elif operation_mode == 'write':
            sentences = re.split(r'(?<=\.|\?|!)\s', content)
            with open(file_path, 'w') as writer:
                for sentence in sentences:
                    writer.write(sentence.strip() + '\n')
                print(f'New data has been written in {file_path}')
        elif operation_mode == 'append':
            with open(file_path, 'a') as appender:
                appender.write(content + '\n')
        elif operation_mode == 'clear':
            with open(file_path, 'w') as clearer:
                print (f'File "{file_path}" has been cleared successfully.')
                pass
        else:
            raise ValueError("Sorry, program allows only to choose one of these operation modes: 'read', 'write' and 'append'")

    except FileNotFoundError:
        print('Sorry, file is not found. Type a Valid path to file')
    except PermissionError:
        print('Permission denied!')
    except Exception as err:
        print(f"Ups, Something went wrong while opening the file! {err}")

# Some testing of the code:
# read dummy_text.txt file:
file_operator('read', 'dummy_text.txt')
# exception FileNotFoundError:
file_operator('read', 'dummtext.txt')
#  add some new string to text in dummy_text.txt
file_operator('append', 'dummy_text.txt', 'Contrary to popular belief, Lorem Ipsum is not simply random text.')
# write some data to dummy2.txt (splitted into a list of sentences)
file_operator('write', 'dummy2.txt', "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. ")
# erase data of  dummy2.txt
file_operator('clear', 'dummy2.txt')