# Refactor homework 12 in an OOP way.

class Animal:
    def __init__(self, name, _id):
        self.name = name
        self.id = _id

    def play_sound(self):
        pass

    def __str__(self):
        return f"class {self.__class__.__name__} name {self.name} id {self.id}"


class Wolf(Animal):
    def play_sound(self):
        return "Roar"


class Lion(Animal):
    def play_sound(self):
        return "Roar"


class Bison(Animal):
    def play_sound(self):
        return "Moo"


class Parrot(Animal):
    def play_sound(self):
        return "Honk"


class Goose(Animal):
    def play_sound(self):
        return "Honk"


class Zoo:
    def __init__(self):
        self._animals = []

    def add_animal(self, animal):
        self._animals.append(animal)

    def remove_animal(self, animal):
        self._animals.remove(animal)


# Example:
if __name__ == "__main__":
    zoo = Zoo()
    wolf = Wolf("Grey Bully", 1)
    lion = Lion("King Leo", 2)
    bison = Bison("Fat Tony", 3)
    parrot = Parrot("Funny Sally", 4)
    goose = Goose("Drunkard Gary", 5)

    zoo.add_animal(wolf)
    zoo.add_animal(lion)
    zoo.add_animal(bison)
    zoo.add_animal(parrot)
    zoo.add_animal(goose)

    for animal in zoo._animals:
        print(animal, f"says: {animal.play_sound()}!")