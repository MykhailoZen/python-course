
dict = {'Alan': 68, 'Roslyn': 48, 'Bertha': 50, 'Sally': 95, 'Rachel': 11, 'John': 95, 'Derek': 82, 'Kevin': 34, 'Michael': 31, 'Richard': 12}

while True:
    name = input("Please, enter student's name: ")
    if name in dict:
        print(f"Student {name} has {dict[name]} points")
        break
    elif name == "Stop program":
        print("Stop program")
        break
    else:
        input("This is incorrect name, please, enter another one: ")