class Zoo:
    def __init__(self):
        self._animals = []

    def add_animal(self, animal):
        self._animals.append(animal)

    def remove_animal(self, animal):
        if animal in self._animals:
            self._animals.remove(animal)
        else:
            print(f"{animal} is not in the Zoo!")

class Wolf:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def play_sound(self):
        return "Roar"

    def __str__(self):
        return f"class {self.__class__.__name__} name {self.name} id {self.id}"


class Lion:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def play_sound(self):
        return "Roar"

    def __str__(self):
        return f"class {self.__class__.__name__} name {self.name} id {self.id}"


class Bison:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def play_sound(self):
        return "Moo"

    def __str__(self):
        return f"class {self.__class__.__name__} name {self.name} id {self.id}"


class Parrot:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def play_sound(self):
        return "Honk"

    def __str__(self):
        return f"class {self.__class__.__name__} name {self.name} id {self.id}"


class Goose:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def play_sound(self):
        return "Honk"

    def __str__(self):
        return f"class {self.__class__.__name__} name {self.name} id {self.id}"

oliwa = Zoo()
mucka=Goose("Mucka",1)
print(mucka.play_sound())
print(mucka)
oliwa.add_animal(mucka)
print(oliwa._animals)
oliwa.remove_animal(mucka)
print(oliwa._animals)