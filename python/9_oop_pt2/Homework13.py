class Zoo:
    def __init__(self):
        self.__animals = []

    def add_animal(self, animal):
        self.__animals.append(animal)

    def remove_animal(self, animal):
        self.__animals.remove(animal)

    def animals_list(self):
        return self.__animals


myZoo = Zoo()


class Animal:
    def __init__(self, name, id, sound):
        self.name = name
        self.id = id
        self.sound = sound

    def play_sound(self):
        return f"The {self.name} at the Zoo goes: {self.sound}"


class Wolf(Animal):
    def __init__(self, name, id):
        super().__init__(name, id, "Roar!")

    def __repr__(self):
        return f"class Wolf name {self.name} id {self.id}"


wolf_1 = Wolf("Kai", 1)
print(wolf_1.play_sound())
print(wolf_1.__repr__())


class Lion(Animal):
    def __init__(self, name, id):
        super().__init__(name, id, "Roar!")

    def __repr__(self):
        return f"class Lion name {self.name} id {self.id}"


lion_1 = Lion("Nala", 2)
print(lion_1.play_sound())
print(lion_1.__repr__())


class Bison(Animal):
    def __init__(self, name, id):
        super().__init__(name, id, "Moo!")

    def __repr__(self):
        return f"class Bison name {self.name} id {self.id}"


bison_1 = Bison("Buffalo", 3)
print(bison_1.play_sound())
print(bison_1.__repr__())


class Parrot(Animal):
    def __init__(self, name, id):
        super().__init__(name, id, "Moo!")

    def __repr__(self):
        return f"class Parrot name {self.name} id {self.id}"


parrot_1 = Parrot("Rio", 4)
print(parrot_1.play_sound())
print(parrot_1.__repr__())


class Goose(Animal):
    def __init__(self, name, id):
        super().__init__(name, id, "Honk!")

    def __repr__(self):
        return f"class Goose name {self.name} id {self.id}"


goose_1 = Goose("Gosling", 5)
print(goose_1.play_sound())
print(goose_1.__repr__())

myZoo.add_animal(wolf_1)
myZoo.add_animal(lion_1)
myZoo.add_animal(bison_1)
myZoo.add_animal(parrot_1)
myZoo.add_animal(goose_1)

#print(myZoo.animals_list())