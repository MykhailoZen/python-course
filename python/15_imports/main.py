from flask import Flask, jsonify, request
from student import Student

app = Flask(__name__)
app.json.sort_keys = False
students = []


@app.route("/", methods=["GET"])
def get_students():
    """
    Request and response with list of students
    :return: json with existed students
    """
    return jsonify(
        [{"name": student.name, "id": student.student_id} for student in students]
    )


@app.route("/create", methods=["POST"])
def create_student():
    """
    Request for adding new student by name. ID added automatically
    :return: message in json format about adding student
    """
    input_data = request.get_json()
    newbee = Student(input_data["name"])
    students.append(newbee)
    return jsonify({"Successfully added student": input_data["name"]}), 201


@app.route("/remove", methods=["DELETE"])
def remove_student():
    """
    Request for removing student by ID
    :return: json message about removing student or not found student
    """
    input_data = request.get_json()
    input_id = input_data["id"]
    for student in students:
        if student.student_id == input_id:
            students.remove(student)
            return jsonify("Successfully removed student"), 200

    return jsonify("Student not found"), 404


@app.route("/update", methods=["PUT"])
def update_student():
    """
    Request for updating student by ID
    :return: json message about updating student or not found student
    """
    input_data = request.get_json()
    input_id = input_data["id"]
    input_name = input_data["name"]
    for student in students:
        if student.student_id == input_id:
            student.name = input_name
            return jsonify("Successfully updated student"), 200

    return jsonify("Student not found"), 404
