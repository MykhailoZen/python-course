file_location = input("Enter the file path: ")
def file_operation(operation_type, file_path):
    try:
        if operation_type == "read":
            with open(file_path, "r") as file:
                print(file.read())
        else:
            print("Invalid operation type. Supported type is 'read'.")
    except FileNotFoundError:
        print("File not found.")

file_operation("read", file_location)

#   Path to a file
#   /Users/artem.bezvuhliak/Documents/python-course/python/6_exception_files_debugging/random_file.txt