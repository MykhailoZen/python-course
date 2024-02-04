#The dictionary with the Students grade

student_grade = {'Alan': 68, 'Roslyn': 48, 'Bertha': 50, 'Sally': 95, 'Rachel': 11,
                 'John': 95, 'Derek': 82, 'Kevin': 34, 'Michael': 31, 'Richard': 12}


name = input("Please enter the students name: " )
def st_grade(name):
    for i in student_grade.keys():
        # Repeat entering the student's name in case of attempt does not successful
        if name not in student_grade.keys() and name != "Stop program":
            name = input("This student doesn't exist. Please try again: ")
        # Stop program manually
        elif name == "Stop program":
            print(" ")
            print("The program has stopped!")
            break
        else:
            print(" ")
            # Return the following message Student <name> has <value> points and complete its execution
            print("Student %s has %s points" % (name, student_grade[name]))
            break

print(st_grade(name))
