class Animal:
    def __init__(self, name: str, id: int):
        self._name = name
        self._id = id

    def __str__(self) -> str:
        return f"Class {self.__class__.__name__}, name {self._name}, id {self._id}"

    @property
    def animal_name(self):
        return self._name

    @property
    def animal_id(self):
        return self._id

    def play_sound(self) -> str:  # the method will be defined in each class itself
        pass


class Zoo:
    def __init__(self):
        self._animals = []

    def add_animals(self, *animals: Animal):
        for animal_to_add in animals:
            if isinstance(animal_to_add, Animal):
                self._animals.append(animal_to_add)
            else:
                print("Please add only previously correctly added animals (with name and id, using appropriate class)")

    @property
    def list_animals(self):
        if len(self._animals) == 0:
            return "The zoo is empty"
        else:
            return [str(animal_in_zoo) for animal_in_zoo in self._animals]

    def remove_animal(self, animal_to_remove: Animal):
        if isinstance(animal_to_remove, Animal):
            if animal_to_remove in self._animals:
                self._animals.remove(animal_to_remove)
                print(f"{animal_to_remove.animal_name} removed from the zoo.")
            else:
                print(f"{animal_to_remove.animal_name} not found in the zoo.")
        else:
            print("Please delete only correctly added animal (with name and id, using appropriate class)")


class Wolf(Animal):
    def play_sound(self) -> str:
        return "Roar!"


class Lion(Animal):
    def play_sound(self) -> str:
        return "Roar!"


class Bison(Animal):
    def play_sound(self) -> str:
        return "Moo!"


class Parrot(Animal):
    def play_sound(self) -> str:
        return "Honk!"


class Goose(Animal):
    def play_sound(self) -> str:
        return "Honk!"


# Uncomment below for testing
# grey_wolf = Wolf("White Fang", 1)
# young_goose = Goose("Woody", 2)
# print(grey_wolf.play_sound())
# print(young_goose.play_sound())
# our_zoo = Zoo()
# print(our_zoo.list_animals)
# our_zoo.add_animals(grey_wolf, young_goose)
# print(our_zoo.list_animals)
# our_zoo.remove_animal(young_goose)
# print(our_zoo.list_animals)
# grey_wolf2 = Wolf("White Fang2", 3)
# our_zoo.remove_animal(grey_wolf2)
# parrot1 = Parrot("Par", 4)
# print(parrot1.animal_id, parrot1.animal_name, parrot1.play_sound(), parrot1)
# bison1 = Bison("Bis", 5)
# print(bison1.animal_id, bison1.animal_name, bison1.play_sound(), bison1)
# lion1 = Lion("Simba", 6)
# print(lion1.animal_id, lion1.animal_name, lion1.play_sound(), lion1)





