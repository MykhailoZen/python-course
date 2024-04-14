class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

class StudentManager:
    def __init__(self, students):
        self.students = students


    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def create_student(self, name, student_id):
        if self.find_student_by_id(student_id):
            return None
        student = Student(name, student_id)
        self.students.append(student)
        return student

    def update_student(self, student_id, new_name):
        student = self.find_student_by_id(student_id)
        if not student:
            return None
        student.name = new_name
        return student

    def delete_student(self, student_id):
        student = self.find_student_by_id(student_id)
        if not student:
            return False
        self.students.remove(student)
        return True

