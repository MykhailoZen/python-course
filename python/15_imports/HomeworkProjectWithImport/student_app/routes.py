from flask import Flask, request, jsonify
from student_app.students import Student
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    greet = """<h1>
    <pre>
    Baby Shark, doo-doo, doo-doo, doo-doo!
    Let's go hunt, doo-doo, doo-doo, doo-doo
    Run away, doo-doo, doo-doo, doo-doo
    It's the end, doo-doo, doo-doo, doo-doo</pre>
    </h1>"""
    body = """
    <body>
        <pre>
                                          ^`.                     o
     ^_              \  \                  o  o
     \ \             {   \                 o
     {  \           /     `~~~--__
     {   \___----~~'              `~~-_     ______          _____
      \                         /// a  `~._(_||___)________/___
      / /~~~~-, ,__.    ,      ///  __,,,,)      o  ______/    
      \/      \/    `~~~;   ,---~~-_`~= \ \------o-'            
                       /   /            / /
                      '._.'           _/_/
                                      ';|\           
        </pre>
    </body>
    """
    return greet + body


# List of students (initially empty)
students = []

# Create a new student
@app.route('/api/student', methods=['POST'])
def create_student():
    data = request.get_json()
    name = data['name']
    student_id = data['id']
    new_student = Student(name, student_id)
    students.append(new_student)
    return jsonify({'message': 'Student created successfully'}), 201

# Update student data by ID
@app.route('/api/student/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()
    for student in students:
        if student.id == student_id:
            student.name = data['name']
            return jsonify({'message': 'Student updated successfully'})
    return jsonify({'error': 'Student not found'}), 404

# Delete student by ID
@app.route('/api/student/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students
    students = [student for student in students if student.id != student_id]
    return jsonify({'message': 'Student deleted successfully'})
