class Zoo:
    def __init__(self):
        self._animals = []
    """
    adds one item to the list
    """
    def add_to_list(self, animal):
        self._animals.append(animal)
    """
    adds list of animals to the list
    """
    def add_list_of_animals(self, animals_list):
        self._animals.extend(animals_list)
    """
    removes all objects matching the id.
    NOTE:  list.remove(object) method does not remove all duplicate values of class Animal,
    only the first object matching the argument object,
    it was decided to manipulate objects by ID, while keeping the container to be a simple list.
    """
    def remove_from_list(self, id):
       self._animals = [item for item in self._animals if item.id != id]


    def __str__(self):
        animals = [str(item) for item in self._animals]
        # return 'Zoo list:\n' + f'{animals}'
        return 'There is the list of zoo animals:\n' + '\n'.join(animals)


#creating a Parent class:
class Animal:
    name: str
    id: int

    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def play_sound(self):
        pass

    def __str__(self):
        return '\u2022 ' + f'Class: {self.__class__.__name__}, name: {self.name}, id number: {self.id}, {self.play_sound()}'


class Wolf(Animal):
    def play_sound(self):
        return 'sound: Wooo'


class Lion(Animal):
    def play_sound(self):
        return 'sound: Hear my Roar'


class Bison(Animal):
    def play_sound(self):
        return 'sound: Moooow'


class Parrot(Animal):
    def play_sound(self):
        return 'sound: Je suis Parrot, honk'

class Goose(Animal):
    def play_sound(self):
        return 'sound: Honk, honk'


# Testing the program
animal_list = [Wolf('Wolfhang', 110), Lion('Hunterr', 111), Bison('Beacon', 112),
               Goose('Google-Doogle', 113), Parrot('Dude', 114)]
new_zoo = Zoo()
new_zoo.add_list_of_animals(animal_list)
print('Check of the list' + '\n' + str(new_zoo))

animal1 = Wolf('Montecurwo', 109)
animal2 = Goose('Winston-blue', 103)
animal3 = Parrot('Nebobr', 130)

new_zoo.add_to_list(animal1)
new_zoo.add_to_list(animal2)
new_zoo.add_to_list(animal3)
print('\n' + 'Check the updated of the list, after adding new animals' + '\n' + str(new_zoo))

new_zoo.remove_from_list(109)
print('\n' + 'Check the updated of the list, after removing animal with id: 109' + '\n' + str(new_zoo))