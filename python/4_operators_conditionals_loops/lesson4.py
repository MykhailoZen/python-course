#Create a program that will help to find out the student's points.
#The program prompts you to enter the student's name and, if successful, returns the following message Student <name> has <value> points and complete its execution.
#If such a name is not in the dictionary, the program should inform about this and offer to enter another name.
#There should also be a way to end the program by typing Stop program.

students_grades = {
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
end_game = 'stop program'
name = input('Please enter student name \n')
while name!=end_game:

  for names in students_grades:
   if names.lower() == name.lower():
     print('Student %s has %s points and complete its execution \n' % (name, str(students_grades[names])))
     name = input('If you want to find data for another student, type a new name. \nIf you found your answers, type "Stop program" \n')
     name = name.lower()
     break
  else:
     name = input('Sorry, there is no such student.\nPlease enter another name. \nIf you found your answers, type "Stop program" \n')

print('Thank you for talking to the bot ;-)')




