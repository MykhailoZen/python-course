class Zoo:
    def __init__(self):
        self._animals = []

    def add_animal(self, animal):
        self._animals.append(animal)

    def remove_animal(self, animal):
        self._animals.remove(animal)

    def list_animals(self):
        return [str(animal) for animal in self._animals]

class AnimalSonds:
    def make_sound(self):
        pass

class RoarSound(AnimalSonds):
    def make_sound(self):
        return "Roar"

class MooSound(AnimalSonds):
    def make_sound(self):
        return "Moo"

class HonkSound(AnimalSonds):
    def make_sound(self):
        return "Honk"

class Animal:
    def __init__(self, name, id, sound_behavior):
        self.name = name
        self.id = id
        self.sound_behavior = sound_behavior

    def play_sound(self):
        return self.sound_behavior.make_sound()

    def __str__(self):
        return f'{self.__class__.__name__}(name={self.name}, id={self.id})'

# Specific animals
class Wolf(Animal):
    def __init__(self, name, id):
        super().__init__(name, id, RoarSound())

class Lion(Animal):
    def __init__(self, name, id):
        super().__init__(name, id, RoarSound())

class Bison(Animal):
    def __init__(self, name, id):
        super().__init__(name, id, MooSound())

class Parrot(Animal):
    def __init__(self, name, id):
        super().__init__(name, id, HonkSound())

class Goose(Animal):
    def __init__(self, name, id):
        super().__init__(name, id, HonkSound())

if __name__ == "__main__":
    zoo = Zoo()
    zoo.add_animal(Wolf("Marty", 1))
    zoo.add_animal(Lion("Alex", 2))
    zoo.add_animal(Bison("Melman", 3))
    zoo.add_animal(Parrot("Gloria", 4))
    zoo.add_animal(Goose("Skipper", 5))

    print(zoo.list_animals())

    for animal in zoo._animals:
        print(animal.play_sound())