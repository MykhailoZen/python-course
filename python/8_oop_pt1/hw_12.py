# Create a Python file with the next classes:
# 1) Create the class "Zoo" with a protected list named "animals"
# 2) Add methods for adding and removing elements from the list.
# 3) Create classes for Wolf, Lion, Bison, Parrot, and Goose
# a) Each class should have fields: name(str), id(int) and constructor.
# b) Each class should have the method "play_sound()"
# which returns the string with the sound of the animal (Use "Roar" for wolf and lion,
# "Moo" for bison, and "honk" for goose and parrot).
# c) Create method which represents the current class object as a string
# e.g. output in print command should be like "class Lion name Alex id 2".


class Zoo:
    def __init__(self):
        self._animals = []

    def add(self, animal):
        self._animals.append(animal)

    def remove(self, animal):
        self._animals.remove(animal)


zoo = Zoo()


class Wolf:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def play_sound(self):
        return "Roar"

    def get_info(self):
        return f"Class Wolf name: {self.name}, id: {self.id}"


wolf_1 = Wolf(1, "Alex")
wolf_2 = Wolf(2, "Sam")


class Lion:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def play_sound(self):
        return "Roar"

    def get_info(self):
        return f"Class Lion name: {self.name}, id: {self.id}"


lion_1 = Lion(1, "Felix")
lion_2 = Lion(2, "Lev")


class Bison:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def play_sound(self):
        return "Moo"

    def get_info(self):
        return f"Class Bison name: {self.name}, id: {self.id}"


bison_1 = Bison(1, "Teddy")
bison_2 = Bison(2, "Maya")


class Parrot:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def play_sound(self):
        return "Honk"

    def get_info(self):
        return f"Class Parrot name: {self.name}, id: {self.id}"


parrot_1 = Parrot(1, "Toni")
parrot_2 = Parrot(2, "Becca")


class Goose:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def play_sound(self):
        return "Honk"

    def get_info(self):
        return f"Class Goose name: {self.name}, id: {self.id}"


goose_1 = Goose(1, "Tront")
goose_2 = Goose(2, "Kira")

# print(lion_1.get_info())
# print(lion_1.play_sound())
#
#
# zoo.add(lion_1)
# zoo.add(parrot_1)
# zoo.add(goose_1)
# zoo.add(wolf_1)
#
# for animal in zoo._animals:
#     print(animal.get_info(), " : ", animal.play_sound())
#
# print(zoo._animals)
