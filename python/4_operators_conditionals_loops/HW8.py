students = {'Alan': 68, 'Roslyn': 48, 'Bertha': 50, 'Sally': 95, 'Rachel': 11, 'John': 95,
            'Derek': 82, 'Kevin': 34, 'Michael': 31, 'Richard': 12}

while True:
     # enter the student's name
    name = input("Enter the student's name or end the program by typing 'Stop program': ")
    # if name from dictionary, print points
    if name in students:
        value = students[name]
        print("Student " + name + " has " + str(value) + " points")
    # if user stop program
    elif name == "Stop program":
        print("Program stopped")
        break
    # if name or command entered incorrect
    else:
        print("Such a name is not found, please enter name correctly or end the program by typing 'Stop program'")
