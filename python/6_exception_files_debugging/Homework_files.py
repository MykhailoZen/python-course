''' Creating function called: operations_files
1. arg - file_operation_type
         'r' This is the default mode. It Opens file for reading.
         'w' This Mode Opens file for writing.
         If file does not exist, it creates a new file.
         If file exists it truncates the file.
         'x' Creates a new file. If file already exists, the operation fails.
         'a' Open file in append mode.
         If file does not exist, it creates a new file.
         't' This is the default mode. It opens in text mode.
         '+' This will open a file for reading and writing (updating)

2. arg - file_path
this is path to the file

3. arg - optional argument'''

def operations_files(file_operation_type, file_path, *content):
    lst_1 = ['w', 'w+']
    lst_2 = ['a', 'a+']
    lst_3 = ['r', 'r+']
    try:
        '''Opening file if mode is coorect. It will cclose automatticaly after
        the program is finished'''
        with open(file_path, file_operation_type) as my_file:
            if file_operation_type in lst_1:
                '''Write mode verification'''
                print("File has been overwritten with the context")
                my_file.write(*content)
            elif file_operation_type in lst_2:
                '''Append mode verification'''
                print("Content appended to the end of the test:")
                my_file.write(*content)
            elif file_operation_type in lst_3:
                f = my_file.read()
                print("Text from the file:")
                print(f)
    except FileNotFoundError as no_file_error:
        '''Exception for the incorrect path'''
        print("File path is incorrect", no_file_error)
    except TypeError as type_err:
        '''Exception for the incorrect type for the mode entered'''
        print("TypeError occurred:", type_err)
    except Exception as error:
        '''Exception for the incorrect mode or for the mode "x" '''
        print("An error occurred:", error)
    finally:
        print("Program finished")


operations_files('w','file_Kotiai_4.txt', '\ntext line 1'
                      '\ntext line 2'
                      '\ntext line 3'
                      '\ntext line 4'
                      '\ntext line 5')