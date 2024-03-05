class Zoo:
    def __init__(self):
        self._animals = []

    def add_animal(self, animal):
        self._animals.append(animal)

    def remove_animal(self, animal):
        self._animals.remove(animal)


class Animal:
    def __init__(self, name, animal_id):
        self.name = name
        self.id = animal_id

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


def list_zoo_animals(zoo_animals):
    for animal in zoo_animals:
        print(animal)


zoo = Zoo()

zoo.add_animal(Wolf("Alfred", 1))
zoo.add_animal(Lion("Adam", 2))
zoo.add_animal(Bison("Antonio", 3))
zoo.add_animal(Parrot("Andrew", 4))
zoo.add_animal(Goose("Adrian", 5))

list_zoo_animals(zoo._animals)
