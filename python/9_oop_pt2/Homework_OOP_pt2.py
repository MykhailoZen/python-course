class Animal:
    """
    Class implementing Animal class
    """
    _animal_sound = None

    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name})'

    def play_sound(self) -> str:
        if not self._animal_sound:
            return f"Animal sound is unknown"
        return self._animal_sound

    def whoami(self) -> str:
        return f'Class {self.__class__.__name__}, name {self.name}, id {self.id}'


class Wolf(Animal):
    """
    Class implementing Wolf animal
    """
    _animal_sound = "Roar, roar, roar"


class Lion(Animal):
    """
    Class implementing Lion animal
    """
    _animal_sound = "Roar, roar, roar"


class Bison(Animal):
    """
    Class implementing Bison animal
    """
    _animal_sound = "Moo, Moo, Moo"


class Parrot(Animal):
    """
    Class implementing Parrot animal
    """
    _animal_sound = "Honk, Honk, Honk"


class Goose(Animal):
    """
    Class implementing Goose animal
    """
    _animal_sound = "Honk, Honk, Honk"


class Zoo:
    """
    Class implementing Zoo object and adding/removing/showing animals to object
    """
    def __init__(self):
        self._animals = []

    def show_animals(self):
        if not self._animals:
            return f'There are no animals yet'
        else:
            return [x.whoami() for x in self._animals]

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


zoo = Zoo()
animal_1 = Lion('Alex', 10)
animal_2 = Parrot('Bara', 12)
animal_3 = Wolf('Lui', 11)
animal_4 = Goose('Martin', 15)
animal_5 = Bison('Bik', 18)
zoo.add(animal_1, animal_2, animal_4, animal_5, animal_3)
# zoo.remove(animal_1, animal_3, animal_4)
print(zoo.show_animals())
