class Student:
    def __init__(self, name, student_id):
        self._name = name
        self._student_id = student_id

    @property
    def name(self):
        return self._name

    @property
    def student_id(self):
        return self._student_id
