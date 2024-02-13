student_grades = {
    'Alan': 68, 'Roslyn': 48, 'Bertha': 50, 'Sally': 95, 'Rachel': 11,
    'John': 95, 'Derek': 82, 'Kevin': 34, 'Michael': 31, 'Richard': 12
}


def find_student_points():
    while True:
        name = input("Enter student's name (or type 'Stop program' to end): ")

        if name.lower() == 'stop program':
            print("Program terminated.")
            break

        if name in student_grades:
            points = student_grades[name]
            print(f"Student {name} has {points} points.")
        else:
            print(f"Student {name} not found. Please enter another name.")


find_student_points()