'''1) Create the class "Zoo" with a protected list named "animals"'''

class Zoo():
    _animals = []
    '''
    def __init__(self, animals):
        self.__animals = animals
        '''
    '''2.1 Method for adding elements to the list'''
    def add_elements(self, item):
        self._animals.append(item)

    '''2.2 Method for removing elements from the list'''
    def rm_elements(self, item):
        if item in self._animals:
            self._animals.remove(item)
        else:
            raise ValueError("No such an item in the list")
    def __str__(self):
        return f'Final_list_of_animals: {" ".join(self._animals)}'

'''player = Zoo(["dog", "cat", "wolf", "lion"])'''
player = Zoo()
player.add_elements('tiger')
player.add_elements('cat')
player.add_elements('wolf')
print(player)
player.rm_elements("cat")
print(player)
player.add_elements('rhino')
print(player)

'''3.a Create class for Wolf. This class should have fields: name(str), id(int) and constructor'''
class Wolf:
    def __init__(self, name, id):
        self._name = str(name)
        self._id = int(id)
    '''3.b Static method "play_sound()" which returns the string with the sound'''
    def play_sound():
        return "Roar"
    '''c) Create method which represents the current class object as a string'''
    def current_class(self):
        return f'class {type(self).__name__}, name: {self._name} id {self._id}'

print(Wolf.play_sound())
wolf = Wolf("Alex_5", 5)
print(wolf.current_class())

'''3.a Create class for Lion. This class should have fields: name(str), id(int) and constructor'''
class Lion:
    def __init__(self, name, id):
        self._name = name
        self._id = id
    '''b) Static method "play_sound()" which returns the string with the sound'''
    def play_sound():
        return "Roar"
    '''c) Create method which represents the current class object as a string'''
    def current_class(self):
        return f'class {type(self).__name__}, name: {self._name} id {self._id}'

print(Lion.play_sound())
lion = Lion("Alex_4", 4)
print(lion.current_class())

'''3.a Create class for Bison. This class should have fields: name(str), id(int) and constructor'''
class Bison:
    def __init__(self, name, id):
        self._name = name
        self._id = id
    '''b) Static method "play_sound()" which returns the string with the sound'''
    def play_sound():
        return "Moo"
    '''c) Create method which represents the current class object as a string'''
    def current_class(self):
        return f'class {type(self).__name__}, name: {self._name} id {self._id}'

print(Bison.play_sound())
bison = Bison("Alex_3", 3)
print(bison.current_class())

'''3.a Create class for Parrot. This class should have fields: name(str), id(int) and constructor'''
class Parrot:
    def __init__(self, name, id):
        self._name = name
        self._id = id
    '''b) Static method "play_sound()" which returns the string with the sound'''
    def play_sound():
        return "Honk"
    '''c) Create method which represents the current class object as a string'''
    def current_class(self):
        return f'class {type(self).__name__}, name: {self._name} id {self._id}'

print(Parrot.play_sound())
parrot = Parrot("Alex_2", 2)
print(parrot.current_class())

'''3.a Create class for Goose. This class should have fields: name(str), id(int) and constructor'''
class Goose:
    def __init__(self, name, id):
        self._name = str(name)
        self._id = int(id)
    '''b) Static method "play_sound()" which returns the string with the sound'''
    def play_sound():
        return "Honk"
    '''c) Create method which represents the current class object as a string'''
    def current_class(self):
        return f'class {type(self).__name__}, name: {self._name} id {self._id}'

print(Goose.play_sound())
goose = Goose("Alex_1", 1)
print(goose.current_class())
