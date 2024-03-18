
class Zoo:

    def __init__(self):
        self.animals = []

    def add_animal(self, animals):
        self.animals.append(animals)
        print("Animal added to the zoo")

    def remove_animal(self, animals):
        self.animals.remove(animals)
        print("Animal removed from the zoo")


class Animal:

    def __init__(self, name, _id):
        self.name = name
        self.id = _id
        print("New animal created")

    def representation(self):
        print(f"class: {self.__class__}, name: {self.name}, id: {self.id}")


class Wolf(Animal):

    def play_sound(self):
        print("Roar")


class Lion(Animal):

    def play_sound(self):
        print("Roar")


class Bison(Animal):

    def play_sound(self):
        print("Moo")


class Parrot(Animal):

    def play_sound(self):
        print("Honk")


class Goose(Animal):

    def play_sound(self):
        print("Honk")


zoo = Zoo()
wolf = Wolf("Wolf", 1)
lion = Lion("Lion", 2)
bison = Bison("Bison", 3)
parrot = Parrot("Parrot", 4)
goose = Goose("Goose", 5)


wolf.play_sound()
lion.play_sound()
bison.play_sound()
parrot.play_sound()
goose.play_sound()


wolf.representation()
lion.representation()
bison.representation()
parrot.representation()
goose.representation()


zoo.add_animal(wolf)
zoo.add_animal(lion)
zoo.add_animal(bison)
zoo.add_animal(parrot)
zoo.add_animal(goose)

print(zoo.animals)

zoo.remove_animal(wolf)
zoo.remove_animal(lion)
zoo.remove_animal(bison)
zoo.remove_animal(parrot)
zoo.remove_animal(goose)

print(zoo.animals)
