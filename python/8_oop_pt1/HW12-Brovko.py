# 1) Create the class "Zoo" with a protected list named "animals"
# 2) Add methods for adding and removing elements from the list.
class Zoo:
    def __init__(self):
        self._animals = []

    def add_animal(self, animal):
        self._animals.append(animal)

    def remove_animal(self, animal):
        self._animals.remove(animal)


# 3) Create classes for Wolf, Lion, Bison, Parrot, and Goose

# a) Each class should have fields: name(str), id(int) and constructor.

# b) Each class should have the method "play_sound()" which returns the string with the sound of the animal (Use "Roar"
# for wolf and lion, "Moo" for bison, and "honk" for goose and parrot).

#c) Create method which represents the current class object as a string e.g. output in print command should be like
# "class Lion name Alex id 2".

class Wolf:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def play_sound(self):
        return 'Woof'

    def __str__(self):
        return f"class {self.__class__.__name__} name {self.name} id {self.id} sounds like {self.play_sound()}"


class Lion:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def play_sound(self):
        return 'Roar'

    def __str__(self):
        return f"class {self.__class__.__name__} name {self.name} id {self.id} sounds like {self.play_sound()}"


class Bison:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def play_sound(self):
        return 'Moo'

    def __str__(self):
        return f"class {self.__class__.__name__} name {self.name} id {self.id} sounds like {self.play_sound()}"


class Parrot:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def play_sound(self):
        return 'Honk'

    def __str__(self):
        return f"class {self.__class__.__name__} name {self.name} id {self.id} sounds like {self.play_sound()}"

class Goose:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def play_sound(self):
        return 'Honk'

    def __str__(self):
        return f"class {self.__class__.__name__} name {self.name} id {self.id} sounds like {self.play_sound()}"


zoo = Zoo()
# an instance of zoo created

wolf = Wolf('Igor', 1)
lion = Lion('Ostap', 2)
bison = Bison('Oleg', 3)
parrot = Parrot('Natalia', 4)
goose = Goose('Fedir', 5)

zoo.add_animal(wolf)
zoo.add_animal(lion)
zoo.add_animal(bison)
zoo.add_animal(parrot)
zoo.add_animal(goose)

print(goose.__str__())
print(parrot.__str__())
print(wolf.__str__())
print(lion.__str__())
print(bison.__str__())