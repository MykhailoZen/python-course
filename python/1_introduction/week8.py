students_set = {'Alan': 68, 'Roslyn': 48, 'Bertha': 50, 'Sally': 95, 'Rachel': 11, 'John': 95, 'Derek': 82, 'Kevin': 34, 'Michael': 31, 'Richard': 12}

while True:
    student_req = input("enter students name:")
    if student_req == "Stop program":
            print ("program stopped")
            break
    elif student_req in students_set:
            print("Student ", student_req, "has ", students_set[student_req], "points and complete its execution")
    elif student_req not in students_set:
            print ("Student not exist, enter another name")

