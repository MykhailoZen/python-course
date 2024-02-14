"""Create a function that will work with files.
The function should have 3 arguments:

File operation type (writing to a file, reading from a file, etc.).
File path (The path to the file with which the operation will be performed).
Content (optional argument).
The function must perform actions with the file. In the case of reading, the content of the file should be displayed to the user.
Add error handling (try to handle all common input errors)."""

def file_operation(task_to_do, file_name, content="default content"):
    try:
        if task_to_do == "r":
            with open(file_name, "r") as reader:
                print(reader.read())
                reader.close()
        elif task_to_do == "w":
            with open(file_name, "r+") as reader:
                reader.write(content)
                reader.write("\n")
                reader.close()
        elif task_to_do == "a":
            with open(file_name, "a") as reader:
                reader.write(content)
                reader.write("\n")
                reader.close()
        else:
            raise Exception(f"argument have to be r, w or a. you entered ({task_to_do})")
    except FileNotFoundError as error:
        print(error)
        print("wrong file name")
    except Exception as error:
        print(error)
        print("wrong request")



task_to_do = input('r for read, w for write, a for append :')
file_name = input('link to file :')
content = input('text to add, optional :')

file_operation(task_to_do, file_name, content)

