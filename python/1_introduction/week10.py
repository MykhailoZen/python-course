"""Create a function that will work with files.
The function should have 3 arguments:

File operation type (writing to a file, reading from a file, etc.).
File path (The path to the file with which the operation will be performed).
Content (optional argument).
The function must perform actions with the file. In the case of reading, the content of the file should be displayed to the user.
Add error handling (try to handle all common input errors).

1. No need to use 'close()' if you open the file with 'with as'. +
2. Default value for 'content' does not work.
If the user does not enter anything for the content, the function will receive an empty string. +
3. The specified option "w for write" does not overwrite the file.+
4. It makes no sense to offer enter content for reading the file.+
5. It is not rational to call an `open` in three places, it can be done only once. -

"""

def file_operation(task_to_do, file_name, content):
    try:
        if content == "":
            content = "default content"
        if task_to_do == "r":
            with open(file_name, "r") as reader:
                print(reader.read())
        elif task_to_do == "w":
            with open(file_name, "r+") as reader:
                reader.truncate(0)
                reader.write(content)
                reader.write("\n")
        elif task_to_do == "a":
            with open(file_name, "a") as reader:
                reader.write(content)
                reader.write("\n")
        else:
            raise Exception(f"argument have to be r, w or a. you entered ({task_to_do})")
    except FileNotFoundError as error:
        print(error)
        print("wrong file name")
    except Exception as error:
        print(error)
        print("wrong request")


content = ""
task_to_do = input('r for read, w for write, a for append :')
file_name = input('link to file :')
if task_to_do == "w" or task_to_do == "a":
    content = input('text to add, optional :')

file_operation(task_to_do, file_name, content)

