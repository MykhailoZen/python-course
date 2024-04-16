class Student:
    id = 1

    def __init__(self, name):
        self.name = name
        self.id = Student.id
        Student.id += 1
