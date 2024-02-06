dict = {'Alan': 68, 'Roslyn': 48, 'Bertha': 50, 'Sally': 95, 'Rachel': 11, 'John': 95, 'Derek': 82, 'Kevin': 34, 'Michael': 31, 'Richard': 12}
lokeys = dict.keys()
uinp = ""
while True:
    uinp = input('Enter the student\'s name: ')
    if uinp == "Stop program":
        break
    if uinp in lokeys:
        print('Student ' + uinp +' has ' + str(dict[uinp]) +' points')
    else:
        print('No such student')
        continue