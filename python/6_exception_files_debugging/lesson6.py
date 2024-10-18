'''Create a function that will work with files.
The function should have 3 arguments:

File operation type (writing to a file, reading from a file, etc.).
File path (The path to the file with which the operation will be performed).
Content (optional argument).
The function must perform actions with the file. In the case of reading, the content of the file should be displayed to the user.
Add error handling (try to handle all common input errors).

'''


def file_handler(file_operation, file_path, content =""):
    match file_operation:
        case "w":
            try:
                with open(file_path, "w") as file:
                    file.write(content + "\n")
            except FileNotFoundError:
                print("File not found")
            except PermissionError:
                print("Permission denied")
            except IOError:
                print("can't open file")
        case "r":
            try:
                file = open(file_path, "r")
                print(file.read())
                file.close()
            except FileNotFoundError:
                print("something went wrong, file not found")
            except PermissionError:
                print("you are not allowed to read this file")
            except IOError:
                print("can't open the file")
        case "a":
            try:
                with open(file_path, "a") as file:
                    file.write(content +"\n")
            except FileNotFoundError:
                print("File not found")
            except PermissionError:
                print("Permission denied")
            except IOError:
                print("can't open file")
            except Exception as e:
                print(e)
        case _:
            print("file operation is not valid")


file_handler("r", "textFile.txt")
file_handler("w", "textFile.txt", "Hello there")
file_handler("a", "textFile.txt", "Hello there again")
