students = {'Alan': 68, 'Roslyn': 48, 'Bertha': 50, 'Sally': 95, 'Rachel': 11, 'John': 95, 'Derek': 82, 'Kevin': 34, 'Michael': 31, 'Richard': 12}

while True:
    name = input("Enter the student's name (or type 'Stop program' to end): ")

    if name.lower() == 'stop program':
        print('Program stopped.')
        break

    if name in students:
        print('Student ' + name + ' has ' + str(students[name]) + ' points')
        break

    else:
        print('Student not found. Please enter another name.')

