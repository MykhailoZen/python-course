from grades import grades

class Finder:
    def __init__(self, name):
        self.name=name
    def selector(self,marks):
        return marks[self.name]

def grader():
    student=input("Enter name of the student:")
    if student.lower() == "stop program":
        print("Leaving")
        exit()
    else:
        try:
            selecting = Finder(student)
            print("Student", student,"has",selecting.selector(grades), "points.")
        except:
            print("Something gone wrong, you have to select student again")

while True:
    grader()
