
class Zoo:
    def __init__(self):
        self._animals = []

    def add_animal(self, animal):
        self._animals.append(animal)

    def remove_animal(self, animal):
        self._animals.remove(animal)


class Animal:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return f"class {self.__class__.__name__} name {self.name} id {self.id} sounds like {self.play_sound()}"

    def play_sound(self):
        return self.sound


class Wolf(Animal):
    sound = "Woof"


class Lion(Animal):
    sound = 'Roar'


class Bison(Animal):
    sound = 'Moo'


class Parrot(Animal):
    sound = 'Honk'


class Goose(Animal):
    sound = 'Honk'


zoo = Zoo()
# an instance of zoo created

wolf = Wolf('Igor', 1)
lion = Lion('Ostap', 2)
bison = Bison('Oleg', 3)
parrot = Parrot('Natalia', 4)
goose = Goose('Fedir', 5)

zoo.add_animal(wolf)
zoo.add_animal(lion)
zoo.add_animal(bison)
zoo.add_animal(parrot)
zoo.add_animal(goose)

print(goose)
print(parrot)
print(wolf)
print(lion)
print(bison)

#print(wolf.play_sound())