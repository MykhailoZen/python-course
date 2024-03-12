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


PT2:
Refactor your previous homework in an OOP way.
"""

class Zoo:
    def __init__(self):
        self._animals = []  # Protected list

    def add_animal(self, animal):

        if isinstance(animal, Animal):
            self._animals.append(animal)
        else:
            print("This is not an animal!")

    def remove_animal(self, animal):

        try:
            self._animals.remove(animal)
        except ValueError:
            print(f"Animal {animal.name} not found.")

    def list_animals(self):

        for animal in self._animals:
            print(animal)

class Animal:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def play_sound(self):

        raise NotImplementedError("This method needs to be overridden in subclasses.")

    def __str__(self):
        return f"class {self.__class__.__name__} name {self.name} id {self.id}"

# Defining subclasses for each animal
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

# Example usage
zoo = Zoo()
animals = [Wolf("Alpha", 1), Lion("Simba", 2), Bison("Benny", 3), Parrot("Polly", 4), Goose("Gus", 5)]

for animal in animals:
    zoo.add_animal(animal)

zoo.list_animals()  # Shows all animals in the zoo

print(animals[0].play_sound())  # Outputs the sound of the first animal (wolf)
