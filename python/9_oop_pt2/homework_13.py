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

class Animal:

    def __init__(self, animal_type, name, id):
        self.name = name
        self.type = animal_type
        self.id = id

    def play_sound(self, sound):
        print(f"This animal says: {sound}")

    def print_classinfo(self):
        print(f"Class {self.type} name {self.name} id {self.id}")


wolf = Animal('Wolf', 'Gray', 1)
wolf.print_classinfo()
wolf.play_sound("Roar")

lion = Animal('Lion', 'Orange', 2)
lion.print_classinfo()
lion.play_sound("Roar")

bioson = Animal('Bioson', 'Brown', 3)
bioson.print_classinfo()
bioson.play_sound("Moo")

parrot = Animal('Parrot', 'Red', 4)
parrot.print_classinfo()
parrot.play_sound("Honk")

goose = Animal('Goose', 'Grey', 5)
goose.print_classinfo()
goose.play_sound("Honk")