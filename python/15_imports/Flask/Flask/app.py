from flask import Flask, request, jsonify
from student import Student

app = Flask(__name__)

students = [
    Student(student_id=1, student_name='Anton'),
    Student(student_id=2, student_name='Pavlo'),
    Student(student_id=3, student_name='Oleksandr')
]


@app.route("/")
def welcome():
    description = '''<h1>Instructions HOMEWORK 18</h1>
                    <b>Practice</b><br><br>
                    1. Create a new Python project and add requirements.txt with needed imports (e.g. flask)<br>
                    2. Create venv for pipenv install imports from requirements.txt<br>
                    3. Create a simple API fask app which designed to store data about students:
                        <ul>
                            <li>
                                Create class Student in a separate module. (should have fields: name, id)
                            </li>
                            <li> 
                                The main file of the app should have a list of students and next API endpoints: 
                                create new student, update student data by ID, delete by ID.
                            </li>
                        </ul>'''
    return description


@app.route('/students', methods=['GET'])
def get_students():
    if students:
        return jsonify([{'student_name': student.student_name,
                         'student_id': student.student_id} for student in students]), 200
    else:
        return jsonify({'message': 'Students not found'}), 404


@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = next((student for student in students if student.student_id == student_id), None)

    if student:
        return jsonify({'student_name': student.student_name, 'student_id': student.student_id}), 200
    else:
        return jsonify({'message': 'Student not found'}), 404


@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    get_student_id = data.get('id')
    get_student_name = data.get('name')

    if get_student_id is None or get_student_name is None:
        return jsonify({'message': 'Name or ID are required'}), 400

    if not get_student_id or not get_student_name:
        return jsonify({'message': 'Name or ID can not empty'}), 400

    new_student = Student(get_student_id, get_student_name)
    students.append(new_student)
    return jsonify({'message': 'Student created successfully'}), 201


@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()
    get_student_name = data.get('name')

    if get_student_name is None:
        return jsonify({'message': 'Name is required'}), 400

    for student in students:
        if student.student_id == student_id:
            student.student_name = get_student_name
            return jsonify({'message': 'Student data updated successfully'})
    return jsonify({'message': 'Student not found'}), 404


@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students
    students = [student for student in students if student.student_id != student_id]
    return jsonify({'message': 'Student deleted successfully'}), 200


if __name__ == '__main__':
    app.run(debug=True)