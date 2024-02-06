student_data = {'Alan': 68, 'Roslyn': 48, 'Bertha': 50, 'Sally': 95,
                'Rachel': 11, 'John': 95, 'Derek': 82, 'Kevin': 34,
                'Michael': 31, 'Richard': 12}

while True:

    print("Student's name:")
    student_input = input()

    if student_input == 'Stop program':
        print("Program stopped")
        exit()

    if student_input in student_data:
        print("Student " + student_input + " has "
              + str(student_data[student_input]) + " points")
        break
    else:
        print("Student not found. Please try again.")