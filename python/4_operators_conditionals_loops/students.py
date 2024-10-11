students = {'Alan': 68, 'Roslyn': 48, 'Bertha': 50, 'Sally': 95, 'Rachel': 11, 'John': 95, 'Derek': 82, 'Kevin': 34, 'Michael': 31, 'Richard': 12}

to_continue = True

while to_continue:
    name = input("Enter student's name: ").capitalize()

    if name.lower() == "exit":
        to_continue = False
        break

    if name in students.keys():
        print(f"Student {name} has {students[name]} points")
    else:
        print(f"No student {name} in the list")
