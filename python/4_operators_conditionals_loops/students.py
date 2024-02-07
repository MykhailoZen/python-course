students = {'Alan': 68, 'Roslyn': 48, 'Bertha': 50, 'Sally': 95, 'Rachel': 11, 'John': 95, 'Derek': 82, 'Kevin': 34,
            'Michael': 31, 'Richard': 12}


while True:
    student = str(input("Student name is: "))
    if student in students:
        points = students[student]
        print("Student {} has {} points.".format(student, points))
        break
    elif student == "Stop program":
        print("Stopped")
        break
    else:
        print("Name not found. Please enter another name.")
