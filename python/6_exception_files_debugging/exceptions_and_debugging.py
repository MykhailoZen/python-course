import os

option = input("Enter file operation type (read/write): ").strip().lower()

file_path = input("Enter file path: ").strip()

try:
    if os.path.exists(file_path):
        try:
            if option == "read":
                with open(file_path, 'r') as file:
                    print("File content:")
                    print(file.read())
            elif option =="write":
                with open(file_path, 'w') as file:
                    content = input("Enter content to write/append to file: ").strip()
                    file.write(content + '\n')
                    print("Content '{}' successfully appended to file.".format(content))
            else:
                print("A wrong option selected")
        except:
            print("An unexpected error occurred")
    else:
        print("File not found")
except:
    print("Something unexpected happened")




