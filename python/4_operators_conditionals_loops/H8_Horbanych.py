studentbase = {
    'Alan': 68, 'Roslyn': 48, 'Bertha': 50, 'Sally': 95, 'Rachel': 11,
    'John': 95, 'Derek': 82, 'Kevin': 34,'Michael': 31, 'Richard': 12}

while True:
    student_name = (input("Enter student's name: ")).capitalize()
    if student_name == "Stop the program":
        break
    elif student_name in studentbase:
        print(f"Student {student_name} has {studentbase[student_name]} points.")
        break
    else:
        print(f"Student's name {student_name} is not present. Write the correct name or write: 'Stop the program' for exit")
