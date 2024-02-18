def file_func(action, file_path, content=''):
    try:
        if action == 'read':
            with open(file_path, 'r') as file:
                print(f"Here is {file_path} content: {file.read()}")
        if action == 'write':
            with open(file_path, 'w') as file:
                file.write(content)
                print(f"Your content: {content} has been written to {file_path}")
        if action == 'clear':
            with open(file_path, 'w') as file:
                file.write(content)
                print(f"Your file: {file_path} has been cleared")
    except FileNotFoundError:
        print('File not found!')
    except PermissionError:
        print('Permission denied!')
    except Exception as e:
        print(f"Something went wrong when opening the file! {e}")


# file_func('read', 'homework.txt')
# file_func('write', 'homework.txt', 'Hello World!')
# file_func('clear', 'test.txt')
