from abc import ABC, abstractmethod

class Zoo:
    def __init__(self):
        self.__animals = []

    def add_animal(self, animal):
        self.__animals.append(animal)

    def remove_animal(self, animal):
        if animal in self.__animals:
            self.__animals.remove(animal)
        else:
            print(f"{animal} is not in the Zoo list")
            pass

class Animal:
    def __init__(self, name, id,):
        self.name = name
        self.id = id

    def play_sound(self):
        return "Roar"

    def __str__(self):
        return f"Class {self.__class__} name {self.name} id {self.id}"


class Wolf(Animal):
    pass

class Lion(Animal):
    pass

class Bison(Animal):
    def play_sound(self):
        return "Moo"

class Parrot(Animal):
    def play_sound(self):
        return "Honk"

class Goose(Animal):
    pass

