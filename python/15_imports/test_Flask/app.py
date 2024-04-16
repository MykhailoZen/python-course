from flask import Flask, jsonify, request

from student import Student

app = Flask(__name__)
students = []


@app.route("/students", methods=["GET", "POST"])
def handle_students():
    if request.method == "GET":
        return get_students()
    elif request.method == "POST":
        return create_student()


def create_student():
    data = request.json
    new_student = Student(data.get("name"))
    students.append(new_student)
    return jsonify({"message": "Student created successfully"}), 201


def get_students():
    return jsonify([{"name": student.name, "id": student.id} for student in students])


@app.route("/students/<int:id>", methods=["GET", "PUT", "DELETE"])
def handle_student(id):
    if request.method == "PUT":
        return update_student(id)
    elif request.method == "GET":
        return get_student_name(id)
    elif request.method == "DELETE":
        return delete_student(id)


def update_student(id):
    data = request.json
    student_name = data.get("name")
    if student_name is not None:
        for student in students:
            if student.id == id:
                student.name = student_name
                return jsonify({"message": "Student updated successfully"}), 200
        return jsonify({"message": "Student not found"}), 404
    else:
        return jsonify({"error": "Name field is missing in request data"}), 400


def get_student_name(id):
    for student in students:
        if student.id == id:
            return jsonify({"id": id, "name": student.name}), 200
    return jsonify({"error": "Student not found"}), 404


def delete_student(id):
    for student in students:
        if student.id == id:
            students.remove(student)
            return jsonify({"message": "Student deleted successfully"}), 200
    return jsonify({"error": "Student not found"}), 404
