class Zoo:
    def __init__(self):
        self._animals = []

    def add_element(self, animal):
        self._animals.append(animal)

    def remove_element(self, animal):
        if animal in self._animals:
            self._animals.remove(animal)
        else:
            print(f"{animal} is not in the Zoo!")

    def __str__(self):
        return f"Zoo: {', '.join(str(animal) for animal in self._animals)}"


class Animal:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def play_sound(self):
        pass

    def __repr__(self):
        return f"class {self.__class__.__name__} name {self.name} id {self.id}"


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


