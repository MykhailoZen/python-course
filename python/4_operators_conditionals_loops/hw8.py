student_base = {
'Alan': 68, 'Roslyn': 48, 'Bertha': 50, 'Sally': 95, 'Rachel': 11, 'John': 95, 'Derek': 82, 'Kevin': 34, 'Michael': 31, 'Richard': 12
}

while True:
    name = input("Enter your name or enter 'Stop program' to exit: ")
    if name == "Stop program": #Check if Stop program was entered
        break
    elif name in student_base: #Check if name in student base
        print ('Student '+ name + ' has: ' + str(student_base[name]) + ' points')
    else:
        print(" Student not found. Enter another name: ")
