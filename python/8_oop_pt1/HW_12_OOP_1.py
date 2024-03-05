"""Create a Python file with the next classes:

1) Create the class "Zoo" with a protected list named "animals"

2) Add methods for adding and removing elements from the list.

3) Create classes for Wolf, Lion, Bioson, Parrtot, and Goose

a) Each class should have fields: name(str), id(int) and constructor.

b) Each class should have the method "play_sound()" which returns the string with the sound of the animal (Use "Roar"
for wolf and lion, "Moo" for bison, and "honk" for goose and parrot).

c) Create method which represents the current class object as a string e.g. output in print command should be like
"class Lion name Alex id 2"."""


# 1) Create the class "Zoo" with a protected list named "animals"
class Zoo:
    def __init__(self):
        self.animals = []

    # 2) Add methods for adding and removing elements from the list.
    def add_animals(self, animal):
        self.animals.append(animal)

    def del_animals(self, animal):
        self.animals.remove(animal)


# Example usage:
zoo = Zoo()
zoo.add_animals("Lion")
zoo.add_animals("Cat")
zoo.add_animals("Dog")
print(zoo.animals)
zoo.del_animals("Dog")
print(zoo.animals)


# 3) Create classes for Wolf, Lion, Bioson, Parrtot, and Goose
class Wolf:
    def __init__(self, name: str, id_animal: int):
        self.name = name
        self.id_animal = id_animal

    def play_sound(self):
        return "Roar"

    def __str__(self):
        return f"class Wolf name {self.name} id {self.id_animal}"


class Lion:
    def __init__(self, name: str, id_animal: int):
        self.name = name
        self.id_animal = id_animal

    def play_sound(self):
        return "Roar"

    def __str__(self):
        return f"class Lion name {self.name} id {self.id_animal}"


class Bioson:
    def __init__(self, name: str, id_animal: int):
        self.name = name
        self.id_animal = id_animal

    def play_sound(self):
        return "Moo"

    def __str__(self):
        return f"class Bioson name {self.name} id {self.id_animal}"


class Parrtot:
    def __init__(self, name: str, id_animal: int):
        self.name = name
        self.id_animal = id_animal

    def play_sound(self):
        return "honk"

    def __str__(self):
        return f"class Parrtot name {self.name} id {self.id_animal}"


class Goose:
    def __init__(self, name: str, id_animal: int):
        self.name = name
        self.id_animal = id_animal

    def play_sound(self):
        return "honk"

    def __str__(self):
        return f"class Goose name {self.name} id {self.id_animal}"


# Example usage:
animal_1 = Wolf("Misha", 1)
animal_2 = Lion("Grisha", 2)
animal_3 = Bioson("Rocky", 3)
animal_4 = Parrtot("Tobby", 4)
animal_5 = Goose("Sally", 5)
print(animal_1, "Sound is:", animal_1.play_sound())
print(animal_2, "Sound is:", animal_2.play_sound())
print(animal_3, "Sound is:", animal_3.play_sound())
print(animal_4, "Sound is:", animal_4.play_sound())
print(animal_5, "Sound is:", animal_5.play_sound())
