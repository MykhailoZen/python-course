dict = {'Alan': 68, 'Roslyn': 48, 'Bertha': 50, 'Sally': 95, 'Rachel': 11, 'John': 95, 'Derek': 82, 'Kevin': 34, 'Michael': 31,
 'Richard': 12}


while True:
    item = input("""Enter name ('Stop program' - for exit): """)
    if item == "Stop program": #Check for exit
        break
    elif item in dict: #Search name in student base
        print('Student ' + item + ' has: ' + str(dict[item]) + ' points')
    else:
        print(" Student not found. Enter another name: ")


