from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data storage (you can replace this with a database)
data_storage = {}


class Student:
    def __init__(self, student_name, student_id):
        self.student_name = student_name
        self.student_id = student_id


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
        data_storage[student_id] = student_name
        return jsonify({'success': True}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/retrieve/<id>', methods=['GET'])
def retrieve_data(id):
    """
    Endpoint to retrieve data associated with a given key.
    """
    if id in data_storage:
        return jsonify({'id': id, 'name': data_storage[id]}), 200
    else:
        return jsonify({'error': 'Id not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)