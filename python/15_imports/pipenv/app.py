from flask import Flask, jsonify, request
from students import Student

app = Flask(__name__)

students = [
    Student("Pes Patron", 1),
    Student("Pan Kockyi", 2)
]
@app.route('/students', methods=['GET'])
def get_students():
    student_base = []
    for student in students:
        student_base.append({'student_name': student.name, 'id': student.student_id})
    return jsonify(student_base)

@app.route('/students', methods=['POST'])
def create_student():
    data = request.json
    if 'name' not in data or 'id' not in data:
        return jsonify({'error': 'Wrong Name or ID'})
    new_student = Student(name=data['name'], student_id=data['id'])
    students.append(new_student)
    return jsonify({' ': 'Student was added','student_name': data['name'], 'id': data['id']})

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.json
    for student in students:
        if student.student_id == student_id:
            student.name = data.get('name', student.name)
            student.student_id = data.get('id', student.student_id)
            return jsonify({' ': 'Student info was updated', 'student_name_new': data['name'], 'id_new': data['id'] })
    return jsonify({'error': 'Wrong student info was typed'})

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    for student in students:
        if student.student_id == student_id:
            students.remove(student)
            return jsonify({'message': 'Student deleted', 'deleted_student_id' : student_id})
    return jsonify({'error': 'Student not found'})

if __name__ == '__main__':
    app.run(debug=True)