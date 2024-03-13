class Zoo:
    def __init__(self):
        self.animals = ['Vorona', 'Bilka']

    def add_element(self, animal):
        self.animals.append(animal)

    def remove_element(self, animal):
        self.animals.remove(animal)


class Animal:
    def __init__(self, name: str, id: str):
        self.name = name
        self.id = id

    def play_sound(self):
        pass

    def string(self):
        return f"class {self.__class__.__name__} name {self.name} id {self.id}"


class Wolf(Animal):

    def play_sound(self):
        return "Roar"


class Lion(Animal):

    def play_sound(self):
        return "Roar"


class Bioson(Animal):

    def play_sound(self):
        return "Moo"


class Parrot(Animal):

    def play_sound(self):
        return "honk"


class Goose(Animal):

    def play_sound(self):
        return "honk"


Zoo = Zoo()
Zoo.add_element('Leleka')
wolf = Wolf('Black wolf', 2)
lion = Lion('Yellow lion', 3)
bison = Bioson('Grey bison', 4)
parrot = Parrot('Red parrot', 5)
goose = Goose('White goose', 6)
Zoo.add_element(wolf.name)
Zoo.add_element(lion.name)
Zoo.add_element(bison.name)
print(Zoo.animals)
Zoo.remove_element(lion.name)
print(Zoo.animals)
Zoo.add_element(parrot.name)
Zoo.add_element(goose.name)
print(Zoo.animals)
print(Wolf.string(wolf) + " sound: " + wolf.play_sound())
print(Lion.string(lion) + " sound: " + lion.play_sound())
print(Bioson.string(bison) + " sound: " + bison.play_sound())
print(Parrot.string(parrot) + " sound: " + parrot.play_sound())
print(Goose.string(goose) + " sound: " + goose.play_sound())
