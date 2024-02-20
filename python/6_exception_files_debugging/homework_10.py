def file_oper(oper_type, file_path, content=None):
    try:
        if oper_type == "write":
            with open(file_path, "w") as file:
                file.write(content)
            print("Content has been written to the file successfully.")
        elif oper_type == "read":
            with open(file_path, "r") as file:
                file_content = file.read()
                print("File content:")
                print(file_content)
        elif oper_type == "append":
            with open(file_path, "a") as file:
                file.write(content)
            print("Content has been appended to the file successfully.")
        else:
            print("Invalid operation type. Please choose 'write', 'read', or 'append'.")
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except PermissionError:
        print("Permission denied. You don't have permission to perform this operation on the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# Write to a file
file_oper("write", "example.txt", "Example content.")

# Append to a file
file_oper("append", "example.txt", "\nAdditional content.")

# Read from a file
file_oper("read", "example.txt")

