""" Creating a function that will work with files"""


def working_with_files(operation_type, path_to_file, content=None):
    # Creating a file
    if operation_type == 'create':
        try:
            with open(path_to_file, 'x') as file:
                pass
        except FileExistsError:
            print(f"File '{path_to_file}' already exists.")
        except IOError as e:
            print(f"An error occurred while creating the file: {e}")
    # Writing to file
    elif operation_type == 'write':
        try:
            with open(path_to_file, 'w') as file:
                file.write(content)
        except IOError as e:
            print(f"An error occurred while writing to the file: {e}")
    # Reading from file
    elif operation_type == 'read':
        try:
            with open(path_to_file, 'r') as file:
                file_content = file.read()
                print(file_content)
        except FileNotFoundError:
            print(f"File '{path_to_file}' not found.")
        except IOError as e:
            print(f"An error occurred while reading the file: {e}")
    # Appending to file
    elif operation_type == 'append':
        try:
            with open(path_to_file, 'a') as file:
                file.write(content)
        except IOError as e:
            print(f"An error occurred while appending to the file: {e}")
    else:
        print("Unsupported operation type")


# Creating a file
working_with_files('create', 'my_file.txt')
# Writing some text to it
working_with_files('write', 'my_file.txt', 'This is my content for text file')
# Reading from file
working_with_files('read', 'my_file.txt')
# Appending some additional text
working_with_files('append', 'my_file.txt', '\nTo be continued...')
# Once more reading from file
working_with_files('read', 'my_file.txt')
# Let's throw some exception
working_with_files('create', 'my_file.txt')
# Let's throw another exception
working_with_files('read', 'file.txt')



