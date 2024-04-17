from flask import Flask, request, jsonify
from student import Student

# Create a new Python project and add requirements.txt with needed imports (e.g. flask)
# Create venv for pipenv install imports from requirements.txt
# Create a simple API fask app which designed to store data about students:
#  Create class Student in a separate module. (should have fields: name, id)
# The main file of the app should have a list of students and next API endpoints: create new student, update student
# data by ID, delete by ID.

app = Flask(__name__)

students = [
    Student('Barack', 1),
    Student('Obama', 2),
    Student('Winston', 3),
    Student('Churchill', 4)
]


@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    name = data.get('name')
    id = data.get('id')

    if not name or not id:
        return jsonify({'error': 'Name and ID not provided'}), 400

    new_student = Student(name, id)
    students.append(new_student)
    return jsonify({'message': 'Student created'})


@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()
    name = data.get('name')

    student = next((student for student in students if student.id == id), None)

    if not student:
        return jsonify({'error': 'Student not found'}), 404

    student.name = name
    return jsonify({'message': 'Student updated'}), 201


@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    global students
    students = [student for student in students if student.id != id]

    return jsonify({'message': 'Student deleted successfully'})


if __name__ == '__main__':
    app.run()


