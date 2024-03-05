class Zoo:
    def __init__(self):
        self._animals = []

    def add_animal(self, animal):
        self._animals.append(animal)

    def remove_animal(self, animal):
        self._animals.remove(animal)

    def list_animals(self):
        for animal in self._animals:
            print(animal)

class Animal:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def play_sound(self):
        pass

    def __str__(self):
        return f'class {self.__class__.__name__} name {self.name} id {self.id}'

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

if __name__ == "__main__":
    zoo = Zoo()
    wolf = Wolf("Wolfie", 1)
    lion = Lion("Leo", 2)
    bison = Bison("Billy", 3)
    parrot = Parrot("Polly", 4)
    goose = Goose("Gus", 5)

    zoo.add_animal(wolf)
    zoo.add_animal(lion)
    zoo.add_animal(bison)
    zoo.add_animal(parrot)
    zoo.add_animal(goose)

    zoo.list_animals()

    print(wolf.play_sound())
    print(bison.play_sound())
    print(parrot.play_sound())