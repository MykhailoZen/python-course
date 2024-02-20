def file_operation(operation_type, file_path, content=None):
    try:
        # Open the file in the appropriate mode based on the operation_type
        with open(file_path, 'r' if operation_type == 'read' else 'a' if operation_type == 'append' else 'w') as file:
            if operation_type == 'read':
                # If operation_type is 'read', read the content from the file
                file_content = file.read()
                # Print the content of the file
                print("File content:")
                print(file_content)
            elif operation_type in ['write', 'append']:
                # If operation_type is 'write' or 'append', write or append the content to the file
                file.write(content)
                # Print a success message depending on the operation_type
                print("Content successfully " + ("appended to" if operation_type == 'append' else "written to") + " the file.")
            else:
                # If the operation_type is invalid, print an error message
                print("Invalid operation type. Please choose from 'read', 'write', or 'append'.")
    except FileNotFoundError:
        # If the file is not found, print an error message
        print("File not found. Please provide a valid file path.")
    except PermissionError:
        # If permission is denied, print an error message
        print("Permission denied. You don't have the necessary permissions to perform this operation.")
    except Exception as e:
        # If any other exception occurs, print an error message with the exception details
        print(f"An error occurred: {e}")
