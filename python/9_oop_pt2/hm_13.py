class Animal:
    def __init__(self, name: str, animal_id: int):
        self.name = name
        self.animal_id = animal_id

    def play_sound(self):
        raise NotImplementedError("Subclasses must implement play_sound method")

    def __str__(self):
        return f'class {self.__class__.__name__}, name {self.name}, with id {self.animal_id}, {self.play_sound()}'


class Wolf(Animal):
    def play_sound(self):
        return f'says - Roar'


class Lion(Animal):

    def play_sound(self):
        return f'says - Roar'


class Bison(Animal):

    def play_sound(self):
        return f'says - Moo'


class Parrot(Animal):

    def play_sound(self):
        return f'says - honk'


class Goose(Animal):

    def play_sound(self):
        return f'says - honk'


class Zoo:

    def __init__(self):
        self.__animals = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.__animals.append(animal)
        else:
            raise ValueError("Only instances of Animal class can be added to the zoo")

    def remove_animal(self, animal):
        try:
            self.__animals.remove(animal)
        except ValueError as Val:
            print(f'This {animal} not in the list of animals. Error: {Val}')
        except Exception as e:
            return 'An error occurred: ' + str(e)

    def get_list_of_animals(self):
        animal_info_list = [str(animal) for animal in self.__animals]
        return f'List of animals in the zoo: {animal_info_list}'


if __name__ == "__main__":
    zoo = Zoo()
    wolf = Wolf('Ivan', 5478)
    lion = Lion('Saran', 4656)
    lion2 = Lion('Star', 1111)
    bison = Bison('Babe', 45654)
    bison2 = Bison('Small', 23232)
    parrot = Parrot('Сrow', 45654)
    goose = Goose('Baе', 45654)

    # verification adding classes Wolf, Lion, Bison, Parrot, Goose
    zoo.add_animal(wolf)
    zoo.add_animal(lion)
    zoo.add_animal(lion2)
    zoo.add_animal(bison)
    zoo.add_animal(parrot)
    zoo.add_animal(goose)

    print("All list")
    print(zoo.get_list_of_animals())
    # verification removing
    zoo.remove_animal(lion)
    print(f"All list after removing Saran")
    print(zoo.get_list_of_animals())

    # verification removing not adding animal
    zoo.remove_animal(bison2)
