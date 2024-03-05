"""
Create a Python file with the next classes:
1) Create the class "Zoo" with a protected list named "animals"
2) Add methods for adding and removing elements from the list.
3) Create classes for Wolf, Lion, Bison, Parrot, and Goose
a) Each class should have fields: name(str), id(int) and constructor.
b) Each class should have the method "play_sound()" which returns the string with the sound of the animal
(Use "Roar" for wolf and lion, "Moo" for bison, and "honk" for goose and parrot).
c) Create method which represents the current class object as a string
e.g. output in print command should be like "class Lion name Alex id 2".
"""

class Zoo:
    def __init__(self):
        self._animals = []  # protected list

    def add_animal(self, animal):
        self._animals.append(animal)

    def remove_animal(self, animal):
        self._animals.remove(animal)

class Animal:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def play_sound(self):
        pass

    def __str__(self):
        return f"class {self.__class__.__name__} name {self.name} id {self.id}"

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

#EXAMPLE

zoo = Zoo()
wolf = Wolf("Alpha", 1)
lion = Lion("Simba", 2)
bison = Bison("Benny", 3)
parrot = Parrot("Polly", 4)
goose = Goose("Gus", 5)

zoo.add_animal(wolf)
zoo.add_animal(lion)
zoo.add_animal(bison)
zoo.add_animal(parrot)
zoo.add_animal(goose)

# play_sound method and __str__ method
print(wolf.play_sound())
print(bison.play_sound())
print(parrot)
