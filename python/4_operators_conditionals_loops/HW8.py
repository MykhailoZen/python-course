students = {'Alan': 68, 'Roslyn': 68, 'Bertha': 50, 'Sally': 95, 'Rachel': 11, 'John': 95,
            'Derek': 82, 'Kevin': 34, 'Michael': 31,'Richard': 12}

print("Hello! This program helps you to find out the student's points. Please enter the name of the student below."
      "If you want to stop the program enter 'Stop program'")


def search_name():
    name = input("Student name: ")
    if name in students:
        print("Student " + name + " has", str(students[name]) + " points")
    elif name == "Stop program":
        exit(0)
    elif name == "":
        print("Please try again.")
        search_name()
    else:
        print(name + " is not in the list. Please try again.")
        search_name()


search_name()
