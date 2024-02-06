# Function for search students in dictionary.
def search_student(students_names_and_grades: dict, input_student_name: str) -> str:
    result = True
    for name, grade in students_names_and_grades.items():
        if name == input_student_name:
            result = f'Student {name} has grade {grade} point'
            break
        else:
            result = (f'Student: "{input_student_name}" not found. Try another student name or '
                      f'enter \'Stop program\' to exit program.')

    return result


# Function for stop program.
def stop_program(input_string):
    if input_string.lower() == 'stop program':
        print('Program was stopped...')
        return exit()


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
        input_string = input('Enter student\'s name: ')

        if stop_program(input_string):
            break
        else:
            search_result = search_student(students_names_and_grades, input_string)
            print(search_result)


main()
