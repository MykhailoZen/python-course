class Zoo:
    def __init__(self):
        self._animals = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self._animals.append(animal)
        else:
            raise TypeError("Can only add objects of type Animal")

    def remove_animal(self, animal):
        if animal in self._animals:
            self._animals.remove(animal)
        else:
            raise ValueError("No such animal in the zoo")

    def __str__(self):
        return f'Final list of animals: {[animal._name for animal in self._animals]}'



class Animal:
    sound = "Roar"

    def __init__(self, name, animal_id):
        self._name = name
        self._id = animal_id

    @classmethod
    def play_sound(cls):
        return cls.sound

    def __str__(self):
        return f'class {type(self).__name__}, name: {self._name}, id: {self._id}'


class Wolf(Animal):
    pass


class Lion(Animal):
    pass


class Bison(Animal):
    sound = "Moo"


class Parrot(Animal):
    sound = "Honk"


class Goose(Parrot):
    pass


# Testing the code
zoo = Zoo()
wolf = Wolf("Wolfie", 1)
lion = Lion("Leo", 2)
bison = Bison("Bisony", 3)
parrot = Parrot("Polly", 4)
goose = Goose("Gus", 5)

zoo.add_animal(wolf)
zoo.add_animal(lion)
zoo.add_animal(bison)
zoo.add_animal(parrot)
zoo.add_animal(goose)

print(zoo)

zoo.remove_animal(bison)
print(zoo)

print(wolf.play_sound())
print(wolf)

print(lion.play_sound())
print(lion)

print(parrot.play_sound())
print(parrot)

print(goose.play_sound())
print(goose)