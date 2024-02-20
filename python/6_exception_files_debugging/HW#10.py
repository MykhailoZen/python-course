def file_operation(operation_type, file_path, file_content=None):
    try:
        if operation_type == "read":
            with open(file_path, "r") as file:
                content = file.read()
                print(content)
        elif operation_type == "write":
            with open(file_path, "w") as file:
                file.write(file_content)
                print("test123 added to a test.txt")
        elif operation_type == "append":
            with open(file_path, "a") as file:
                if file_content:
                    file_content = "\n" + file_content if not file_content.startswith('\n') else file_content
                file.write(file_content)
                print("new line added to test.txt")
        else:
            print("Invalid operation type.")

    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("No permission to read test.txt .")
    except Exception as e:
        print("Error:", e)


# reading test.txt
file_operation("read", "test.txt")

# Write test123 to test.txt
file_operation("write", "test.txt", "test123")

# adding new line to test.txt
file_operation("append", "test.txt", "new line")
