"""
Create a Python file with the next classes:
1) Create the class "Zoo" with a protected list named "animals"
2) Add methods for adding and removing elements from the list.
3) Create classes for Wolf, Lion, Bison, Parrot, and Goose
a) Each class should have fields: name(str), id(int) and constructor.
b) Each class should have the method "play_sound()" which returns the string with the sound of the animal
Use "Roar" for wolf and lion, "Moo" for bison, and "honk" for goose and parrot
c) Create method which represents the current class object as a string e.g. output in print command
should be like "class Lion name Alex id 2".
"""

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        return animal

    def remove_animal(self, animal):
        self.animals.remove(animal)

my_zoo = Zoo()
animal_1 = my_zoo.add_animal(["Wolf", 1])
animal_2 = my_zoo.add_animal(["Lion", 2])
animal_3 = my_zoo.add_animal(["Bison", 3])
animal_4 = my_zoo.add_animal(["Parrot", 4])
animal_5 = my_zoo.add_animal(["Goose", 5])
animal_6 = my_zoo.add_animal(["Snake", 6])
# animal_6 added specifically to showcase remove method
print(my_zoo.animals)
my_zoo.remove_animal(animal_6)
print(my_zoo.animals)


class Wolf:
    def __init__(self, name, id):
            self.name = name
            self.id = id
            self.sound = "Roar!"

    def play_sound(self):
        return f"The {self.name} at the Zoo goes: {self.sound}"

    def __repr__(self):
        return f"class Wolf name {self.name} id {self.id}"

wolf_1 = Wolf("Kai", 1)
print(wolf_1.play_sound())
print(wolf_1)

class Lion:
    def __init__(self, name, id):
            self.name = name
            self.id = id
            self.sound = "Roar!"

    def play_sound(self):
        return f"The {self.name} at the Zoo goes: {self.sound}"

    def __repr__(self):
        return f"class Lion name {self.name} id {self.id}"

lion_1 = Lion("Nala", 2)
print(lion_1.play_sound())
print(lion_1)

class Bison:
    def __init__(self, name, id):
            self.name = name
            self.id = id
            self.sound = "Moo!"

    def play_sound(self):
        return f"The {self.name} at the Zoo goes: {self.sound}"

    def __repr__(self):
        return f"class Bison name {self.name} id {self.id}"

bison_1 = Bison("Buffalo", 3)
print(bison_1.play_sound())
print(bison_1)


class Parrot:
    def __init__(self, name, id):
            self.name = name
            self.id = id
            self.sound = "Honk!"

    def play_sound(self):
        return f"The {self.name} at the Zoo goes: {self.sound}"

    def __repr__(self):
        return f"class Parrot name {self.name} id {self.id}"

parrot_1 = Parrot("Rio", 4)
print(parrot_1.play_sound())
print(parrot_1)

class Goose:
    def __init__(self, name, id):
            self.name = name
            self.id = id
            self.sound = "Honk!"

    def play_sound(self):
        return f"The {self.name} at the Zoo goes: {self.sound}"

    def __repr__(self):
        return f"class Goose name {self.name} id {self.id}"

goose_1 = Goose("Gosling", 5)
print(goose_1.play_sound())
print(goose_1)

