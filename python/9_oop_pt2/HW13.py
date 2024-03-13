class Zoo:
    def __init__(self):
        self._animals = []

    def add_animal(self, animal):
        self._animals.append(animal)

    def remove_animal(self, animal):
        if animal in self._animals:
            self._animals.remove(animal)

    def display_animals(self):
        print("Animals in the zoo:")
        for animal in self._animals:
            print(animal)
            print("Sound:", animal.make_sound())


class Animal:
    def __init__(self, name, animal_id):
        self.name = name
        self.id = animal_id

    def make_sound(self):
        pass

    def __str__(self):
        return f"class {self.__class__.__name__} name {self.name} id {self.id}"


class Wolf(Animal):
    def make_sound(self):
        return "Roar"


class Lion(Animal):
    def make_sound(self):
        return "Roar"


class Bison(Animal):
    def make_sound(self):
        return "Moo"


class Parrot(Animal):
    def make_sound(self):
        return "Honk"


class Goose(Animal):
    def make_sound(self):
        return "Honk"


if __name__ == "__main__":
    zoo = Zoo()

    wolf = Wolf("Alpha", 1)
    lion = Lion("Simba", 2)
    bison = Bison("Bob", 3)
    parrot = Parrot("Polly", 4)
    goose = Goose("Gus", 5)

    zoo.add_animal(wolf)
    zoo.add_animal(lion)
    zoo.add_animal(bison)
    zoo.add_animal(parrot)
    zoo.add_animal(goose)

    zoo.display_animals()
