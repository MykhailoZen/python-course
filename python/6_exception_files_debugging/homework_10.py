def operation_with_file(operation_type, file_path, content=None):
    try:
        with open(file_path, operation_type) as file:
            if operation_type == "r":
                file_content = file.read()
                print("File content:", "\n", file_content)
            elif operation_type in ["w", "a"]:
                file.write(content + '\n')
                print("Content successfully edited in the file.")
            else:
                print("Invalid operation type. Please choose from 'r', 'w', or 'a'.")
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
    except PermissionError:
        print("Permission denied to access the file. Please ensure you have the necessary permissions.")


operation_with_file("r", "example.txt")

operation_with_file("w", "example.txt", "This is example content.")

operation_with_file("a", "example.txt", "This is some appended content.")
