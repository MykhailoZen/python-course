class Student:
    def __init__(self, name, student_id):
        self._name = name
        self._student_id = student_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def student_id(self):
        return self._student_id
