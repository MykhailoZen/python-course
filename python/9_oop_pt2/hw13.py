"""
Create a Python file with the next classes:

1) Create the class "Zoo" with a protected list named "animals"
2) Add methods for adding and removing elements from the list.
3) Create classes for Wolf, Lion, Bison, Parrot, and Goose

a) Each class should have fields: name(str), id(int) and constructor.
b) Each class should have the method "play_sound()" which returns the string with the sound of the animal (Use "Roar" for wolf and lion, "Moo" for bison, and "honk" for goose and parrot).
c) Create method which represents the current class object as a string e.g. output in print command should be like "class Lion name Alex id 2".
"""

class Zoo:
    def __init__(self):
        self._animals = []

    def add_animal(self, animal):
        self._animals.append(animal)

    def remove_animal(self, animal):
        self._animals.remove(animal)

    @property
    def animals(self):
        return self._animals


class Animal:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def play_sound(self):
        return "The sound animal produces"

    def __str__(self):
        return "class {} name {} id {}".format(self.__class__.__name__, self.name, self.id)


class Wolf(Animal):
    def play_sound(self):
        return "Roar"


class Lion(Animal):
    def play_sound(self):
        return "Roar"


class Bison(Animal):
    def play_sound(self):
        return "Moo"


class Parrot(Animal):
    def play_sound(self):
        return "Honk"


class Goose(Animal):
    def play_sound(self):
        return "Honk"


# Execution part:
zoo = Zoo()

wolf = Wolf("Akela", 1)
lion = Lion("Simba", 2)
bison = Bison("Buffalo", 3)
parrot = Parrot("Rio", 4)
goose = Goose("Roman", 5)

# Adding method usage

zoo.add_animal(wolf)
zoo.add_animal(lion)
zoo.add_animal(bison)
zoo.add_animal(parrot)
zoo.add_animal(goose)

print("Zoo animals:")
for animal in zoo.animals:
    print(animal)

print()

# Remove method usage
zoo.remove_animal(goose)

print("Zoo animals after goose removal")
for animal in zoo._animals:
    print(animal)

print()
print()


# Animal sounds

print(wolf.name + " says", wolf.play_sound())
print(lion.name + " says", lion.play_sound())
print(bison.name + " says", bison.play_sound())
print(parrot.name + " says", parrot.play_sound())
print(goose.name + " says", goose.play_sound())