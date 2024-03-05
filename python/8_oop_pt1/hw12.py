
# command + /

class Zoo:

    def __init__(self, __animals):
        self.animals = []

    def add(self, animals):
        self.animals.append(animals)

    def remove(self, animals):
        self.animals.remove(animals)


class Wolf:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def play_sound(self):
        print("Roar")

    def representation(self):
        print(f"class: {self}, name: {self.name}, id: {self.id}")


class Lion:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def play_sound(self):
        print("Roar")

    def representation(self):
        print(f"class: {self}, name: {self.name}, id: {self.id}")


class Bioson:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def play_sound(self):
        print("Moo")

    def representation(self):
        print(f"class: {self}, name: {self.name}, id: {self.id}")


class Parrtot:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def play_sound(self):
        print("Honk")

    def representation(self):
        print(f"class: {self}, name: {self.name}, id: {self.id}")


class Goose:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def play_sound(self):
        print("Honk")

    def representation(self):
        print(f"class: {self}, name: {self.name}, id: {self.id}")


