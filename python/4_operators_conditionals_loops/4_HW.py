student_grades = {'Alan': 68, 'Roslyn': 48, 'Bertha': 50, 'Sally': 95, 'Rachel': 11, 'John': 95, 'Derek': 82, 'Kevin': 34, 'Michael': 31, 'Richard': 12}

entered_name = input("Enter student's name to get their grade: ")

while entered_name not in student_grades:
    if entered_name == 'Stop program':
        break
    entered_name = input("You have entered incorrect name. Enter proper student's name to get their grade: ")
else:
    print(f'Student {entered_name} has {student_grades[entered_name]} points')
