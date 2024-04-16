import uuid


class Student:
    """
    Class implementing student
    """

    def __init__(self, name: str):
        """
        Initialization of student object
        :param name: student name
        """
        self.name = name
        self.student_id = str(uuid.uuid4())
