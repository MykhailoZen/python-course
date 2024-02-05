
students = {'Alan': 68, 'Roslyn': 48, 'Bertha': 50, 'Sally': 95, 'Rachel': 11, 'John': 95, 'Derek': 82, 'Kevin': 34, 'Michael': 31, 'Richard': 12}

while True:
    user_input = input("Please, enter student name: ")
    if user_input == "Stop program":
        break
    elif user_input in students:
        print(f"Student {user_input} has {students[user_input]} points")
        break
    else:
        print(f"There is no student with name {user_input}. You can stop the program by typing 'Stop program'.")
