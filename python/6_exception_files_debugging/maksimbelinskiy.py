""" Creating a function that will work with files"""


def working_with_files(operation_type, path_to_file, content=None):
    try:
        with open(path_to_file, operation_type) as file:
            if operation_type == "r":
                return print(file.read())
            if operation_type == "w" or operation == "a":
                result = file.write(str(content) + "\n")
                return result
            if operation_type == "x":
                pass

    except FileNotFoundError:
        return print(f"Not found: {path_to_file}")
    except FileExistsError:
        return print(f"File exist: {path_to_file}")
    except Exception as e:
        return print(f"An error occurred: {e}")

working_with_files('w','maks.txt',content='Hi')