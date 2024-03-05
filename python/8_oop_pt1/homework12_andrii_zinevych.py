class Zoo:
    def __init__(self, name, id):
        self._animals = []
        self.name = name
        self.id = id

    def add_element(self, animal):
        self._animals.append(animal)

    def remove_element(self, animal):
        if animal in self._animals:
            self._animals.remove(animal)
        else:
            print(f"{animal} is not in the Zoo!")

    def __str__(self):
        return f"class {self.__class__.__name__} name {self.name} id {self.id}"


class Wolf:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def play_sound(self):
        return "Roar"

    def __str__(self):
        return f"class {self.__class__.__name__} name {self.name} id {self.id}"


class Lion:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def play_sound(self):
        return "Roar"

    def __str__(self):
        return f"class {self.__class__.__name__} name {self.name} id {self.id}"


class Bison:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def play_sound(self):
        return "Moo"

    def __str__(self):
        return f"class {self.__class__.__name__} name {self.name} id {self.id}"


class Parrot:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def play_sound(self):
        return "Honk"

    def __str__(self):
        return f"class {self.__class__.__name__} name {self.name} id {self.id}"


class Goose:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def play_sound(self):
        return "Honk"

    def __str__(self):
        return f"class {self.__class__.__name__} name {self.name} id {self.id}"
