def file_operation (file_operation, file_path, content=None):
    try:
        with open(file_path, file_operation) as file:
            if file_operation == "w":
                file.write(content)
                print("Your content has been written to the file")
            elif file_operation == "a":
                file.write(content)
                print("Your content has been added to the file")
            elif file_operation == "r":
                file_content = file.read()
                print("\nThe contents of the file are as follows: \n" + file_content)
    except ValueError:
        print("\nError: Invalid file operation type. Please enter 'r', 'w', or 'a'.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as ex:
        print("The following error occurred: ", ex)
"""Examples with valid arguments:"""
file_operation("w", "test.txt", " 1. First line info")
file_operation("a", "test.txt", "\n 2. Some appended info in 2nd line")
file_operation("r", "test.txt")
"""Examples with invalid arguments:"""
file_operation("wrong", "test.txt", "Some info")
file_operation("r", "nonexistent_file.txt")