def file_handling(operation_type, file_path, content=None):
    try:
        if operation_type == 'read':
            with open(file_path, 'r') as file:
                file_content = file.read()
                print("File content:")
                print(file_content)
        elif operation_type == 'write':
            with open(file_path, 'w') as file:
                file.write(content)
                print("Content has been successfully written to the file.")
        else:
            print("Invalid operation type. Please specify 'read' or 'write'.")

    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except PermissionError:
        print("Permission denied. You don't have the necessary permissions to perform this operation.")
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        print("All operations are completed")

file_handling('read', 'Myhomework.txt')
file_handling('write', 'Myhomework.txt', 'Random text.')
file_handling('read', 'nonexistent_file.txt')
