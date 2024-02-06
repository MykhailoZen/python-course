# Student grades data
student_grades = {'Alan': 68, 'Roslyn': 48, 'Bertha': 50, 'Sally': 95, 'Rachel': 11, 'John': 95, 'Derek': 82,
                  'Kevin': 34, 'Michael': 31, 'Richard': 12}


def find_student_points():
    while True:
        # Prompt user to enter student's name or "Stop program" to end
        user_input = input("Enter student's name (type 'Stop program' to end): ")

        if user_input.lower() == 'Stop program':
            print("Program stopped.")
            break

        # Check if the entered name exists in the dictionary
        if user_input in student_grades:
            # If the name exists, print the points and end the program
            points = student_grades[user_input]
            print(f"Student {user_input} has {points} points. Program complete.")
            break
        else:
            # If the name doesn't exist, inform the user and prompt for another name
            print(f"Student {user_input} not found. Please enter another name.")


# Run the program
find_student_points()
