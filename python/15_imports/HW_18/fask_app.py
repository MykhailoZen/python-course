from flask import Flask, jsonify, request

from class_Student import Student

app = Flask(__name__)
students = []


@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)


@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    student = Student(data['name'], data['id'])
    students.append(student.__dict__)
    return jsonify(student.__dict__)


@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()
    for student in students:
        if student['id'] == id:
            student['name'] = data['name']
            return jsonify(student)
    return jsonify({'message': 'Student not found'}), 404


@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    global students
    students = [student for student in students if student['id'] != id]
    return jsonify({'message': 'Student deleted'})


if __name__ == '__main__':
    app.run(debug=True)
