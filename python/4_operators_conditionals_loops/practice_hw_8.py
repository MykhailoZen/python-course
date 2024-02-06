# Function for search students in dictionary.
def search_student(students_names_and_grades: dict, input_student_name: str) -> tuple[str, bool]:
    result = True
    for name, grade in students_names_and_grades.items():
        if name == input_student_name.capitalize():
            result = f'Student {name} has grade {grade} point', True
            break
        else:
            result = (f'Student: "{input_student_name}" not found. Try another student name or '
                      f'enter \'Stop program\' to exit program.'), False

    return result


# Function for continue works with program.
def continue_program() -> bool:
    while True:
        continue_or_stop = input('Are you want to continue yes/no: ')
        if continue_or_stop.lower() == 'yes' or continue_or_stop.lower() == 'y':
            return True
        elif continue_or_stop.lower() == 'no' or continue_or_stop.lower() == 'n':
            return False


# Function for stop program.
def stop_program(input_string):
    if input_string.lower() == 'stop program':
        print('Program was stopped...')
        return exit()
    else:
        return False


# Main program
def main():
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

    while True:
        empty_string = ''

        input_string = input('Enter student\'s name: ')
        stop = stop_program(input_string)

        if input_string != empty_string or stop:
            search_result = search_student(students_names_and_grades, input_string)
            print(search_result[0])

            if search_result[1]:
                if continue_program():
                    continue
                else:
                    break
            else:
                continue
        else:
            continue


main()
