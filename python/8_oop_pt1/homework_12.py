class Animal:
    def __init__(self, name: str, id: int) -> None:
        self._name = name
        self._id = id

    def represent(self) -> str:
        return f"Class {self.__class__.__name__}, name {self._name}, id {self._id}"

    @property
    def animal_name(self):
        return self._name

    @property
    def animal_id(self):
        return self._id

    def play_sound(self) -> str:  # the method will be defined in each class itself
        pass


class Zoo(object):
    def __init__(self):
        self._animals = []

    def add_animal(self, *animal: Animal) -> None:
        for animal_to_add in animal:
            if isinstance(animal_to_add, Animal):
                self._animals.append(animal_to_add)
            else:
                print("Please add only previously correctly added animals (with name and id, using appropriate class)")

    @property
    def list_animals(self):
        if len(self._animals) == 0:
            return "The zoo is empty"
        else:
            return [animal_in_zoo.represent() for animal_in_zoo in self._animals]

    def remove_animal(self, *animals_to_remove: Animal) -> None:
        for animal_to_remove in animals_to_remove:
            if isinstance(animal_to_remove, Animal):
                if animal_to_remove in self._animals:
                    self._animals.remove(animal_to_remove)
                    print(f"{animal_to_remove.animal_name} removed from the zoo.")
                else:
                    print(f"{animal_to_remove.animal_name} not found in the zoo.")
            else:
                print("Please delete only correctly added animals (with name and id, using appropriate class)")


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
# our_zoo.add_animal(grey_wolf, young_goose)
# print(our_zoo.list_animals)
# our_zoo.remove_animal(young_goose)
# print(our_zoo.list_animals)
# grey_wolf2 = Wolf("White Fang2", 3)
# our_zoo.remove_animal(grey_wolf2)
# a = Parrot("Par", 4)
# print(a.animal_id, a.animal_name, a.play_sound(), a.represent())
# b = Bison("Bis", 5)
# print(b.animal_id, b.animal_name, b.play_sound(), b.represent())
# l = Lion("Simba", 6)
# print(l.animal_id, l.animal_name, l.play_sound(), l.represent())





