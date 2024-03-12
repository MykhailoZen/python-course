class Animal:
    SOUND = ''

    def __init__(self, name, a_id):
        self.name = name
        self.a_id = a_id

    def play_sound(self):
        return self.SOUND

    def __str__(self):
        return f'class {self.__class__.__name__} name {self.name} id {self.a_id}'


class Wolf(Animal):
    SOUND = 'Roar'


wolf_1 = Wolf('Ben', 1)
wolf_2 = Wolf('Dean', 2)
wolf_3 = Wolf('Chuck', 3)


class Lion(Animal):
    SOUND = 'Roar'


lion_1 = Lion('Alex', 1)
lion_2 = Lion('Rex', 2)
lion_3 = Lion('Croissant', 3)


class Bison(Animal):
    SOUND = 'Moo'


bison_1 = Bison('Boo', 1)
bison_2 = Bison('Max', 2)
bison_3 = Bison('Missy', 3)


class Parrot(Animal):
    SOUND = 'Honk'


parrot_1 = Parrot('Petro', 1)
parrot_2 = Parrot('Happy', 2)
parrot_3 = Parrot('Bob', 3)


class Goose(Animal):
    SOUND = 'Honk'


goose_1 = Goose('JZ', 1)
goose_2 = Goose('Lil', 2)
goose_3 = Goose('NK', 3)
