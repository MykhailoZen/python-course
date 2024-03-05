# Create a Python file with the next classes: 1) Create the class "Zoo" with a protected list named "animals" 2) Add
# methods for adding and removing elements from the list. 3) Create classes for Wolf, Lion, Bison, Parrot,
# and Goose a) Each class should have fields: name(str), id(int) and constructor. b) Each class should have the
# method "play_sound()" which returns the string with the sound of the animal (Use "Roar" for wolf and lion,
# "Moo" for bison, and "honk" for goose and parrot). c) Create method which represents the current class object as a
# string e.g. output in print command should be like "class Lion name Alex id 2".
class Zoo:
    def __init__(self):
        self._animals = []

    def add_animal(self, new_animal):
        self._animals.append(new_animal)

    def remove_animal(self, animal_to_remove):
        self._animals.remove(animal_to_remove)


class Animal:
    def __init__(self, name, animal_id):
        self.animal_name = name
        self.animal_id = animal_id

    def make_sound(self):
        return f"{self.__class__.__name__} says {self.animal_name}"

    def __str__(self):
        return f"class {self.__class__.__name__} name {self.animal_name} id {self.animal_id}"


class Wolf(Animal):
    def make_sound(self):
        return "Roar"


class Lion(Animal):
    def make_sound(self):
        return "Roar"


class Bison(Animal):
    def make_sound(self):
        return "Moo"


class Parrot(Animal):
    def make_sound(self):
        return "Honk"


class Goose(Animal):
    def make_sound(self):
        return "Honk"


# Example
if __name__ == "__main__":
    zoo = Zoo()
    wolf = Wolf("Wolf1", 1)
    lion = Lion("Lion2", 2)
    bison = Bison("Bison3", 3)
    parrot = Parrot("Parrot4", 4)
    goose = Goose("Goose5", 5)

    zoo.add_animal(wolf)
    zoo.add_animal(lion)
    zoo.add_animal(bison)
    zoo.add_animal(parrot)
    zoo.add_animal(goose)

    for animal in zoo._animals:
        print(animal, "sound:", animal.make_sound())

    # Testing
    print("test:")
    zoo.remove_animal(lion)
    if lion not in zoo._animals:
        print("Lion2 removed successfully")
    else:
        print("Failed to remove Lion2")

    zoo.add_animal(lion)
    if lion in zoo._animals:
        print("Lion2 added successfully")
    else:
        print("Failed to add Lion2")
