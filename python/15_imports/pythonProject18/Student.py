class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def __repr__(self):
        return f"Name = {self.name} , ID = {self.student_id}"

