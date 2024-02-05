"""
Create a program that will help to find out the student's points.
The program prompts you to enter the student's name and, if successful, returns the following message Student <name> has
<value> points and complete its execution.
If such a name is not in the dictionary, the program should inform about this and offer to enter another name.
There should also be a way to end the program by typing Stop program.
"""
student_grades = {'Alan': 68, 'Roslyn': 48, 'Bertha': 50, 'Sally': 95, 'Rachel': 11, 'John': 95, 'Derek': 82,
                  'Kevin': 34, 'Michael': 31, 'Richard': 12}

while True:
    user_input = input("Please, enter the name of student to get mark: \n >>> ").capitalize()
    if user_input == "Stop program":
        print("Exit...")
        break
    elif user_input in student_grades:
        print("Student {} has {} points".format(user_input, student_grades.get(user_input)))
        break
    else:
        print("There is no such name, please enter another: \n")
