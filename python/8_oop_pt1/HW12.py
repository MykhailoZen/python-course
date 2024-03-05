class Zoo:
    def __init__(self):
        self._animals = []  # Initialize the list to store animals

    def add_animal(self, animal):
        """Add an animal to the zoo."""
        self._animals.append(animal)

    def remove_animal(self, animal):
        """Remove an animal from the zoo."""
        if animal in self._animals:
            self._animals.remove(animal)

# Base class for all animals
class Animal:
    def __init__(self, name, animal_id):
        self.name = name
        self.id = animal_id

    def play_sound(self):
        """Method to make the animal sound."""
        pass  # This method will be overridden in the subclasses

    def __str__(self):
        """String representation of the animal."""
        return f"class {self.__class__.__name__} name {self.name} id {self.id}"

# Specific animal classes
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

# Example Usage:
if __name__ == "__main__":
    zoo = Zoo()
    
    # Creating animal instances and adding them to the zoo
    wolf = Wolf("Alpha", 1)
    lion = Lion("Simba", 2)
    bison = Bison("Bob", 3)
    parrot = Parrot("Polly", 4)
    goose = Goose("Gus", 5)
    
    zoo.add_animal(wolf)
    zoo.add_animal(lion)
    zoo.add_animal(bison)
    zoo.add_animal(parrot)
    zoo.add_animal(goose)

    print("Animals in the zoo:")
    for animal in zoo._animals:
        print(animal)
        print("Sound:", animal.play_sound())
