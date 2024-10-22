student_grades = {'Alan': 68, 'Roslyn': 48, 'Bertha': 50, 'Sally': 95, 'Rachel': 11, 'John': 95, 'Derek': 82,
                  'Kevin': 34, 'Michael': 31, 'Richard': 12}
name = input("Enter the student's name:")

while name != "Stop program" and name not in student_grades:
    name = input("Not found, please try again or type \"Stop program\" to exit.")
else:
    if name != "Stop program":
        print(f"Student {name} has {student_grades[name]} points")
