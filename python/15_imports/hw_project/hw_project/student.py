# student.py

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.id = student_id

    def __repr__(self):
        return f"<Student name={self.name} id={self.id}>"
