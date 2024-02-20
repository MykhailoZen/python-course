
def manipulate(action, filepath, content=None):
    dict_of_arguments = {'r': 'read file', 'w': 'overwrite file', 'a': 'add to current line', 'al': 'add to a new line'}

    """
    Parameters:
            action (str): The action to perform:
            r - read
            w - write
            a - add to current line
            al - add to a new line
            filepath (str): The path to the file
            content (str, optional): The content to write or append (default is None).

    Raises:
            ValueError: If the action is not one of 'r', 'w', 'a', or 'al'.
    """

    try:
        if action.lower() == 'r':
            with open(filepath, 'r') as file:
                print(file.read())
        elif action.lower() == 'w':
            with open(filepath, 'w') as file:
                file.write(str(content))
        elif action.lower() == 'a':
            with open(filepath, 'a') as file:
                file.write(str(content))
        elif action.lower() == 'al':
            with open(filepath, 'a') as file:
                file.write('\n' + str(content))
        else:
            raise ValueError(
                f'{action} is an invalid argument.'
                f' Please choose one of the following: {", ".join(dict_of_arguments.keys())}')
    except FileNotFoundError:
        print(f'There is no such file as {filepath} :(')
    except FileExistsError:
        print(f'Sorry, {filepath} already exists')
    except PermissionError:
        print(f'Permission to {filepath} is denied')
    except ValueError as error:
        print(error)




