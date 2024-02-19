import os


def list_files(directory):
    try:
        files = os.listdir(directory)
        if not files:
            print("No files found in the directory.")
        else:
            print("Files in the directory:")
            for file in files:
                print(file)
    except FileNotFoundError:
        print("Directory not found.")
    except PermissionError:
        print("Permission denied. You do not have permission to access the directory.")
    except Exception as e:
        print(f"An error occurred: {e}")


def file_operation_with_input(directory):
    try:
        list_files(directory)

        operation_type = input("Enter the file operation type (1 for read, 2 for write, 3 for append, 4 for create): ")

        if operation_type not in ['1', '2', '3', '4']:
            print("Invalid operation type. "
                  "Please choose 1 for 'read', 2 for 'write', 3 for 'append', or 4 for 'create'.")
            return

        operation_type = int(operation_type)

        file_path = input("Enter the file path: ")

        if operation_type == 1:
            with open(file_path, 'r') as file:
                file_content = file.read()
                print(file_content)
        elif operation_type == 2:
            content = input("Enter the content: ")
            with open(file_path, 'w') as file:
                file.write(content)
                print(f"Content has been written to {file_path}")
        elif operation_type == 3:
            content = input("Enter the content: ")
            with open(file_path, 'a') as file:
                file.write('\n' + content)  # Append content on a new line
                print(f"Content has been appended to {file_path}")
        elif operation_type == 4:
            with open(file_path, 'w') as file:
                print(f"New file created: {file_path}")

    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except PermissionError:
        print("Permission denied. You do not have permission to access the file.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Get the current directory where the script is running
current_directory = os.getcwd()
print(f"Current directory: {current_directory}")


# usage:
file_operation_with_input(current_directory)
