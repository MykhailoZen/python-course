class Zoo:
    def __init__(self):
        self._animals = []

    def add_animal(self, animal):
        self._animals.append(animal)

    def remove_animal(self, animal):
        self._animals.remove(animal)

class animal:
    def __int__(self, name, animal_id, sound):
        self.name = name
        self.id = animal_id
        self.sound = sound

    def play_sound(self):
        return self.sound
    def __str__(self):
        return f"class {type(self).__name__} name {self.name} id {self.id}"

class Wolf(animal):
    def __init__(self, name, animal_id):
        self.name = name
        self.id = animal_id
        self.sound = "roar"
class Lion(animal):
    def __init__(self, name, animal_id):
        self.name = name
        self.id = animal_id
        self.sound = "roar"


class Bison(animal):
    def __init__(self, name, animal_id):
        self.name = name
        self.id = animal_id
        self.sound = "moo"

class Parrot(animal):
    def __init__(self, name, animal_id):
        self.name = name
        self.id = animal_id
        self.sound = "honk"

class Goose(animal):
    def __init__(self, name, animal_id):
        self.name = name
        self.id = animal_id
        self.sound = "honk"


# Usage
if __name__ == "__main__":
    zoo = Zoo()

    wolf = Wolf("Stark", 11)
    lion = Lion("Alex", 3)
    bison = Bison("Chak", 16)
    parrot = Parrot("Allan", 4198)
    goose = Goose("Rob", 1)

    zoo.add_animal(wolf)
    zoo.add_animal(lion)
    zoo.add_animal(bison)
    zoo.add_animal(parrot)
    zoo.add_animal(goose)

    for animal in zoo._animals:
        print(animal, "says", animal.play_sound())