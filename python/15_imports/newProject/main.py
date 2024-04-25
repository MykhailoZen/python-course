from flask import Flask, jsonify, request
from students import Student

app = Flask(__name__)

students = [
    Student("Bobby", 1),
    Student("Betty", 2),
    Student("Chris", 3),
    Student("Charlie", 4),
    Student("Marry", 5),
]


@app.route('/students', methods=['GET'])
def get_students():
    return jsonify([{'name': student.name, 'id': student.student_id} for student in students])


@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    name = data.get('name')
    student_id = data.get('id')

    if not name or not student_id:
        return jsonify({'error': 'Name and ID are required!'}), 400

    for student in students:
        if student.student_id == student_id:
            return jsonify({'error': 'Student ID already exists!'}), 400

    student = Student(name, student_id)
    students.append(student)

    return jsonify({'message': 'Student created successfully!'}), 200


@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()
    name = data.get('name')

    for student in students:
        if student.student_id == student_id:
            student.name = name
            return jsonify({'message': 'Student updated successfully!'}), 200

    return jsonify({'error': 'Student not found!'}), 404


@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    for student in students:
        if student.student_id == student_id:
            students.remove(student)
            return jsonify({'message': 'Student deleted successfully!'}), 200

    return jsonify({'error': 'Student not found!'}), 404


if __name__ == '__main__':
    app.run(debug=True)