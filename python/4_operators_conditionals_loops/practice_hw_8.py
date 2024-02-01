# Dictionary of the all students.
def students_database():
    # Dictionary
    students_names_and_grades = {
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

    return students_names_and_grades


# Search students and grades in dictionary.
def search_students_and_grades(data=None, name_student=None):
    count = 0
    result = True
    for name_student_key in data:
        if name_student_key == name_student:
            result = list(data.items())[count]
            break
        else:
            result = False
        count += 1
    return result


# Stop or continue works with program.
def stop_or_continue_program(entered_value):
    # Continuing works with program.
    if entered_value == '':
        return main_program()
    # Stop program.
    elif entered_value == 'stop':
        print('Program is stopped...')
        return exit()
    else:
        print('Incorrect input. Please try again...')
        return False


def main_program():
    database = students_database()
    student_name = input('Please enter student name: ')
    search_in_database = search_students_and_grades(database, name_student=student_name)

    if student_name == '':
        stop_or_continue_program(student_name)
    elif search_in_database:
        search_student_name, search_student_grade = search_in_database
        print('Request was performed successful...')
        print(f'Result -> Student name: {search_student_name}, Grade: {search_student_grade}')

        while True:
            continue_or_stop = input('If you want continue tap ENTER or enter \'Stop\' to stop program: ').lower()
            if stop_or_continue_program(continue_or_stop):
                break
    elif not search_in_database:
        while True:
            continue_or_stop = input('Student was not found. Please entering another student name tap Enter or '
                                     'enter \'Stop\' to stop program: ').lower()
            if stop_or_continue_program(continue_or_stop):
                break


main_program()
