def file_action(operation: str, path: str, content: str = '') -> str:
    """
    Function performs correspondent actions with files

    :param operation: file operation type
    :param path: file path
    :param content: content (optional argument)
    :return: depends on operation with file: r - prints file, w/a - writing to file, x - file creation and writing
    """
    try:
        with open(path, operation) as file:
            if 'r' in operation:
                print(file.read())
            if 'w' in operation or 'a' in operation:
                content = content.encode() if 'b' in operation else content
                file.write(content)
            if 'x' in operation:
                content = content.encode() if 'b' in operation else content
                file.write(content)
                print('File is created successfully!')
    except (ValueError, TypeError) as e:
        print(f'Something went wrong: {e}')
    except FileNotFoundError:
        print('This file does not exist!')
    except FileExistsError:
        print('This file already exists!')
    except OSError as e:
        print(f'Wrong file path: {e}')

