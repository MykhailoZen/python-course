# Student grades data
student_grades = {'Alan': 68, 'Roslyn': 48, 'Bertha': 50, 'Sally': 95, 'Rachel': 11, 'John': 95, 'Derek': 82, 'Kevin': 34, 'Michael': 31, 'Richard': 12}

def find_student_points():
    while True:
        # Prompt user to enter student's name or 'Stop program' to end
        student_name = input("Enter student's name (or 'Stop program' to end): ")

        if student_name.lower() == 'stop program':
            print("Program stopped.")
            break

        # Using faster algorithm - direct access to dictionary
        if student_name in student_grades:
            # If the name is found, print the student's points
            points = student_grades[student_name]
            print(f"Student {student_name} has {points} points.")
        else:
            # If the name is not found, inform the user and prompt for another name
            print(f"Student {student_name} not found. Please enter another name.")

if __name__ == "__main__":
    find_student_points()
