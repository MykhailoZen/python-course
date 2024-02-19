def file_operation (file_operation, file_path, content=None):
    try:
        with open(file_path, file_operation) as file:
            if file_operation == "w":
                file.write(content)
                print("Сontent's been written to the file")
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
"""Valid arguments:"""
file_operation("a", "123.txt", " Add info line")
file_operation("w", "123.txt", "\n Add second line")
file_operation("r", "123.txt")
"""Invalid arguments:"""
file_operation("operate", "123.txt", "Info Info")
file_operation("w", "file_file2.txt")
