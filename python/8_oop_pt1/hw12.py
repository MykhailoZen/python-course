# 1) Create the class "Zoo" with a protected list named "animals"
# 2) Add methods for adding and removing elements from the list.
class Zoo:

    def __init__(self):
        self.__animals = []

    def add_animal(self, animal):
        self.__animals.append(animal)

    def remove_animal(self, animal):
        if animal in self.__animals:
            self.__animals.remove(animal)
        else:
            print(f"{animal} is not in the Zoo list")
            pass

    def show(self):
        """To check the animals list"""
        print(self.__animals)

#testing
zoo = Zoo()
zoo.add_animal("lama")
zoo.show()
zoo.remove_animal("lama")
zoo.show()
zoo.remove_animal("tiger")
zoo.show()
# 3) Create classes for Wolf, Lion, Bioson, Parrtot, and Goose
# a) Each class should have fields: name(str), id(int) and constructor.
# b) Each class should have the method "play_sound()" which returns the string with the sound of the animal
# (Use "Roar" for wolf and lion, "Moo" for bison, and "honk" for goose and parrot).
# c) Create method which represents the current class object as a string
# e.g. output in print command should be like "class Lion name Alex id 2".

class Wolf:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def play_sound(self):
        return "Roar"

    def __str__(self):
        return f"Class 'Wolf' name '{self.name}' id '{self.id}'"

wolf = Wolf("aaa", 1)
print(wolf.__str__())

class Lion:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def play_sound(self):
        return "Roar"

    def __str__(self):
        return f"Class 'Lion' name '{self.name}' id '{self.id}'"

lion = Lion("bbb", 2)
print(lion.__str__())

class Bioson:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def play_sound(self):
        return "Moo"

    def __str__(self):
        return f"Class 'Bioson' name '{self.name}' id '{self.id}'"

bison = Bioson("ccc", 3)
print(bison.__str__())

class Parrtot:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def play_sound(self):
        return "honk"

    def __str__(self):
        return f"Class 'Parrtot' name '{self.name}' id '{self.id}'"

parrot = Parrtot("ddd", 4)
print(parrot.__str__())

class Goose:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def play_sound(self):
        return "honk"

    def __str__(self):
        return f"Class 'Goose' name '{self.name}' id '{self.id}'"

goose = Goose("eee", 5)
print(goose.__str__())

