from flask import Flask, request, jsonify
from .lib.students_c import Student

app = Flask(__name__)


@app.route('/home')
def hello_world():
    return '<p>Hello, World!</p>'


@app.route('/store', methods=['POST'])
def store_data():
    """
    Endpoint to store or update data. Expects JSON data in the request body.
    """
    try:
        data = request.json  # Get JSON data from request
        # Assuming data contains a key 'key' to identify the entry
        student_id = data.get('id')
        if student_id is None:
            return jsonify({'error': 'Key not provided'}), 400
        student_name = data.get('name')
        if student_name is None:
            return jsonify({'error': 'Value not provided'}), 400
        #data_storage[student_id] = student_name
        student = Student(student_name, student_id)
        Student.student_list.append((student_id, student_name))
        return jsonify({'success': True}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/retrieve/<id>', methods=['GET'])
def retrieve_data(id):
    """
    Endpoint to retrieve data associated with a given key.
    """
    for student_id, student_name in Student.student_list:
        if student_id == id:
            return jsonify({'id': student_id, 'name': student_name}), 200
    return jsonify({'error': 'Id not found'}), 404

@app.route('/list', methods=['GET'])
def retrieve_all_data():
    """
    Endpoint get all students stored.
    """
    all_students = [{'id': student_id, 'name': student_name} for student_id, student_name in Student.student_list]
    return jsonify(all_students)

if __name__ == '__main__':
    app.run(debug=True)