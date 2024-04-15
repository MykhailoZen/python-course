import requests

BASE_URL = 'http://127.0.0.1:5000'


def get_students():
    response = requests.get(f'{BASE_URL}/students')
    if response.status_code == 200:
        return response.json()
    else:
        return f'Error: {response.text}'


def create_student(name, student_id):
    data = {'name': name, 'id': student_id}
    response = requests.post(f'{BASE_URL}/students', json=data)
    if response.status_code == 201:
        return 'Student created successfully'
    else:
        return f'Error: {response.text}'


def update_student(student_id, name):
    data = {'name': name}
    response = requests.put(f'{BASE_URL}/students/{student_id}', json=data)
    if response.status_code == 200:
        return 'Student updated successfully'
    else:
        return f'Error: {response.text}'


def delete_student(student_id):
    response = requests.delete(f'{BASE_URL}/students/{student_id}')
    if response.status_code == 200:
        return 'Student deleted successfully'
    else:
        return f'Error: {response.text}'


if __name__ == '__main__':
    #  Verification usage
    print("List of Students:")
    print(get_students())

    print("\nCreating a new student...")
    print(create_student('Kate', 2))

    print("\nList of Students after adding new student:")
    print(get_students())

    print("\nUpdating student with ID 1...")
    print(update_student(1, 'Ogha'))

    print("\nList of Students after updating:")
    print(get_students())

    print("\nDeleting student with ID 1...")
    print(delete_student(2))

    print("\nList of Students after deleting:")
    print(get_students())
