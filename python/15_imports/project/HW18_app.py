from flask import Flask, request, jsonify
from HW18 import Student

application = Flask(__name__)

students = []


@application.route("/")
def index():
    return "Welcome to the Student API!"


@application.route("/students", methods=["GET", "POST"])
def all_students():
    """
    GET: Retrieves a list of all students.
    POST: Creating of a new student.
    """
    if request.method == "GET":
        return jsonify([student.__dict__ for student in students])
    else:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Some fields are missed"}), 400

        for student in students:
            if student.student_id == data["student_id"]:
                return jsonify({"error": "ID is already exist. Try another one"}), 409

        new_student = Student(data["student_name"], data["student_id"])
        students.append(new_student)
        return jsonify({"message": "Student successfully created"}), 201


@application.route("/students/<int:student_id>", methods=["GET", "PUT", "DELETE"])
def student_by_id(student_id):
    """
    GET: Retrieves a student by ID.
    PUT: Updating of a student's data.
    DELETE: Deletes a student by ID.
    """
    student = next((s for s in students if s.student_id == student_id), None)
    if student is None:
        return jsonify({"error": "Student not found"}), 404

    if request.method == "GET":
        return jsonify(student.__dict__)
    elif request.method == "PUT":
        # Validate request data
        data = request.get_json()
        if not data or not data.get("student_name"):
            return jsonify({"error": "Missing required field (name)"}), 400

        student.name = data["student_name"]
        return jsonify({"message": "Student updated successfully"})
    else:  # DELETE
        students.remove(student)
        return jsonify({"message": "Student deleted successfully"})


if __name__ == "__main__":
    application.run(debug=True)

