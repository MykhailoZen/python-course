students_grades = {'Alan': 68, 'Roslyn': 48, 'Bertha': 50, 'Sally': 95, 'Rachel': 11, 'John': 95, 'Derek': 82, 'Kevin': 34, 'Michael': 31, 'Richard': 12}


def ask_for_one_more_name():
    answer = input("Do you want to get grade of another student, type \'yes\' for it  or \'no\' to quit ").lower()
    if answer == 'no':
        print('Thanks for using program. Farewell.')
        return False
    elif answer == 'yes':
        return True
    else:
        print("Sorry, don't understand your answer. Please type 'yes' or 'no' ")
        return ask_for_one_more_name()


while True:
    student_name = input("Enter student name and get grade or type 'stop program' to quit program: ").strip(' ').capitalize()
    if student_name == 'Stop program':
        print("Program stopped. Farewell")
        break # to stop running

    elif student_name in students_grades:
        print(f" {student_name} has a {students_grades[student_name]}")
        if not ask_for_one_more_name(): # to work with case, when typed no and to exit code
            break

    else:
        print(f'Try another name, please, or type \"stop program\" to quit program:')






