class Zoo:
    def __init__(self):
        self.__animals = []

    def add_animals(self, animal):
        self.__animals.append(animal)

    def del_animals(self, animal):
        self.__animals.remove(animal)

    @property
    def animals(self):
        return self.__animals

    def __str__(self):
        return f'All animals: {[animal.__class__.__name__ for animal in self.__animals]}'


class Animals:
    def __init__(self, name: str, id_animal: int):
        self.name = name
        self.id_animal = id_animal

    def __str__(self):
        return f"Class {self.__class__.__name__} name {self.name} id {self.id_animal} . "


class Wolf(Animals):
    def play_sound(self):
        return "Roar"


class Lion(Animals):
    def play_sound(self):
        return "Roar"


class Bioson(Animals):

    def play_sound(self):
        return "Moo"


class Parrtot(Animals):

    def play_sound(self):
        return "honk"


class Goose(Animals):
    def play_sound(self):
        return "honk"


# Example usage:

zoo = Zoo()

# usage of Add method
animals_list = [Wolf("Misha", 1), Lion("Grisha", 2),
                Bioson("Rocky", 3), Parrtot("Tobby", 4),
                Goose("Sally", 5)]

for animal in animals_list:
    zoo.add_animals(animal)

print(zoo)
print(animals_list[0].__str__())
# usage of Delete method
zoo.del_animals(animals_list[2])
print(zoo)
# usage of Play sound method
print(animals_list[1].play_sound())
print(animals_list[4].__str__(), "Sound is:", animals_list[4].play_sound())
