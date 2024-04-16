from flask import Flask, request, jsonify
from Student import Student

app = Flask(__name__)

students = [
            Student("AAA", 1),
            Student("BBB", 2),
            Student("CCC", 3),
            Student("DDD", 4),
            Student("EEE", 5)
        ]


# Check all available students
@app.route("/")
def check_students():
    return jsonify([str(student) for student in students])


# Create new student with name and id and list the whole list for verification
@app.route('/students/add', methods=['POST'])
def create_student():
    data = request.get_json()
    new_student = Student(name=data['name'], student_id=data['student_id'])
    global students
    students.append(new_student)
    return jsonify(str(students)), 201


#  Update student data by ID
@app.route('/students/change/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()
    for student in students:
        if student.student_id == student_id:
            student.name = data.get('name', student.name)
            return jsonify(str(student)), 200
    return jsonify({'error': 'Student not found'}), 404


# Delete by ID
@app.route('/students/delete/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students
    students = [student for student in students
                if student.student_id != student_id]
    return jsonify({'message': 'Deleted }'}), 200
