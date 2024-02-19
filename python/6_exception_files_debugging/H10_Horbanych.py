def file_operation(file_operation_type, file_path, content=None):
    try:
        if file_operation_type == "read":
            with open(file_path, "r") as file:
                file_content = file.read()
                print("File content:")
                print(file_content)
        elif file_operation_type == "write":
            with open(file_path, "w") as file:
                file.write(content)
                print("Content written to the file successfully.")
        elif file_operation_type == "append":
            with open(file_path, "a") as file:
                file.write(content)
                print("Content appended to the file successfully.")
        else:
            print("Invalid file operation type. Please choose from 'read', 'write', or 'append'.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except PermissionError:
        print(f"You don't have permission to perform this operation on '{file_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example_1
# usage:
# Reading from a file
file_operation("read", "example.txt")

# Example_2
# Writing to a file
file_operation("write", "example.txt", "Hello, world!")

# Example_3
# Appending to a file
file_operation("append", "example.txt", "\nThis is a new line.")