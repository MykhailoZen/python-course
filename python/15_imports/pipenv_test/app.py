from flask import Flask, request, jsonify
from student import Student

app = Flask(__name__)

students = [
    Student('Joey', 1),
    Student('Chandler', 2),
    Student('Monica', 3),
    Student('Ross', 4),
    Student('Phoebe', 5),
    Student('Rachel', 6)
]


@app.route('/get-student/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = next((student for student in students if student.student_id == int(student_id)), None)
    if student:
        return jsonify({'name': student.name, 'id': student.student_id}), 200
    else:
        return jsonify({'message': 'Student not found'}), 404


@app.route('/create-student', methods=['POST'])
def create_student():
    data = request.get_json()
    if 'name' not in data:
        return jsonify({'message': 'Missing name in request body'}), 400

    if 'id' in data:
        new_id = data['id']
        if any(student.student_id == new_id for student in students):
            return jsonify({'message': 'A student with this id already exists'}), 400
    else:
        new_id = max(student.student_id for student in students) + 1 if students else 1

    new_student = Student(data['name'], new_id)
    students.append(new_student)
    return jsonify({'name': new_student.name, 'id': new_student.student_id}), 201


@app.route('/update-student/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()
    if 'name' not in data:
        return jsonify({'message': 'Missing name in request body'}), 400

    student = next((student for student in students if student.student_id == student_id), None)
    if not student:
        return jsonify({'message': 'Student not found'}), 404

    student.name = data['name']
    return jsonify({'name': student.name, 'id': student.student_id}), 200


@app.route('/delete-student/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = next((student for student in students if student.student_id == int(student_id)), None)
    if student:
        return jsonify({'message': 'Student deleted successfully'}), 200
    else:
        return jsonify({'message': 'Student not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
