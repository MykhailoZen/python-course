from flask import Flask, jsonify, request
from student import Student

app = Flask(__name__)
students = []

@app.route('/students', methods=['POST'])
def create_student():
    data = request.json
    name = data.get('name')
    student_id = data.get('id')
    if name is None or student_id is None:
        return jsonify({'error': 'Name and ID are required'}), 400
    student = Student(name, student_id)
    students.append(student)
    return jsonify({'message': 'Student created successfully'})

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.json
    name = data.get('name')
    if name is None:
        return jsonify({'error': 'Name is required'}), 400
    for student in students:
        if student.student_id == student_id:
            student.name = name
            return jsonify({'message': 'Student updated successfully'})
    return jsonify({'error': 'Student not found'}), 404

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    for i, student in enumerate(students):
        if student.student_id == student_id:
            del students[i]
            return jsonify({'message': 'Student deleted successfully'})
    return jsonify({'error': 'Student not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
