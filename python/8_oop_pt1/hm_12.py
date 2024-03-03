"""
Create a Python file with the next classes:

1) Create the class "Zoo" with a protected list named "animals"
2) Add methods for adding and removing elements from the list.
3) Create classes for Wolf, Lion, Bioson, Parrtot, and Goose
    a) Each class should have fields: name(str), id(int) and constructor.
    b) Each class should have the method "play_sound()" which returns the string with the sound of the animal
    (Use "Roar" for wolf and lion, "Moo" for bison, and "honk" for goose and parrot).
    c) Create method which represents the current class object as a string e.g. output in print command should be like
    "class Lion name Alex id 2".
"""


class Zoo:
    __animals = []

    def __init__(self):
        pass

    @classmethod
    def add_animal(cls, animal):
        cls.__animals.append(animal)

    @classmethod
    def remove_animal(cls, animal):
        try:
            cls.__animals.remove(animal)
        except ValueError as Val:
            print(f'This {animal} not in the list of animals. Error: {Val}')
        except Exception as e:
            return 'An error occurred: ' + str(e)

    @classmethod
    def get_list_of_animals(cls):
        return f'All animals in the zoo: {cls.__animals}'


class Wolf:

    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def play_sound(self):
        return f'says - Roar'

    def __str__(self):
        return f'class {self.__class__.__name__}, name {self.name}, with id {self.id},{self.play_sound()}'


class Lion:

    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def play_sound(self):
        return f'says - Roar'

    def __str__(self):
        return f'class {self.__class__.__name__}, name {self.name}, with id {self.id},{self.play_sound()}'


class Bison:

    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def play_sound(self):
        return f'says - Moo'

    def __str__(self):
        return f'class {self.__class__.__name__}, name {self.name}, with id {self.id},{self.play_sound()}'


class Parrot:

    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def play_sound(self):
        return f'says - honk'

    def __str__(self):
        return f'class {self.__class__.__name__}, name {self.name}, with id {self.id},{self.play_sound()}'


class Goose:

    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def play_sound(self):
        return f'says - honk'

    def __str__(self):
        return f'class {self.__class__.__name__}, name {self.name}, with id {self.id},{self.play_sound()}'


if __name__ == "__main__":
    # verification class Zoo
    Zoo.add_animal("Cat")
    Zoo.add_animal('Dog')
    Zoo.add_animal('Crocodile')
    Zoo.add_animal('Tiger')
    print(Zoo.get_list_of_animals())
    # Check ValueError
    Zoo.remove_animal('D')
    print(Zoo.get_list_of_animals())

    Zoo.remove_animal('Crocodile')
    print(Zoo.get_list_of_animals())

    # verification classes Wolf, Lion, Bison, Parrot, Goose
    wolf = Wolf('Ivan', 5478)
    print(wolf)

    lion = Lion('Saran', 4656)
    print(lion)

    bison = Bison('Babe', 45654)
    print(bison)

    parrot = Parrot('Сrow', 45654)
    print(parrot)

    goose = Goose('Baе', 45654)
    print(goose)
