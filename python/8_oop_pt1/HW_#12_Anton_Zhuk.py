class Zoo:
    """Class Zoo has a protected list to named animals and add, extend, remove, get and clear animals methods"""

    def __init__(self):
        self._animals = []

    # Method add_animals to provide an opportunity add animals to list.
    def add_animals(self, animal_name):
        self._animals.append(animal_name)

    # Method extend_animals to provide an opportunity extend list of animals.
    def extend_animals(self, animal_name):
        self._animals.extend(animal_name)

    # Method remove_animals to provide an opportunity remove animals from list.
    def remove_animals(self, animal_name):
        self._animals.remove(animal_name)

    # Method get_animals to provide and opportunity get list of animals.
    def get_animals(self):
        return self._animals

    # Method clear_animals_list to provide and opportunity clear list of animals.
    def clear_animals_list(self):
        self._animals.clear()


class Wolf:
    def __init__(self, id_animal: int, name_animal: str) -> None:
        self.name_animal = name_animal
        self.id_animal = id_animal

    def play_sound(self) -> str:
        return 'Roar'

    def __str__(self) -> str:
        return f'class {self.__class__.__name__} name {self.name_animal} id {self.id_animal}'


class Lion:
    def __init__(self, id_animal: int, name_animal: str) -> None:
        self.name_animal = name_animal
        self.id_animal = id_animal

    def play_sound(self) -> str:
        return 'Roar'

    def __str__(self) -> str:
        return f'class {self.__class__.__name__} name {self.name_animal} id {self.id_animal}'


class Bison:
    def __init__(self, id_animal: int, name_animal: str) -> None:
        self.name_animal = name_animal
        self.id_animal = id_animal

    def play_sound(self) -> str:
        return 'Moo'

    def __str__(self) -> str:
        return f'class {self.__class__.__name__} name {self.name_animal} id {self.id_animal}'


class Parrot:
    def __init__(self, id_animal: int, name_animal: str) -> None:
        self.name_animal = name_animal
        self.id_animal = id_animal

    def play_sound(self) -> str:
        return 'honk'

    def __str__(self) -> str:
        return f'class {self.__class__.__name__} name {self.name_animal} id {self.id_animal}'


class Goose:
    def __init__(self, id_animal: int, name_animal: str) -> None:
        self.name_animal = name_animal
        self.id_animal = id_animal

    def play_sound(self) -> str:
        return 'honk'

    def __str__(self) -> str:
        return f'class {self.__class__.__name__} name {self.name_animal} id {self.id_animal}'


zoo = Zoo()

print(f'a. {zoo.get_animals()}')

zoo.add_animals('Horse')
print(f'b. {zoo.get_animals()}')

zoo.extend_animals(['Dog', 'Cat', 'Mouse'])
print(f'c. {zoo.get_animals()}')

zoo.remove_animals('Horse')
print(f'd. {zoo.get_animals()}')

zoo.clear_animals_list()
print(f'e. {zoo.get_animals()}')

print('-' * 35)

wolf_animal = Wolf(1, 'Amur')
lion_animal = Lion(2, 'Alia')
bison_animal = Bison(3, 'Tolik')
parrot_animal = Parrot(4, 'Oscar')
goose_animal = Goose(5, 'Nikita')
zoo.extend_animals([wolf_animal, lion_animal, bison_animal, parrot_animal, goose_animal])

counter = 0
for animal in zoo.get_animals():
    counter += 1
    print(f'{counter}. {animal} - {animal.play_sound()}')
