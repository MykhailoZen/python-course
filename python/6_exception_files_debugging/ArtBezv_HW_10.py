def file_operation(operation_type, file_path, data):
    try:
        if operation_type == "read":
            with open(file_path, "r") as file:
                print(file.read())
        elif operation_type == "write":
            if data is None:
                raise ValueError("Data must be provided for write operation.")
            with open(file_path, "w") as file:
                file.write(data)
            print("Content written successfully to the file.")
        elif operation_type == "append":
            if data is None:
                raise ValueError("Data must be provided for append operation.")
            with open(file_path, "a") as file:
                file.write(data)
            print("Data appended successfully to the file.")
        else:
            print("Invalid operation type. Supported type is 'read'.")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied to access the file.")

file_operation("write", 'random_file.txt', "Contrary to popular belief, Lorem Ipsum is not simply random text.")