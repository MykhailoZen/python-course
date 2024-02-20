def file_operator(operation_type, file_path, *content):
    try:
        with open(file_path, operation_type) as file:
            if operation_type == 'r':
                file_content = file.read()
                print(file_content)
                # To read a file content
            elif operation_type == 'w':
                file.write(str(content) + '\n')
                print("Written to a file: ")
                # To write something into a file
            elif operation_type == 'a':
                file.write(str(content))
                # To append something into a file
            else:
                print('smth went wrong, try again')
    except ValueError as ve:
        print(f"{ve}. Wrong operation type, select: r,w, or a")
    except FileNotFoundError as nf:
        print(f"{nf}. Seems such file does not exist.")
    except Exception as other:
        print(f"Smth went wrong: {other}")


# examples:
file_operator('w', 'hw10.txt', 'written smth in a file')
file_operator('a', 'hw10.txt', 'appended')
file_operator('r', 'hw10.txt')
file_operator('b', 'hw10.txt')
file_operator('r', 'hw111.txt')
