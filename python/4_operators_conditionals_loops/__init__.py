"""
Create a program that will help to find out the student's points.
The program prompts you to enter the student's name and, if successful, returns the following message Student <name> has <value> points and complete its execution.
If such a name is not in the dictionary, the program should inform about this and offer to enter another name.
There should also be a way to end the program by typing Stop program
"""

student_data = {
    'Alan': 68, 'Roslyn': 48, 'Bertha': 50, 'Sally': 95,
    'Rachel': 11, 'John': 95, 'Derek': 82, 'Kevin': 34,
    'Michael': 31, 'Richard': 12
}


def get_student_score():
    while True:
        student_name = input("Enter the name of a student from a List or 'Stop program' to end the program: ': ")

        if student_name == 'Stop program':
            print("Program interrupted.")
            break

        if student_name in student_data:
            points = student_data[student_name]
            print(f"Student {student_name} has {points} points.")
        else:
            print(f"Student {student_name} not in List. Please enter the correct name.")


get_student_score()
