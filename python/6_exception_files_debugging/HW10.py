def files_operations(operation_type, file_path, *content):
    """This function will execute different operations with file, e.g. writing, reading, appending, creating"""
    try:
        with open(file_path, operation_type) as my_file:
            if operation_type == 'w':
                print('File has been overwritten.')
                my_file.write(*content)
            elif operation_type == 'a':
                print('File has been updated.')
                my_file.write(*content)
            elif operation_type == 'r':
                b = my_file.read()
                print('File has the following content:')
                print(b)
    except FileExistsError as file_exist_error:
        """Verification of the file existence, that user want to create"""
        print('Such file is already exist:', file_exist_error)
    except FileNotFoundError as no_file_error:
        """Verification that the specified path is correct and in general if the file exists"""
        print('Such file is not exist according to specified path:', no_file_error)
    except TypeError as type_error:
        """Verification that all parameters has the correct type"""
        print('Type error occurred:', type_error)


files_operations('r', 'test_file.txt', "\nHello!I am your test file!Do your best!")




