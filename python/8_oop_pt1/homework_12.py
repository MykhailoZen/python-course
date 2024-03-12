class Zoo:
    def __init__(self):
        self.__animals = []

    def add_animal(self, animal):
        self.__animals.append(animal)

    def remove_animal(self, animal):
        self.__animals.remove(animal)

    def print_animals(self):
        print(self.__animals)

"""We can add animals to the protected list, remove them and check list content"""
my_zoo = Zoo()
my_zoo.add_animal('Dog')
my_zoo.add_animal('Cat')
my_zoo.print_animals()
my_zoo.remove_animal('Dog')
my_zoo.print_animals()

class Wolf:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def play_sound(self):
        print('Roar')

    def print_classinfo(self):
        print(f"Class Wolf name {self.name} id {self.id}")

my_wolf = Wolf('Gray', 1)
my_wolf.play_sound()
my_wolf.print_classinfo()

class Lion:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def play_sound(self):
        print('Roar')

    def print_classinfo(self):
        print(f"Class Lion name {self.name} id {self.id}")

my_lion = Lion('Orange', 2)
my_lion.play_sound()
my_lion.print_classinfo()

class Bioson:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def play_sound(self):
        print('Moo')

    def print_classinfo(self):
        print(f"Class Bioson name {self.name} id {self.id}")

my_bioson = Bioson('Brown', 3)
my_bioson.play_sound()
my_bioson.print_classinfo()

class Parrot:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def play_sound(self):
        print('Honk')

    def print_classinfo(self):
        print(f"Class Parrot name {self.name} id {self.id}")

my_parrot = Parrot('Red', 4)
my_parrot.play_sound()
my_parrot.print_classinfo()

class Goose:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def play_sound(self):
        print('Honk')

    def print_classinfo(self):
        print(f"Class Goose name {self.name} id {self.id}")

my_goose = Goose('White', 5)
my_goose.play_sound()
my_goose.print_classinfo()