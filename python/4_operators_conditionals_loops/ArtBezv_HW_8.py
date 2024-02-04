scoreboard = {'Alan': 68, 'Roslyn': 48, 'Bertha': 50, 'Sally': 95, 'Rachel': 11, 'John': 95, 'Derek': 82, 'Kevin': 34, 'Michael': 31, 'Richard': 12}
print("To stop the program please type: Stop program")

while True:
    name = input('Please enter the name: ')

    if name.lower() == "stop program":
        break

    if name in scoreboard:
        print('Student {} has {} points'.format(name, scoreboard[name]))
        break
    else:
        print('Student not found. Try again')