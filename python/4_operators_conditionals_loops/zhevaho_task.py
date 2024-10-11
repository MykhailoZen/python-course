# Create a program that will help to find out the student's points.
# The program prompts you to enter the student's name and, if successful,
# returns the following message Student <name> has <value> points and complete its execution.
# If such a name is not in the dictionary, the program should inform about this and offer to enter another name.
# There should also be a way to end the program by typing Stop program.


students = {
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

game_running = True
while game_running:
    answer = input("Please, enter the student's name: ")
    if answer == 'Stop':
        print("Game over.")
        game_running = False
    elif answer in students:
        print(f"Student {answer} has {students[answer]} points.")
    else:
        print("The name is not in a dictionary. Choose another name: ")

