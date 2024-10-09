students = {'Alan': 68,
            'Roslyn': 48,
            'Bertha': 50,
            'Sally': 95,
            'Rachel': 11,
            'John': 95,
            'Derek': 82,
            'Kevin': 34,
            'Michael': 31,
            'Richard': 12}

student_in = input('Type student name: ')

while student_in != "Stop program":
    if student_in in students:
        for key, value in students.items():
            if key == student_in:
                print(f'Student {key} has {value} points.')
        break
    else:
        print(f'There are no such student in the Dictionary.')
        student_in = input('Type student name again please: ')
