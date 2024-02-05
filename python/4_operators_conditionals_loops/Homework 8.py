student_grades = {'Alan': 68, 'Roslyn': 48, 'Bertha': 50, 'Sally': 95, 'Rachel': 11, 'John': 95, 'Derek': 82, 'Kevin': 34, 'Michael': 31, 'Richard': 12}
def find_student_points():
    while True:
        student_name = input("Enter student's name (or type 'Stop program' to end): ")
        if student_name.lower() == 'stop program':
            print("Program stopped.")
            break
        if student_name in student_grades:
            points = student_grades[student_name]
            print("Student {} has {} points.".format(student_name, points))
        else:
            print("Student not found. Please enter another name.")
find_student_points()


