from flask import Flask, jsonify, request
from class_students import Student

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


students_list = []


@app.route('/students', methods=['GET'])
def get_students():
    return jsonify([{'name': student.name, 'id': student.id} for student in students_list]), 200


@app.route('/students', methods=['POST'])
def create_new_student():
    data = request.get_json()
    name = data.get('name')
    student_id = data.get('id')
    for student in students_list:
        if student.id == student_id:
            return jsonify({'error': 'Student with this ID already exists'}), 400
    student = Student(name, student_id)
    students_list.append(student)
    return jsonify({'message': 'Student created'}), 201


@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()
    name = data.get('name')
    for student in students_list:
        if student.id == student_id:
            student.name = name
            return jsonify({'message': 'Student updated'}), 200
    return jsonify({'message': 'Student not found'}), 404


@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students_list
    students_list = [student for student in students_list if student.id != student_id]
    return jsonify({'message': 'Student deleted'}), 200


if __name__ == '__main__':
    app.run(debug=True)



