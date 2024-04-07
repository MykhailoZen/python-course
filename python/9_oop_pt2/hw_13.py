from abc import abstractmethod


class Zoo:
    def __init__(self):
        self._animals = []

    def add(self, animal):
        self._animals.append(animal)

    def remove(self, animal):
        self._animals.remove(animal)

    def __len__(self):
        return len(self._animals)


zoo = Zoo()


class Animal:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_info(self):
        return (
            f"Class {self.__class__.__name__} name: {self.name}, id: {self.id}"
        )

    @abstractmethod
    def play_sound(self):
        pass


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


wolf_1 = Wolf(1, "Alex")
wolf_2 = Wolf(2, "Sam")
lion_1 = Lion(1, "Felix")
lion_2 = Lion(2, "Lev")
bison_1 = Bison(1, "Teddy")
bison_2 = Bison(2, "Maya")
parrot_1 = Parrot(1, "Toni")
parrot_2 = Parrot(2, "Becca")
goose_1 = Goose(1, "Tront")
goose_2 = Goose(2, "Kira")


print(wolf_1.get_info())
zoo.add(wolf_2)
print(len(zoo))
print(lion_1.play_sound())
