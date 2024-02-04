# Student grades (data for homework)
grades = {'Alan': 68, 'Roslyn': 48, 'Bertha': 50, 'Sally': 95, 'Rachel': 11, 'John': 95, 'Derek': 82,
          'Kevin': 34, 'Michael': 31, 'Richard': 12}

# Checking in loop, for student's name or "Stop" phrase
while True:
    # Prompt user for student's name or to stop the program
    name = input("Enter student's name (or type 'Stop program' to end): ")
    # Check if user wants to stop program
    if name == "Stop program":
        print("Program stopped")
        break  # End the program
    # Check if the entered name is in the dictionary
    if name in grades:
        # Name found, return grades
        points = grades[name]
        print(f"Student {name} has {points} points")
        break  # Found the student, so end the program
    else:
        # Name not found, ask to reenter name, or exit the program
        print("Student not found. Please try again or type 'Stop program' to end.")
