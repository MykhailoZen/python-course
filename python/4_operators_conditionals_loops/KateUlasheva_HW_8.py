student_names = {
    'Alan': 68, 'Roslyn': 48, 'Bertha': 50, 'Sally': 95,
    'Rachel': 11, 'John': 95, 'Derek': 82, 'Kevin': 34,
    'Michael': 31, 'Richard': 12
}

def find_student_points():
    while True:
        name = input("Enter the student's name (or 'Stop program' to end): ")
        if name == 'Stop program':
            print("Program stopped.")
            break
        elif name in student_names:
            points = student_names[name]
            print("Student {} has {} points.".format(name, points))
        else:
            print("There is no student with this name. Enter another name.")

find_student_points()