class Zoo:
    def __init__(self):
        self._animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self._animals.remove(animal)
        print("Romoved: " + str(animal))
    @property
    def animals(self):
        return self._animals


class Animal:
    def __init__(self, animal_name, animal_id):
        self._animals = []
        self.animal_name = animal_name
        self.animal_id = animal_id

    def play_sound(self):
        pass

    def __str__(self):
        return f"Class {self.__class__.__name__} animal name {self.animal_name} animal id {self.animal_id} "


class Wolf(Animal):
    def play_sound(self):
        return "Roar"


class Lion(Animal):
    def play_sound(self):
        return "Roar"


class Beason(Animal):
    def play_sound(self):
        return "Moo"


class Parrot(Animal):
    def play_sound(self):
        return "Honk"


class Goose(Animal):
    def play_sound(self):
        return "Honk"


zoo = Zoo()
wolf = Wolf("Big bad Wolf", 1)
lion = Lion("King", 2)
beason = Beason("Ben", 3)
parrot = Goose("Sparrow", 4)
goose = Goose("Pink", 5)

zoo.add_animal(wolf)
zoo.add_animal(lion)
zoo.add_animal(beason)
zoo.add_animal(parrot)
zoo.add_animal(goose)

for animal in zoo.animals:
    print(animal, "Sound:", animal.play_sound())

zoo.remove_animal(wolf)
zoo.remove_animal(beason)


