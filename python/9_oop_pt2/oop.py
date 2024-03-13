class Zoo:  # encapsulation
    def __init__(self):
        self._animals = []

    def add_animal(self, animal):
        self._animals.append(animal)

    def remove_animal(self, animal):
        self._animals.remove(animal)

    def list_animals(self):
        for animal in self._animals:
            print(animal)


class Animal:  # abstraction
    def __init__(self, name, animal_id):
        self.name = name
        self.id = animal_id

    def play_sound(self):
        pass

    def __str__(self):
        return f"class {self.__class__.__name__} name {self.name} id {self.id}"


class Wolf(Animal):  # inheritance
    def play_sound(self):  # polymorphism
        return "Roar"


class Lion(Animal):  # inheritance
    def play_sound(self):  # polymorphism
        return "Roar"


class Bison(Animal):  # inheritance
    def play_sound(self):  # polymorphism
        return "Moo"


class Parrot(Animal):  # inheritance
    def play_sound(self):  # polymorphism
        return "Honk"


class Goose(Animal):  # inheritance
    def play_sound(self):  # polymorphism
        return "Honk"


zoo = Zoo()

zoo.add_animal(Wolf("Alfred", 1))
zoo.add_animal(Lion("Adam", 2))
zoo.add_animal(Bison("Antonio", 3))
zoo.add_animal(Parrot("Andrew", 4))
zoo.add_animal(Goose("Adrian", 5))

zoo.list_animals()
