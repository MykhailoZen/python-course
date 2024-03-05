class Zoo:

    def __init__(self):
        self._animals = []

    def add_animal(self, animal):
        self._animals.append(animal)

    def remove_animal(self, animal):
        self._animals.remove(animal)

    def print_animals(self):
        print(self._animals)


class Wolf:
    def __init__(self, name: str, unique_id: int) -> None:
        self.name = name
        self.unique_id = unique_id

    @staticmethod
    def play_sound() -> str:
        return 'Roar'

    def __str__(self):
        return f"class Wolf name {self.name} id {self.unique_id}"


class Lion:
    def __init__(self, name: str, unique_id: int) -> None:
        self.name = name
        self.unique_id = unique_id

    @staticmethod
    def play_sound() -> str:
        return 'Roar'

    def __str__(self):
        return f"class Lion name {self.name} id {self.unique_id}"


class Bison:
    def __init__(self, name: str, unique_id: int) -> None:
        self.name = name
        self.unique_id = unique_id

    @staticmethod
    def play_sound() -> str:
        return 'Moo'

    def __str__(self):
        return f"class Bison name {self.name} id {self.unique_id}"


class Parrot:
    def __init__(self, name: str, unique_id: int) -> None:
        self.name = name
        self.unique_id = unique_id

    @staticmethod
    def play_sound() -> str:
        return 'honk'

    def __str__(self):
        return f"class Parrot name {self.name} id {self.unique_id}"


class Goose:
    def __init__(self, name: str, unique_id: int) -> None:
        self.name = name
        self.unique_id = unique_id

    @staticmethod
    def play_sound() -> str:
        return 'honk'

    def __str__(self):
        return f"class Goose name {self.name} id {self.unique_id}"
