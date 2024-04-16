# app.py

from flask import Flask, jsonify, request
from student import Student

app = Flask(__name__)
students = []

@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    new_student = Student(name=data['name'], student_id=data['id'])
    students.append(new_student)
    return jsonify({'student': repr(new_student)}), 201

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()
    for student in students:
        if student.id == student_id:
            student.name = data['name']
            return jsonify({'student': repr(student)}), 200
    return jsonify({'error': 'Student not found'}), 404

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students
    students = [student for student in students if student.id != student_id]
    return jsonify({'message': 'Student deleted'}), 200

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    for student in students:
        if student.id == student_id:
            return jsonify({'student': repr(student)}), 200
    return jsonify({'error': 'Student not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
