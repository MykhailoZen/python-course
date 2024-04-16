
from flask import Flask, jsonify, request
from students import Student

app = Flask(__name__)
students = []

@app.post('/students')
def create_std():
    data = request.json
    name, _id = data.get('name'), data.get('id')
    students.append(Student(name, id))
    return jsonify



@app.delete('/students/<int:id>')
def delete_std(_id):
    data = request.json
    name, _id = data.get('name'), data.get('id')
    students.remove(Student(name, id))
    return jsonify

