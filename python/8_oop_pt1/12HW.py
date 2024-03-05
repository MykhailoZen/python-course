class Zoo:
    def __init__(self):
        self.animals = ['Vorona', 'Bilka']
    def add_element(self, animal):
        self.animals.append(animal)
    def remove_element(self, animal):
        self.animals.remove(animal)
class Wolf:
    def __init__(self, name:str, id:int):
        self.name = name
        self.id = id
    def play_sound(self):
        return "Roar"
    def string(self):
        return f"class Wolf name {self.name} id {self.id}"
class Lion:
    def __init__(self, name:str, id:int):
        self.name = name
        self.id = id
    def play_sound(self):
        return "Roar"
    def string(self):
        return f"class Lion name {self.name} id {self.id}"
class Bioson:
    def __init__(self, name:str, id:int):
        self.name = name
        self.id = id
    def play_sound(self):
        return "Moo"
    def string(self):
        return f"class Bioson name {self.name} id {self.id}"
class Parrot:
    def __init__(self, name:str, id:int):
        self.name = name
        self.id = id
    def play_sound(self):
        return "honk"
    def string(self):
        return f"class Parrtot name {self.name} id {self.id}"
class Goose:
    def __init__(self, name:str, id:int):
        self.name = name
        self.id = id
    def play_sound(self):
        return "honk"
    def string(self):
        return f"class Goose name {self.name} id {self.id}"
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


