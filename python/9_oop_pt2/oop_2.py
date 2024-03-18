class Zoo:
    def __init__(self):
        self._animals = []

    @property
    def animals(self):
        return self._animals

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self._animals.remove(animal)


class Animal:
    def __init__(self, animal_name, animal_id):
        self.animal_name = animal_name
        self.animal_id = animal_id

    def __str__(self):
        return f"Class {self.__class__.__name__} animal name {self.animal_name} animal id {self.animal_id} "


class Wolf(Animal):
    def play_sound(self):
        return "Roar"


class Lion(Animal):
    def play_sound(self):
        return "Arrr"


zoo = Zoo()
wolf = Wolf("Big bad Wolf", 1)
lion = Lion("King", 2)

zoo.add_animal(wolf)
zoo.add_animal(lion)

print(wolf)
print(lion)

for animal in zoo.animals:
    print(animal, "Sound:", animal.play_sound())
