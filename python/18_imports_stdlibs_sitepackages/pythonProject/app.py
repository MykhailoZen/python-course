from flask import Flask, jsonify, request
from students import Student

app = Flask(__name__)

students = []


@app.route("/add_student", methods=["POST"])
def add_student():
    data = request.get_json()
    name = data.get("name")
    student_id = data.get("id")
    new_student = Student(name, student_id)
    students.append(new_student)
    return jsonify({"message": "Student added successfully"})


@app.route("/upd_student", methods=["POST"])
def upd_student():
    data = request.get_json()
    name = data.get("name")
    student_id = data.get("id")
    for student in students:
        if student.id == student_id:
            student.name = name
            return jsonify({"message": "Student name updated successfully"})


@app.route("/del_student", methods=["POST"])
def del_student():
    data = request.get_json()
    student_id = data.get("id")
    for i, student in enumerate(students):
        if student.id == student_id:
            del students[i]
            return jsonify({"message": "Student deleted successfully"})


@app.route("/get_students", methods=["GET"])
def get_students():
    student_data = [{"name": student.name, "id": student.id} for student in students]
    return jsonify(student_data)


if __name__ == "__main__":
    app.run(debug=True)
