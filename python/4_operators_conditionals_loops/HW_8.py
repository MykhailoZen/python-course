# 2. Practice
# Create a program that will help to find out the student's points.
# The program prompts you to enter the student's name and, if successful,
# returns the following message Student <name> has <value> points and complete its execution.
# If such a name is not in the dictionary, the program should inform about this and offer to enter another name.
# There should also be a way to end the program by typing Stop program.
#
# Student grades (data for homework)
# {'Alan': 68, 'Roslyn': 48, 'Bertha': 50, 'Sally': 95, 'Rachel': 11, 'John': 95, 'Derek': 82, 'Kevin': 34,
# 'Michael': 31, 'Richard': 12}

database = {
    'Alan': 68, 'Roslyn': 48, 'Bertha': 50, 'Sally': 95, 'Rachel': 11,
    'John': 95, 'Derek': 82, 'Kevin': 34,'Michael': 31, 'Richard': 12}

while True:
    student_name = (input("Enter student's name: ")).capitalize()
    if student_name.lower() == "stop":
        break
    elif student_name in database:
        print(f"Student {student_name} has {database[student_name]} points.")
        break
    else:
        print(f"Student's name {student_name} is absent. Enter correct name or write: 'stop' if you want exit")