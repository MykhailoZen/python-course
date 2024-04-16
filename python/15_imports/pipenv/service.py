class Student:
    def __init__(self, student_name, student_id):
        self.student_name = student_name
        self.student_id = student_id

    def __repr__(self):
        return f"Student(name='{self.student_name}', student_id={self.student_id})"

