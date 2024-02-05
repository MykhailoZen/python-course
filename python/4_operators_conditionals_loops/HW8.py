student = {'Alan': 68, 'Roslyn': 48,
            'Bertha': 50, 'Sally': 95,
            'Rachel': 11, 'John': 95,
            'Derek': 82, 'Kevin': 34,
            'Michael': 31, 'Richard': 12}
for n in student:
    name = input("Enter the student's name: ")
    if name in student:
        print("Student " + str(name) + " has " + str(student[name]) + " points")
        break
    elif name == "Stop program":
        print ("Program terminated")
        break
    else:
        print("Wrong name, try again")