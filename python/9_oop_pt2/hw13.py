
class Zoo:

    animals = []

    def __init__(self, name, _id):
        self.name = name
        self.id = id
        print("New animal created")

    def add(self, animals):
        self.animals.append(animals)
        print("Animal added to the list")

    def remove(self, animals):
        self.animals.remove(animals)
        print("Animal removed from the list")

    def representation(self):
        print(f"class: {self.__class__}, name: {self.name}, id: {self.id}")


class Wolf(Zoo):

    def play_sound(self):
        print("Roar")


class Lion(Zoo):

    def play_sound(self):
        print("Roar")


class Bison(Zoo):

    def play_sound(self):
        print("Moo")


class Parrot(Zoo):

    def play_sound(self):
        print("Honk")


class Goose(Zoo):

    def play_sound(self):
        print("Honk")


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


wolf.add(wolf)
lion.add(lion)
bison.add(bison)
parrot.add(parrot)
goose.add(goose)

print(Zoo.animals)

wolf.remove(wolf)
lion.remove(lion)
bison.remove(bison)
parrot.remove(parrot)
goose.remove(goose)

print(Zoo.animals)
