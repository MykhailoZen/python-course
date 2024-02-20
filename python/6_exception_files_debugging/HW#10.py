def file_operation(operation_type, file_path, file_content=None):
    try:
        with open(file_path, "a" if operation_type == "append" else "w" if operation_type == "write" else "r") as file:
            if operation_type == "read":
                content = file.read()
                print(content)
            elif operation_type == "write":
                file.write(file_content)
                print("test123 added to test.txt")
            elif operation_type == "append":
                if file_content:
                    file_content = "\n" + file_content if not file_content.startswith('\n') else file_content
                file.write(file_content)
                print("new line added to test.123")
            else:
                print("Invalid operation.")

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
