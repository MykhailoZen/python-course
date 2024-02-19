def file_operation(operation_type, file_path, content=None):
    try:
        if operation_type == 'read':
            with open(file_path, 'r') as file:
                file_content = file.read()
                print("File content:")
                print(file_content)
        elif operation_type == 'write':
            with open(file_path, 'w') as file:
                file.write(content)
                print("Content has been written to the file.")
        elif operation_type == 'append':
            with open(file_path, 'a') as file:
                file.write('\n' + content)
                print("Content has been appended to the file.")
        else:
            print("Invalid operation type. Please choose 'read', 'write', or 'append'.")
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except PermissionError:
        print("Permission denied. You do not have permission to access the file.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage:
operation_type = input("Enter the file operation type (read/write/append): ")
file_path = input("Enter the file path: ")

if operation_type in ['write', 'append']:
    content = input("Enter the content: ")
    file_operation(operation_type, file_path, content)
else:
    file_operation(operation_type, file_path)
