from flask import Flask, request, jsonify
from service import Student

app = Flask(__name__)

students = [
    Student(student_name="Sally", student_id=0),
    Student(student_name="Sally", student_id=1),
    Student(student_name="Sally", student_id=2),
    Student(student_name="Sally", student_id=3)
    ]

@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    new_student = Student(student_name=data['name'], student_id=data['student_id'])
    students.append(new_student)
    return jsonify(str(new_student)), 201

@app.route('/api/student/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()
    for student in students:
        if student.id == student_id:
            student.name = data['name']
            return jsonify({'message': 'Student updated successfully'})
    return jsonify({'error': 'Student not found'}), 404

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = next((student for student in students if student.student_id == student_id), None)
    if student:
        return jsonify({
            'student_name': student.student_name,
            'student_id': student.student_id
        })
    else:
        return jsonify({'error': 'Student not found'}), 404

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students
    students = [student for student in students if student.student_id != student_id]
    return jsonify({'message': 'Deleted successfully'}), 204

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify([str(student) for student in students])