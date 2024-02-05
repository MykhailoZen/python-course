students = {'Alan': 68, 'Roslyn': 48, 'Bertha': 50, 'Sally': 95, 'Rachel': 11, 'John': 95, 'Derek': 82, 'Kevin': 34, 'Michael': 31, 'Richard': 12}

def student_find():
    while True:
        name = input("Please write the name of the student (type 'Stop program' to end): ")

        if name == "Stop program":
            print("Program stopped.")
            break
        elif name not in students:
            print("Student not found. Try again.")

        else:
            print(f"Student {name} has {students[name]} points.")
            break


student_find()