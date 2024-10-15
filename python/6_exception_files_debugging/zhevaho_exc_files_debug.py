from io import UnsupportedOperation
# Create a function that will work with files.
# The function should have 3 arguments:
##File operation type (writing to a file, reading from a file, etc.).
## File path (The path to the file with which the operation will be performed).
## Content (optional argument).
# The function must perform actions with the file. In the case of reading, the content of the file should be
# displayed to the user. Add error handling (try to handle all common input errors).
def actions_with_files():
    try:
        with open("test.txt", "a") as file:
            file.write("\nNew text.")
    except UnsupportedOperation as error_message:
        print(f"that file is {error_message}")
    except FileNotFoundError as error_message:
        print(f"No such file or directory: {error_message}")
    else:
        file = open("test.txt")
        content = file.read()
        print(content)
        file.close()
    finally:
        print("We have successfully written a new line of text to the file and read it")

actions_with_files()
