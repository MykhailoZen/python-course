'''1) Create the class "Zoo" with a protected list named "animals"'''

class Zoo():
    def __init__(self):
        self._animals = []

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
class Animal:
    sound = "Roar"
    def __init__(self, name, id):
        self._name = name
        self._id = id
    '''3.b Class method "play_sound()" which returns the string with the sound'''
    @classmethod
    def play_sound(cls):
        return cls.sound
    '''c) Create method which represents the current class object as a string'''
    def current_class(self):
        return f'class {type(self).__name__}, name: {self._name} id {self._id}'

'''3) Create classes for Wolf, Lion, Bioson, Parrtot, and Goose

a) Each class should have fields: name(str), id(int) and constructor.

b) Each class should have the method "play_sound()" which returns the 
string with the sound of the animal (Use "Roar" for wolf and lion, "Moo" 
for bison, and "honk" for goose and parrot). 

c) Create method which represents the current class object as a string 
e.g. output in print command should be like "class Lion name Alex id 2".'''

class Wolf(Animal):
    pass
class Lion(Wolf):
    pass
class Bison(Animal):
    sound = "Moo"
class Parrot(Animal):
    sound = "honk"
class Goose(Parrot):
    pass

w = Wolf("Wolf_4", 4)
print(w.play_sound())
print(w.current_class())

l = Lion("Lion_2", 2)
print(l.play_sound())
print(l.current_class())

b = Bison("Bison_3", 3)
print(b.play_sound())
print(b.current_class())

p = Parrot("Parrot_1", 1)
print(p.play_sound())
print(p.current_class())

g = Goose("Goose_5", 5)
print(g.play_sound())
print(g.current_class())

