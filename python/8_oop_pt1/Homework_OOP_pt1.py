# Class Wolf
class Wolf:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name})'

    def play_sound(self) -> str:
        return f'Roar, roar, roar'

    def whoami(self) -> str:
        return f'Class {self.__class__.__name__}, name {self.name}, id {self.id}'


# Class Lion
class Lion:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name})'

    def play_sound(self) -> str:
        return f'Roar, roar, roar'

    def whoami(self) -> str:
        return f'Class {self.__class__.__name__}, name {self.name}, id {self.id}'


# Class Bison
class Bison:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name})'

    def play_sound(self) -> str:
        return f'Moo, Moo, Moo'

    def whoami(self) -> str:
        return f'Class {self.__class__.__name__}, name {self.name}, id {self.id}'


# Class Parrot
class Parrot:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name})'

    def play_sound(self) -> str:
        return f'Honk, Honk, Honk'

    def whoami(self) -> str:
        return f'Class {self.__class__.__name__}, name {self.name}, id {self.id}'


# Class Goose
class Goose:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name})'

    def play_sound(self) -> str:
        return f'Honk, Honk, Honk'

    def whoami(self) -> str:
        return f'Class {self.__class__.__name__}, name {self.name}, id {self.id}'


class Zoo:
    def __init__(self):
        self._animals = []

    def show_animals(self):
        print([x.whoami() for x in self._animals])

    def add(self, *args):
        """
        Adding animals to Zoo list
        :param args: any initialized animal
        """
        for x in args:
            self._animals.append(x)
            print(f'Added new animal {x} to Zoo list')

    def remove(self, *args):
        """
        Removing animals from Zoo list
        :param args: any initialized animal
        """
        for x in args:
            self._animals.remove(x)
            print(f'Removed animal {x} from Zoo list')


# zoo = Zoo()
# animal_1 = Lion('Alex', 10)
# animal_2 = Parrot('Bara', 12)
# animal_3 = Wolf('Lui', 11)
# animal_4 = Goose('Martin', 15)
# animal_5 = Bison('Bik', 18)
# zoo.add(animal_1, animal_2, animal_4, animal_5, animal_3)
# zoo.remove(animal_1, animal_3, animal_4)
# print(zoo._animals)