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
    if data.get("name") is not None:
        new_student = Student(data.get("name"))
        students.append(new_student)
        return jsonify({"message": "Student created successfully"}), 201
    else:
        return jsonify({"error": "Name is required."}), 400


def get_students():
    return jsonify([{"name": student.name, "id": student.id} for student in students])


@app.route("/students/<int:id>", methods=["GET", "PUT", "DELETE"])
def handle_student(id):
    student = find_student_by_id(id)
    if request.method == "PUT":
        if student:
            return update_student(student)
        else:
            return jsonify({"message": "Student not found"}), 404
    elif request.method == "GET":
        if student:
            return get_student_name(student)
        else:
            return jsonify({"error": "Student not found"}), 404
    elif request.method == "DELETE":
        if student:
            return delete_student(student)
        else:
            return jsonify({"error": "Student not found"}), 404


def find_student_by_id(id):
    for student in students:
        if student.id == id:
            return student
    return None


def update_student(student):
    data = request.json
    student_name = data.get("name")
    if student_name is not None:
        student.name = student_name
        return jsonify({"message": "Student updated successfully"}), 200
    else:
        return jsonify({"error": "Name field is missing in request data"}), 400


def get_student_name(student):
    return jsonify({"id": student.id, "name": student.name}), 200


def delete_student(student):
    students.remove(student)
    return jsonify({"message": "Student deleted successfully"}), 200
