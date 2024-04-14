from flask import Flask, request, jsonify
from app import Student, StudentManager

app = Flask(__name__)

"""The main file of the app should have a list of students"""
students = [
            Student("Alice", 1),
            Student("Bob", 2),
            Student("Charlie", 3)
        ]

student_manager = StudentManager(students)

"""API endpoint: create new student"""
@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    name = data.get('name')
    student_id = data.get('id')

    if not name or not student_id:
        return jsonify({'error': 'Name and ID are required'}), 400

    student = student_manager.create_student(name, student_id)
    if not student:
        return jsonify({'error': 'Student with this ID already exists'}), 400

    return jsonify({'id': student.student_id, 'name': student.name}), 201

"""API endpoint: update student data by ID"""
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()
    name = data.get('name')

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    student = student_manager.update_student(student_id, name)
    if not student:
        return jsonify({'error': 'Student not found'}), 404

    return jsonify({'id': student.student_id, 'name': student.name})

"""API endpoint:  delete student by ID by ID"""
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    success = student_manager.delete_student(student_id)
    if not success:
        return jsonify({'error': 'Student not found'}), 404

    return jsonify({'message': 'Student deleted'})

if __name__ == '__main__':
    app.run(debug=True)