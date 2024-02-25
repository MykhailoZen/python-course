def file_func(action, file_path, content=None):

    try:
        with open(file_path, action) as file:
            if action == 'r':
                print(f"Here is {file_path} content:\n{file.read()}")
            elif action == 'w' or action == 'a':
                file.write(str(content) + "\n")
                print(f"Your content has been written to {file_path}: '{content}'")
            elif action == 'x':
                print(f"New file '{file_path}' was created")
            else:
                pass

    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("Permission denied!")
    except Exception as e:
        print(f"Something went wrong when opening the file! {e}")
