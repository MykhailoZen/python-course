"""
Create a program that will help to find out the student's points.
The program prompts you to enter the student's name and, if successful, returns the following message
Student <name> has <value> points and complete its execution.
If such a name is not in the dictionary, the program should inform about this and offer to enter another name.
There should also be a way to end the program by typing Stop program.

Student grades (data for homework)
{'Alan': 68, 'Roslyn': 48, 'Bertha': 50, 'Sally': 95, 'Rachel': 11, 'John': 95, 'Derek': 82, 'Kevin': 34, 'Michael': 31, 'Richard': 12}

"""
# Student grades
student_grades = {
    'Alan': 68,
    'Roslyn': 48,
    'Bertha': 50,
    'Sally': 95,
    'Rachel': 11,
    'John': 95,
    'Derek': 82,
    'Kevin': 34,
    'Michael': 31,
    'Richard': 12
}
stop = "stop program"
def get_student_grades():
    while True:
        input_name = input("Please enter the student's name for getting student's points: ")
        # If such a name is in the dictionary
        if input_name in student_grades:
            grade = student_grades[input_name]
            print(f'Student {input_name} has {grade} points.')
            # and complete its execution
            break
        #  to end the program by typing Stop program.
        elif input_name.lower() == stop:
            print(f'The program was stopped')
            break
        # If such a name is not in the dictionary and not Stop program
        else:
            print(f'We do not have {input_name} in student grades list. Please input another name! ')

get_student_grades()
