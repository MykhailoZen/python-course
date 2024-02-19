import os


def perform_file_operation(operation_type, file_path, content=None):
    try:
        # Check operation type and perform corresponding action
        if operation_type == "read":
            if not os.path.exists(file_path):
                raise FileNotFoundError("File '{}' not found.".format(file_path))
            with open(file_path, 'r') as file:
                file_content = file.read()
                print("File content:")
                print(file_content)
        elif operation_type == "write":
            with open(file_path, 'w') as file:
                file.write(content + '\n')
                print("Content '{}' successfully written to file.".format(content))
        elif operation_type == "append":
            with open(file_path, 'a') as file:
                file.write(content + '\n')
                print("Content '{}' successfully appended to file.".format(content))
        elif operation_type == "delete":
            if not os.path.exists(file_path):
                raise FileNotFoundError("File '{}' not found.".format(file_path))
            os.remove(file_path)
            print("File '{}' successfully deleted.".format(file_path))
        elif operation_type == "create":
            if os.path.exists(file_path):
                raise FileExistsError("File '{}' already exists.".format(file_path))
            with open(file_path, 'w') as file:
                if content:
                    file.write(content + '\n')
                print("File '{}' successfully created.".format(file_path))
        else:
            raise ValueError("Invalid operation type: '{}'".format(operation_type))

    except FileNotFoundError as e:
        print("Error:", e)
    except FileExistsError as e:
        print("Error:", e)
    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)


def main():
    print("Current directory content:")
    for item in os.listdir():
        print(item)

    operation_type = input("Enter file operation type (read/write/append/delete/create): ").strip().lower()
    file_path = input("Enter file path: ").strip()

    # Only ask for content if operation type is 'write', 'append', or 'create'
    if operation_type in ["write", "append", "create"]:
        content = input("Enter content to write/append to file (optional): ").strip()
    else:
        content = None

    perform_file_operation(operation_type, file_path, content)


if __name__ == "__main__":
    main()
