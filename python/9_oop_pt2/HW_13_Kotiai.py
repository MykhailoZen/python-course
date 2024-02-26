'''Homework for the week 10: Exception, File operation, Debugging rebased to class'''

class OperFiles:
    def __init__(self,file_operation_type, file_path, content=''):
        self.file_operation_type=file_operation_type
        self.file_path = file_path
        self.content = content
    def operation(self):
        if self.file_operation_type == "w":
            '''Write mode verification'''
            print("File has been overwritten with the context")
            self.my_file.write(self.content)
        elif self.file_operation_type == "a":
            '''Append mode verification'''
            print("Content appended to the end of the test:")
            self.my_file.write(f'\n{self.content}')
        elif self.file_operation_type == "r":
            print("Text from the file:")
            f = self.my_file.read()
            print(f)
    def __enter__(self):
        print("__enter__")
        try:
            self.my_file = open(self.file_path, self.file_operation_type)
            return self
        except FileNotFoundError as no_file_error:
            '''Exception for the incorrect path'''
            print("File path is incorrect", no_file_error)
        except TypeError as type_err:
            '''Exception for the incorrect type for the mode entered'''
            print("TypeError occurred:", type_err)
        except AttributeError:
            print("There is no such attribute")
        except Exception as error:
            '''Exception for the incorrect mode or for the mode "x" '''
            print("An error occurred:", error)
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")
        self.my_file.close()


with OperFiles("r", 'file_Kotiai_6.txt', 'text line e') as file_operation:
    file_operation.operation()














