# Create a Python file with the next classes:
# 1) Create the class "Zoo" with a protected list named "animals"
# 2) Add methods for adding and removing elements from the list.
# 3) Create classes for Wolf, Lion, Bison, Parrot, and Goose
# a) Each class should have fields: name(str), id(int) and constructor.
# b) Each class should have the method "play_sound()" which returns the string with the sound of the animal (Use "Roar"
# for wolf and lion, "Moo" for bison, and "honk" for goose and parrot).
# c) Create method which represents the current class object as a string e.g. output in print command should be like
# "class Lion name Alex id 2".


class Zoo:
    def __init__(self):
        self._animals = []

    def add_animal(self, animal):
        self._animals.append(animal)

    def remove_animal(self, animal):
        self._animals.remove(animal)

    def get_animals(self):  # Public method to access the private list
        return self._animals


class Wolf:
    def __init__(self, name, animal_id):
        self.name = name
        self.id = animal_id

    def play_sound(self):
        return "Roar"

    def __str__(self):
        return f"class Wolf name {self.name} id {self.id}"


class Lion:
    def __init__(self, name, animal_id):
        self.name = name
        self.id = animal_id

    def play_sound(self):
        return "Roar"

    def __str__(self):
        return f"class Lion name {self.name} id {self.id}"


class Bison:
    def __init__(self, name, animal_id):
        self.name = name
        self.id = animal_id

    def play_sound(self):
        return "Moo"

    def __str__(self):
        return f"class Bison name {self.name} id {self.id}"


class Parrot:
    def __init__(self, name, animal_id):
        self.name = name
        self.id = animal_id

    def play_sound(self):
        return "Honk"

    def __str__(self):
        return f"class Parrot name {self.name} id {self.id}"


class Goose:
    def __init__(self, name, animal_id):
        self.name = name
        self.id = animal_id

    def play_sound(self):
        return "Honk"

    def __str__(self):
        return f"class Goose name {self.name} id {self.id}"


# Playing with our animals and putting them into zoo
# Creating Zoo instance
zoo = Zoo()
# Creating Lion instance
lion = Lion("Leo", 1)
zoo.add_animal(lion)
# Creating Bison instance
bison = Bison("Brown", 2)
zoo.add_animal(bison)
# Creating Goose instance
goose = Goose("Gooch", 3)
zoo.add_animal(goose)
# Let's see and hear them
for animal in zoo.get_animals():
    print(f"{animal} - {animal.play_sound()}")
