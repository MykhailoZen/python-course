""" Create a program that will help to find out the student's points.
The program prompts you to enter the student's name and, if successful, returns the following
message Student <name> has <value> points and complete its execution.

If such a name is not in the dictionary, the program should inform about this and offer to enter another name.

There should also be a way to end the program by typing Stop program.

Student grades (data for homework)
{'Alan': 68, 'Roslyn': 48, 'Bertha': 50, 'Sally': 95, 'Rachel': 11,
 'John': 95, 'Derek': 82, 'Kevin': 34, 'Michael': 31, 'Richard': 12} """



grades = {
    'Alan': 68, 'Roslyn': 48, 'Bertha': 50, 'Sally': 95, 'Rachel': 11,
    'John': 95, 'Derek': 82, 'Kevin': 34,'Michael': 31, 'Richard': 12}

while True:
    stud_name = (input("Please enter the student's name: ")).capitalize()
    if stud_name in grades:
        print(f" Result found \n Student {stud_name} has {grades[stud_name]} points.")
        break
    if stud_name == "Stop program":
        print("Program stopped!")
        break
    else:
        print(f"Student's name {stud_name} is NOT in the grades list.\n Please enter another name or write: 'Stop program' to exit")


