from flask import Flask, request
import json
from student import Student

app = Flask(__name__)


# Added few students for testing purpose
students = [
    Student("James Bond", 1),
    Student("John Smith", 2),
]


@app.route('/students', methods=['GET'])
def get_students():
    student_list = []
    for student in students:
        student_data = {'name': student.name, 'id': student.student_id}
        student_list.append(student_data)
    return json.dumps(student_list)


@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    name = data.get('name')
    student_id = data.get('id')
    if not name or not student_id:
        return json.dumps({'error': 'Please provide id and name'}), 400
    student = Student(name, student_id)
    students.append(student)
    return json.dumps({'message': 'Student was added'}), 201


@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()
    name = data.get('name')
    index = next(
        (i for i, s in enumerate(students) if s.student_id == student_id),
        None)
    if index is None:
        return json.dumps({'error': 'Student not found'}), 404
    if name:
        students[index].name = name
    return json.dumps({'message': 'Student updated successfully'})


@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    for i, s in enumerate(students):
        if s.student_id == student_id:
            del students[i]
            return json.dumps({'message': 'Student deleted successfully'})
    return json.dumps({'error': 'Student not found'}), 404


if __name__ == '__main__':
    app.run(debug=False)
