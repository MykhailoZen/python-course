
students = {'Alan': 68,
            'Roslyn': 48,
            'Bertha': 50,
            'Sally': 95,
            'Rachel': 11,
            'John': 95,
            'Derek': 82,
            'Kevin': 34,
            'Michael': 31,
            'Richard': 12}

while True:
    input_value = input("Please enter student's name: ")
    if input_value == "Stop program":
        break
    elif input_value in students:
        print(f"Student {input_value} has {students[input_value]} points")
        break
    else:
        print("No such name here, try to enter another one")


