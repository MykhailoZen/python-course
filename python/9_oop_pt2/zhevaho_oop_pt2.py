class Animal:
    def __init__(self, animal_id, name):
        self.animal_id = animal_id
        self.name = name

    def play_sound(self):
        pass

    def __str__(self):
        return f"{self.name}, {self.animal_id}"


class Predator(Animal):
    def play_sound(self):
        return "Roar"

class Wolf(Predator):
    pass

class Lion(Predator):
    pass

class Herbivore(Animal):

    def play_sound(self):
        return "Moo"

class Bison(Herbivore):
    pass

class Bird(Animal):

    def play_sound(self):
        return "Honk"

class Parrot(Bird):
    pass

class Goose(Bird):
    pass

parrot1 = Parrot("01", "Bob")
print(parrot1)
print(parrot1.play_sound())