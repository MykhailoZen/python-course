from abc import ABC, abstractmethod

class Zoo:
    def __init__(self):
        self._animals = []

    def add_animal(self, animal):
        self._animals.append(animal)

    def remove_animal(self, animal):
        if animal in self._animals:
            self._animals.remove(animal)
        else:
            print(f"{animal} not found in the zoo.")

class Animal(ABC):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    @abstractmethod
    def play_sound(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

class Wolf(Animal):
    def __init__(self, name, id):
        super().__init__(name, id)

    def play_sound(self):
        return "Roar"

    def __str__(self):
        return f"class Wolf name {self.name} id {self.id}"

class Lion(Animal):
    def __init__(self, name, id):
        super().__init__(name, id)

    def play_sound(self):
        return "Roar"

    def __str__(self):
        return f"class Lion name {self.name} id {self.id}"

class Bison(Animal):
    def __init__(self, name, id):
        super().__init__(name, id)

    def play_sound(self):
        return "Moo"

    def __str__(self):
        return f"class Bison name {self.name} id {self.id}"

class Parrot(Animal):
    def __init__(self, name, id):
        super().__init__(name, id)

    def play_sound(self):
        return "Honk"

    def __str__(self):
        return f"class Parrot name {self.name} id {self.id}"

class Goose(Animal):
    def __init__(self, name, id):
        super().__init__(name, id)

    def play_sound(self):
        return "Honk"

    def __str__(self):
        return f"class Goose name {self.name} id {self.id}"


wolf = Wolf("Grey Wolf", 1)
print(wolf.play_sound())  # Output: Roar
print(wolf)

lion = Lion("Orange Lion", 2)
print(lion.play_sound())  # Output: Roar
print(lion)

bison = Bison("Brown Bison", 3)
print(bison.play_sound())  # Output: Moo
print(bison)

parrot = Parrot("Green Parrot", 4)
print(parrot.play_sound())  # Output: Honk
print(parrot)

goose = Goose("White Goose", 5)
print(goose.play_sound())  # Output: Honk
print(goose)
