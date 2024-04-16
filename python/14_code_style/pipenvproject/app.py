# app.py
import json

from flask import Flask, jsonify, request
from student import Student

app = Flask(__name__)

# Student data is stored in file 'students.json'
STUDENTS_FILE = "students.json"

# Initialize an empty list to store student objects
students = []


def load_students():
    global students
    try:
        with open(STUDENTS_FILE, "r") as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []


def save_students():
    with open(STUDENTS_FILE, "w") as file:
        json.dump(students, file)


# tested via postman GET http://127.0.0.1:5000/students
@app.route("/students", methods=["GET"])
def get_students():
    load_students()
    # Map 'id' to 'student_id' for consistency
    students_with_student_id = [
        {"name": student["name"], "student_id": student["student_id"]}
        for student in students
    ]
    return jsonify(students_with_student_id)


# How to test via postman:
# POST http://127.0.0.1:5000/students/1
# raw->json format input->{"name": "Aleksandr5","id": 5}
@app.route("/students", methods=["POST"])
def create_student():
    data = request.get_json()
    name = data.get("name")
    student_id = data.get("id")
    new_student = Student(name, student_id)
    students.append(new_student.__dict__)
    save_students()
    return jsonify({"message": "Student created successfully"}), 201


# How to test via postman:
# PUT http://127.0.0.1:5000/students/1
# raw->json format input->{"name": "Aleksandr5","new_student_id": <new student i>}
@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    load_students()
    data = request.get_json()
    new_student_id = data.get("new_student_id")

    if new_student_id is None:
        return jsonify({"message": "New student ID not provided"}), 400

    # Check if the new ID conflicts with existing IDs
    if any(student.get("student_id") == new_student_id for student in students):
        return jsonify({"message": "New student ID already exists"}), 400

    for student in students:
        if student.get("student_id") == student_id:
            student["student_id"] = new_student_id
            save_students()
            return jsonify({"message": "Student ID updated successfully"})
    return jsonify({"message": "Student not found"}), 404


# How to test via postman:
# DELETE http://127.0.0.1:5000/students/<student_id> (in my case 5 - http://127.0.0.1:5000/students/5 )
# raw->json format input->{"name": "Aleksandr5","new_student_id": <new student i>}
@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    load_students()
    for i, student in enumerate(students):
        if (
            student.get("student_id") == student_id
        ):  # Check 'student_id' instead of 'id'
            del students[i]
            save_students()
            return jsonify({"message": "Student deleted successfully"})
    return jsonify({"message": "Student not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
