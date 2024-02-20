def operation_file(operation_type, file_path, content=""):
    """
        Perform a file operation based on the specified type.

        Args:
            operation_type (str): The type of file operation ('w', 'r', 'x', 'a').
            file_path (str): The path to the file for the operation.
            content (str, optional): The content to write to the file (for 'write' operation).

        Raises:
            FileNotFoundError: If the file is not found.
            PermissionError: If the user does not have permission to perform the operation.
            ValueError: If operation_type is not one of 'w', 'r', 'x', 'a'.
        """
    try:
        with open(file_path, operation_type) as test:
            if operation_type == "x":
                test.write(content)
                return "Test file created"
            elif operation_type == "w":
                test.write(content)
                return "Content writen to the file"
            elif operation_type == "a":
                test.write(content)
                return "Content added to the file"
            elif operation_type == "r":
                return test.read()
            else:
                raise ValueError("Invalid operation type. Supported types: 'x', 'w', 'a', 'r'.")
    except FileNotFoundError:
        return "File not found."
    except PermissionError:
        return "Permission denied. You do not have permission to perform this operation."
    except ValueError as e:
        return e


# Created to a file
print(operation_file('x', 'test_file_1.txt', ))
# Writing to a file
print(operation_file('w', 'test_file_1.txt', 'This is my first line'))
# Append to a file
print(operation_file('a', 'test_file_1.txt', '\nThis is my second line\nThis is my third line'))
# Read to a file
print(operation_file('r', 'test_file_1.txt', ))
# FileNotFoundError
print(operation_file('r', 'test_file1.txt', ))
# ValueError
print(operation_file('e', 'test_file_1.txt', ))
