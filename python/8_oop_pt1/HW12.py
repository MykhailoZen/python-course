# 1) Create the class "Zoo" with a protected list named "animals"
# 2) Add methods for adding and removing elements from the list.

class Zoo:

    def __init__(self):
        self._animals = []

    def add(self, item):
        self._animals.append(item)

    def remove(self, item):
        try:
            return self._animals.remove(item)
        except ValueError:
            print("List is empty")


# 3) Create classes for Wolf, Lion, Bison, Parrot, and Goose
# a) Each class should have fields: name(str), id(int) and constructor.
# b) Each class should have the method "play_sound()" which returns the string with the sound of the animal
# (Use "Roar" for wolf and lion, "Moo" for bison, and "honk" for goose and parrot).
# c) Create method which represents the current class object as a string e.g. output in print command should be like
# "class Lion name Alex id 2".

class Wolf:
    SOUND = 'Roar'

    def __init__(self, name, a_id):
        self.name = name
        self.a_id = a_id

    @staticmethod
    def play_sound():
        return Wolf.SOUND

    def __str__(self):
        return f'class {self.__class__.__name__} name {self.name} id {self.a_id}'


wolf_1 = Wolf('Ben', 1)
wolf_2 = Wolf('Dean', 2)
wolf_3 = Wolf('Chuck', 3)


class Lion:
    SOUND = 'Roar'

    def __init__(self, name, a_id):
        self.name = name
        self.a_id = a_id

    @staticmethod
    def play_sound():
        return Lion.SOUND

    def __str__(self):
        return f'class {self.__class__.__name__} name {self.name} id {self.a_id}'


lion_1 = Lion('Alex', 1)
lion_2 = Lion('Rex', 2)
lion_3 = Lion('Croissant', 3)


class Bison:
    SOUND = 'Moo'

    def __init__(self, name, a_id):
        self.name = name
        self.a_id = a_id

    @staticmethod
    def play_sound():
        return Bison.SOUND

    def __str__(self):
        return f'class {self.__class__.__name__} name {self.name} id {self.a_id}'


bison_1 = Bison('Boo', 1)
bison_2 = Bison('Max', 2)
bison_3 = Bison('Missy', 3)


class Parrot:
    SOUND = 'Honk'

    def __init__(self, name, a_id):
        self.name = name
        self.a_id = a_id

    @staticmethod
    def play_sound():
        return Parrot.SOUND

    def __str__(self):
        return f'class {self.__class__.__name__} name {self.name} id {self.a_id}'


parrot_1 = Parrot('Petro', 1)
parrot_2 = Parrot('Happy', 2)
parrot_3 = Parrot('Bob', 3)


class Goose:
    SOUND = 'Honk'

    def __init__(self, name, a_id):
        self.name = name
        self.a_id = a_id

    @staticmethod
    def play_sound():
        return Goose.SOUND

    def __str__(self):
        return f'class {self.__class__.__name__} name {self.name} id {self.a_id}'


goose_1 = Goose('JZ', 1)
goose_2 = Goose('Lil', 2)
goose_3 = Goose('NK', 3)
