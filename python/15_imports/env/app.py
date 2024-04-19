from flask import Flask, request, jsonify
from students import Student

app = Flask(__name__)

# List of students.
students = [
    Student(name="Bob", student_id=1),
    Student(name="Allan", student_id=2),
    Student(name="Dog", student_id=3),
    Student(name="Cat", student_id=4),
    Student(name="Ally", student_id=5)
]

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify([str(student) for student in students])

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = next((student for student in students if student.student_id == student_id), None)
    if student:
        return jsonify(str(student))
    else:
        return jsonify({'error': 'Student not found'}), 404

@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    new_student = Student(name=data['name'], student_id=data['student_id'])
    students.append(new_student)
    return jsonify(str(new_student)), 201


@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()
    for student in students:
        if student.student_id == student_id:
            student.name = data.get('name', student.name)
            return jsonify(str(student)), 200
    return jsonify({'error': 'Student not found'}), 404


@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students
    students = [student for student in students if student.student_id != student_id]
    return jsonify({'message': 'Deleted successfully'}), 204


if __name__ == '__main__':
    app.run(debug=True)