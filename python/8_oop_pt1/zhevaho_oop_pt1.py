# Create a Python file with the next classes:
from tkinter.font import names

# 1) Create the class "Zoo" with a protected list named "animals"
class Zoo:
    def __init__(self):
        self._animals = []

    # 2) Add methods for adding and removing elements from the list.

    def get_animals(self):
        return [str(animal) for animal in self._animals]

    def add_animal(self, animal):
        self._animals.append(animal)

    def remove_animal(self, animal):
        self._animals.remove(animal)



# 3) Create classes for Wolf, Lion, Bison, Parrot, and Goose
# a) Each class should have fields: name(str), id(int) and constructor.
# b) Each class should have the method "play_sound()" which returns the string with the sound of the animal
# (Use "Roar" for wolf and lion, "Moo" for bison, and "honk" for goose and parrot).
# c) Create method which represents the current class object as a string e.g.
# output in print command should be like "class Lion name Alex id 2".

class Wolf:

    def __init__(self, name, animal_id):
        self.name = name
        self.id = animal_id

    def play_sound(self):
        return "Roar"

    def __str__(self):
        return f"Wolf {self.name} id {self.id}"

wolf = Wolf("Alex", 2)
print(wolf)
print(wolf.play_sound())
zoo = Zoo()
zoo.add_animal(wolf)
print(zoo.get_animals())


class Lion:
    def __init__(self, name, animal_id):
        self.name = name
        self.id = animal_id

    def play_sound(self):
        return "Roar"

    def __str__(self):
        return f"Lion {self.name} id {self.id}"

class Bison:
    def __init__(self, name, animal_id):
        self.name = name
        self.id = animal_id

    def play_sound(self):
        return "Moo"

    def __str__(self):
        return f"Bison {self.name} id {self.id}"

class Parrot:
    def __init__(self, name, animal_id):
        self.name = name
        self.id = animal_id

    def play_sound(self):
        return "Honk"

    def __str__(self):
        return f"Parrot {self.name} id {self.id}"

class Goose:
    def __init__(self, name, animal_id):
        self.name = name
        self.id = animal_id

    def play_sound(self):
        return "Honk"

    def __str__(self):
        return f"Goose {self.name} id {self.id}"


