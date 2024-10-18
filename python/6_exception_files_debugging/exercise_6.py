# Create a function that will work with files.
# The function should have 3 arguments:
#
# File operation type (writing to a file, reading from a file, etc.).
# File path (The path to the file with which the operation will be performed).
# Content (optional argument).
# The function must perform actions with the file. In the case of reading, the content of the file should be displayed
# to the user.
# Add error handling (try to handle all common input errors)
def file_function(file_operation: str, file_path: str, content: str = "") -> None:
    try:
        with open(file_path, 'r+') as f:
            match file_operation:
                case "read":
                    print(f.read())
                case "write":
                    f.seek(0, 2)  # cursor to file end
                    f.write(content)
                    f.seek(0)  # cursor to file begin
                    print(f.read())
                case _:
                    print('This operation is not supported.')
        f.close()
    except FileNotFoundError:
        print('Incorrect file path. Please type again.')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    file_function('read', 'file.txt')
    file_function('write', 'file.txt', 'New content to write\n')
