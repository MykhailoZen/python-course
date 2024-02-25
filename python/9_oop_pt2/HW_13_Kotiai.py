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


"""Homework for week 9 rebased to class"""

class Area():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_rectangle_area(self):
        """2. This function should return the area of the rectangle,
        which is calculated as multiplication of length and width:"""
        rec_area = float(self.length) * float(self.width)
        print("Total rectangle area is equal to")
        return rec_area

ar = Area(4, 5)
print(ar.calculate_rectangle_area())


""" Homework for week 11 rebased to class"""
class LambdaFunc():
    def __init__(self, dic_origin='', number_list=''):
        self.dic_origin = dic_origin
        self.number_list = number_list
    def re(self):
        dic_flip = {x: y for y, x in self.dic_origin.items()}
        print(dic_flip)

    def copy_list(self):
        cp_number_list = [x for x in self.number_list]
        print(cp_number_list)

l = [x for x in range(10)]
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
la = LambdaFunc(d, '')
la.re()

l = [x for x in range(10)]
cp_num = LambdaFunc('', l)
cp_num.copy_list()











