from past.builtins import raw_input


points = {
    "Alan": 68,
    "Roslyn": 48,
    "Bertha": 50,
    "Sally": 95,
    "Rachel": 11,
    "John": 95,
    "Derek": 82,
    "Kevin": 34,
    "Michael": 31,
    "Richard": 12,
}

user_input = raw_input("Hi! Please write a student's name: ")

while user_input not in points.keys():
    if user_input == "Stop":
        print("Program stopped")
        break
    else:
        user_input = raw_input(
            "There is no such student. Please write a student's name: "
        )
else:
    print(
        "Student " + user_input + " has " + str(points[user_input]) + " points"
    )


# Create a program that will help to find out the student's points.
# The program prompts you to enter the student's name and, if successful, returns the following message Student <name> has <value> points and complete its execution.
# If such a name is not in the dictionary, the program should inform about this and offer to enter another name.
# There should also be a way to end the program by typing Stop program.
# Student grades (data for homework)
# {'Alan': 68, 'Roslyn': 48, 'Bertha': 50, 'Sally': 95, 'Rachel': 11, 'John': 95, 'Derek': 82, 'Kevin': 34, 'Michael': 31, 'Richard': 12}
