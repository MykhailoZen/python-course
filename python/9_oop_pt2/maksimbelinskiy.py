class Animal:
    def __init__(self, name, animal_id):
        self.name = name
        self.animal_id = animal_id

    def play_sound(self):
        pass

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


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)


# Example usage:
if __name__ == "__main__":
    zoo = Zoo()
    wolf = Wolf("Gray Wolf", 1)
    lion = Lion("Simba", 2)
    bison = Bison("Benny", 3)
    parrot = Parrot("Polly", 4)
    goose = Goose("Gary", 5)

    zoo.add_animal(wolf)
    zoo.add_animal(lion)
    zoo.add_animal(bison)
    zoo.add_animal(parrot)
    zoo.add_animal(goose)

    print("Animals in the zoo:")
    for animal in zoo.animals:
        print(animal)
        print("Sound:", animal.play_sound())