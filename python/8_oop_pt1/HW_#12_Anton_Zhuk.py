class Zoo:
    """Class Zoo has a protected list to named animals and add, extend, remove and get animals methods"""

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
    _class_name = 'Wolf'

    def __init__(self, id_animal: int, name_animal: str):
        self.name_animal = name_animal
        self.id_animal = id_animal

    def play_sound(self):
        sound_of_animal = 'Roar'

        return sound_of_animal

    def __str__(self):
        class_object_as_a_string = f'class {self._class_name} name {self.name_animal} id {self.id_animal}'

        return class_object_as_a_string


class Lion:
    _class_name = 'Lion'

    def __init__(self, id_animal: int, name_animal: str):
        self.name_animal = name_animal
        self.id_animal = id_animal

    def play_sound(self):
        sound_of_animal = 'Roar'

        return sound_of_animal

    def __str__(self):
        class_object_as_a_string = f'class {self._class_name} name {self.name_animal} id {self.id_animal}'

        return class_object_as_a_string


class Bison:
    _class_name = 'Bison'

    def __init__(self, id_animal: int, name_animal: str):
        self.name_animal = name_animal
        self.id_animal = id_animal

    def play_sound(self):
        sound_of_animal = 'Moo'

        return sound_of_animal

    def __str__(self):
        class_object_as_a_string = f'class {self._class_name} name {self.name_animal} id {self.id_animal}'

        return class_object_as_a_string


class Parrot:
    _class_name = 'Parrot'

    def __init__(self, id_animal: int, name_animal: str):
        self.name_animal = name_animal
        self.id_animal = id_animal

    def play_sound(self):
        sound_of_animal = 'honk'

        return sound_of_animal

    def __str__(self):
        class_object_as_a_string = f'class {self._class_name} name {self.name_animal} id {self.id_animal}'

        return class_object_as_a_string


class Goose:
    _class_name = 'Goose'

    def __init__(self, id_animal: int, name_animal: str):
        self.name_animal = name_animal
        self.id_animal = id_animal

    def play_sound(self):
        sound_of_animal = 'honk'

        return sound_of_animal

    def __str__(self):
        class_object_as_a_string = f'class {self._class_name} name {self.name_animal} id {self.id_animal}'

        return class_object_as_a_string


zoo = Zoo()
zoo.add_animals('Horse')
print(f'1. {zoo.get_animals()}')

zoo.extend_animals(['Dog', 'Cat', 'Mouse'])
print(f'2. {zoo.get_animals()}')

zoo.remove_animals('Horse')
print(f'3. {zoo.get_animals()}')

zoo.clear_animals_list()
print(f'4. {zoo.get_animals()}')

wolf_animal = Wolf(1, 'Amur')
lion_animal = Lion(2, 'Alia')
bison_animal = Bison(3, 'Tolik')
parrot_animal = Parrot(4, 'Oscar')
goose_animal = Goose(5, 'Nikita')
zoo.extend_animals([wolf_animal, lion_animal, bison_animal, parrot_animal, goose_animal])

for animal in zoo.get_animals():
    print(f"{animal} - {animal.play_sound()}")





