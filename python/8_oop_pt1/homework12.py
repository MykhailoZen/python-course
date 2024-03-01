"""
Create a Python file with the next classes:
1) Create the class "Zoo" with a protected list named "animals"
2) Add methods for adding and removing elements from the list.
3) Create classes for Wolf, Lion, Bison, Parrot, and Goose
    a) Each class should have fields: name(str), id(int) and constructor.
    b) Each class should have the method "play_sound()" which returns the string with the sound of the animal (Use "Roar" for wolf and lion, "Moo" for bison, and "honk" for goose and parrot).
    c) Create method which represents the current class object as a string e.g. output in print command should be like "class Lion name Alex id 2".
"""


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
        for item in animals_list:
            self.add_to_list(item)
    """
    removes all objects matching the id 
    """
    def remove_from_list(self, id):
       list_size = len(self._animals)
       index = 0
       while index < list_size:
           item = self._animals[index]
           if item.id == id:
               self._animals.pop(index)
               list_size -= 1
           else:
               index += 1

    def __str__(self):
        animals = [str(item) for item in self._animals]
        # return 'Zoo list:\n' + f'{animals}'
        return 'There is the list of zoo animals:\n' + '\n'.join(animals)


class Wolf:
    name: str
    id: int

    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def play_sound(self):
        return 'sound: Wooo'

    def __str__(self):
        return f'Class: {self.__class__.__name__}, name: {self.name}, id number: {self.id}, {self.play_sound()}'


class Lion:
    name: str
    id: int

    def __init__(self, name: str, id: int):
        self.name = str(name)
        self.id = int(id)

    def play_sound(self):
        return 'sound: Roar'

    def __str__(self):
        return f'Class: {self.__class__.__name__}, name: {self.name}, id number: {self.id}, {self.play_sound()}'

class Bison:
    name: str
    id: int

    def __init__(self, name: str, id: int):
        self.name = str(name)
        self.id = int(id)

    def play_sound(self):
        return 'sound: Moo'

    def __str__(self):
        return f'Class: {self.__class__.__name__}, name: {self.name}, id number: {self.id}, {self.play_sound()}'

class Parrot:
    name: str
    id: int

    def __init__(self, name: str, id: int):
        self.name = str(name)
        self.id = int(id)

    def play_sound(self):
        return 'sound: Honk'

    def __str__(self):
        return f'Class: {self.__class__.__name__}, name: {self.name}, id number: {self.id}, {self.play_sound()}'
class Goose:
    name: str
    id: int

    def __init__(self, name: str, id: int):
        self.name = str(name)
        self.id = int(id)

    def play_sound(self):
        return 'sound: Honk'

    def __str__(self):
        return f'Class: {self.__class__.__name__}, name: {self.name}, id number: {self.id}, {self.play_sound()}'

# adding animals too Zoo list and print it:
animal_list = [Wolf('Monty',  101), Wolf('Simon', 102),
               Lion('King', 103), Wolf('Mikki', 104), Wolf('Monty',  101),
               Bison('Boo', 105), Parrot('Gosha', 106), Goose('Goose', 107)]
KyivZoo = Zoo()
KyivZoo.add_list_of_animals(animal_list)
print(KyivZoo)
print('\nRemoving all animals with id 101:')
KyivZoo.remove_from_list(101)
print(KyivZoo)
print('\nAdding new animal: Lion Alex with id 107')
new_animal = Lion("Alex", 107 )
KyivZoo.add_to_list(new_animal)
print(KyivZoo)
print('\nRemove animals with id 107 from the list ')
KyivZoo.remove_from_list(107)
print(KyivZoo)

print(type(Wolf('mike', 110)))