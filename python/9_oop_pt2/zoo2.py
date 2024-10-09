

class Zoo:
    def __init__(self):
        self._animals = []

    def add_animal(self, animal):
        self._animals.append(animal)

    def remove_animal(self, animal):
        if animal in self._animals:
            self._animals.remove(animal)
        else:
            print(f"{animal} is not in the Zoo!")

class Animal:
    def __init__(self, name, animal_id):
        self.name = name
        self.animal_id = animal_id

    def play_sound(self):
        return "Imaginary sound"

    def __str__(self):
        return f"class {self.__class__.__name__} name {self.name} id {self.animal_id}"



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

oliwa = Zoo()
mucka=Goose("Mucka",1)
print(mucka.play_sound())
print(mucka)
oliwa.add_animal(mucka)
print(oliwa._animals)
oliwa.remove_animal(mucka)
print(oliwa._animals)