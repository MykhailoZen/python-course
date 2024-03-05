def operation_with_file(
        operation: str,
        file_path: str,
        content=None
):
    """
    This function was made for file handling, where:
    :param operation: type of operation for interaction
    :param file_path: path to file
    :param content: content of file

    :return: result of function
    """

    operations_list = ["w", "a", "r", "x"]

    if operation not in operations_list:
        raise ValueError(f"Invalid argument '{operation}'. Please choose some from {operations_list}")
    if operation in {"w", "a"} and not content:
        raise ValueError(f"Content can't be empty for this operation")

    try:
        with open(file_path, operation) as file:
            # Reading
            if operation == "r":
                return print(file.read())

            # Writing / Appending
            if operation == "w" or operation == "a":
                result = file.write(str(content) + "\n")
                return result

            # Creating of new file
            if operation == "x":
                pass

    except (FileNotFoundError, FileExistsError, Exception) as exc:
        return print(f"An error occurred: {exc!r}")