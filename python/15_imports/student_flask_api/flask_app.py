# flask_app.py
from flask import Flask, request, jsonify
from student import Student

app = Flask(__name__)

students = []


@app.route('/')
def hello():
    return 'Hello, World!'

@app.post('/test')
def process_post():
    data = request.get_json()
    return f"data {data}"

# @app.post('/students')
# def create_student():
 #   data = request.json
  #  student = Student(name=data[0], student_id=data[1])
   # students.append(student)
    # return students

@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    student = Student(name=data['name'], student_id=data['id'])
    students.append(student)
    return jsonify({'message': 'Student created successfully'}), 201


@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()
    for student in students:
        if student.student_id == student_id:
            student.name = data['name']
            return jsonify({'message': 'Student updated successfully'})
    return jsonify({'error': 'Student not found'}), 404


@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students
    students = [student for student in students if student.student_id != student_id]
    return jsonify({'message': 'Student deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)
