from flask import Flask, request
from student import Student

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


students = []


@app.route('/student/create')
def student_create():
    data = request.json
    student = Student(name=data['name'], student_id=data['id'])
    students.append(student)
    return (f"Student has been added (name={student.name},"
            f"id={student.student_id})")


@app.route('/student/update/<id>')
def update_student(student_id):
    data = request.json
    for student in students:
        if student.student_id == student_id:
            name_old = student.name
            name_new = data['name']
            student.name = name_new
            return (f"Student (id={student_id}) has been updated"
                    f"(name_old={name_old},name_new={name_new})")
    return f"Student id [{student_id}] was not found"


@app.route('/student/delete/<id>')
def delete_student(student_id):
    data = request.json
    for student in students:
        if student.student_id == student_id:
            students.remove(student)
            return (f"Student has been deleted (name={student.name},"
                    f"id={student.student_id})")
    return f"Student id [{student_id}] was not found"
