from flask import Flask, request, jsonify
from student import Student
import requests

app = Flask(__name__)

students = []

@app.route('/student', methods=['POST'])
def create_student():
    data = request.json
    new_student = Student(name=data['name'], id=data['id'])
    students.append(new_student)
    return jsonify({'message': 'Student created successfully'}), 201

@app.route('/student/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.json
    for student in students:
        if student.id == student_id:
            student.name = data.get('name', student.name)
            return jsonify({'message': 'Student updated successfully'}), 200
    return jsonify({'message': 'Student not found'}), 404


@app.route('/student/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students
    students = [student for student in students if student.id != student_id]
    return jsonify({'message': 'Student deleted successfully'}), 200


if __name__ == '__main__':
    app.run(debug=True)


    create_student_data = {'name': 'John Doe', 'id': 1}
    create_response = requests.post('http://127.0.0.1:5000/student', json=create_student_data)
    print('POST:', create_response.json())


    update_student_data = {'name': 'Updated Name'}
    update_response = requests.put('http://127.0.0.1:5000/student/1', json=update_student_data)
    print('PUT:', update_response.json())


    delete_response = requests.delete('http://127.0.0.1:5000/student/1')
    print('DELETE:', delete_response.json())
