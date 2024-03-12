class Zoo:
    def __init__(self):
        self._animals = []

    def add_animal(self, animal):
        self._animals.append(animal)

    def remove_animal(self, animal):
        self._animals.remove(animal)

    def print_animals(self):
        print(self._animals)


class Animal:
    def __init__(self, name: str, unique_id: int) -> None:
        self.name = name
        self.unique_id = unique_id

    def play_sound(self) -> str:
        return 'sound'

    def __str__(self):
        class_name = self.__class__.__name__
        return f'class {class_name} name {self.name} id {self.unique_id}'


class Wolf(Animal):
    def play_sound(self) -> str:
        return 'Roar'


class Lion(Animal):
    def play_sound(self) -> str:
        return 'Roar'


class Bison(Animal):
    def play_sound(self) -> str:
        return 'Moo'


class Parrot(Animal):
    def play_sound(self) -> str:
        return 'honk'


class Goose(Animal):
    def play_sound(self) -> str:
        return 'honk'