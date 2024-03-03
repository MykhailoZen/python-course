class OperFiles:
    def __init__(self, file_operation_type, file_path, content=''):
        self.file_operation_type = file_operation_type
        self.file_path = file_path
        self.content = content
        self.my_file = None

    def operation(self):
        if self.file_operation_type == "w":
            self.write_mode()
        elif self.file_operation_type == "a":
            self.append_mode()
        elif self.file_operation_type == "r":
            self.read_mode()

    def write_mode(self):
        print("File has been overwritten with the content")
        self.my_file.write(self.content)

    def append_mode(self):
        print("Content appended to the end of the text:")
        self.my_file.write(f'\n{self.content}')

    def read_mode(self):
        print("Text from the file:")
        f = self.my_file.read()
        print(f)

    def __enter__(self):
        print("__enter__")
        try:
            self.my_file = open(self.file_path, self.file_operation_type)
            return self
        except FileNotFoundError as no_file_error:
            print("File path is incorrect:", no_file_error)
        except TypeError as type_err:
            print("TypeError occurred:", type_err)
        except AttributeError:
            print("There is no such attribute")
        except Exception as error:
            print("An error occurred:", error)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")
        if self.my_file:
            self.my_file.close()


with OperFiles("r", 'file_Kotiai_6.txt', 'text line e') as file_operation:
    file_operation.operation()