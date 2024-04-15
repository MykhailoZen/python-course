from flask import Flask, jsonify, request
from student import Student

app = Flask(__name__)

# List of students
students = []


@app.route('/students', methods=['GET'])
def get_students():
    return jsonify([{'name': student.name, 'id': student.id} for student in students])


@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    name = data.get('name')
    student_id = data.get('id')
    if not name or not student_id:
        return jsonify({'error': 'Both name and id are required'}), 400
    new_student = Student(name, student_id)
    students.append(new_student)
    return jsonify({'message': 'Student created successfully'}), 201


@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()
    name = data.get('name')
    if not name:
        return jsonify({'error': 'Name is required'}), 400
    for student in students:
        if student.id == student_id:
            student.name = name
            return jsonify({'message': 'Student updated successfully'})
    return jsonify({'error': 'Student not found'}), 404


@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    for i, student in enumerate(students):
        if student.id == student_id:
            del students[i]
            return jsonify({'message': 'Student deleted successfully'})
    return jsonify({'error': 'Student not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
