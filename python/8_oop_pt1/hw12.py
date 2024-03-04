
#Create a Python file with the next classes:
#1) Create the class "Zoo" with a protected list named "animals"
#2) Add methods for adding and removing elements from the list.
#3) Create classes for Wolf, Lion, Bioson, Parrtot, and Goose
#a) Each class should have fields: name(str), id(int) and constructor.
#b) Each class should have the method "play_sound()" which returns the string with the sound of the animal (Use "Roar" for wolf and lion, "Moo" for bison, and "honk" for goose and parrot).
#c) Create method which represents the current class object as a string e.g. output in print command should be like "class Lion name Alex id 2".

#1 Task
class Zoo:
    def __init__(self):
        self._animals = []
#2 Task
    def adding_animal(self, animal):
        self._animals.append(animal)

    def removing_animal(self, animal):
        self._animals.remove(animal)

    def printing_animal(self):
        for item in self._animals:
            print(item)

#check
zoopark = Zoo()
zoopark.adding_animal("Pes Patron")
zoopark.adding_animal("Kit Syrskyi")
zoopark.adding_animal("Holub Chotkyi")
zoopark.removing_animal("Holub Chotkyi")
zoopark.printing_animal()



#3
class Wolf:
    def __init__(self, name: str, animal_id: int, constructor):
        self.name = name
        self.animal_id = animal_id
        self.constructor = constructor

    def play_sound(self):
        return "Roar"

    def __str__(self):
        return f"Class {Wolf.__name__} name: {self.name}; id: {self.animal_id}"


anm_1 = Wolf("Wild", 99, True)



class Lion:
    def __init__(self, name: str, animal_id: int, constructor):
        self.name = name
        self.animal_id = animal_id
        self.constructor = constructor

    def play_sound(self):
        return "Roar"

    def __str__(self):
        return f"Class {Lion.__name__} name: {self.name}; id: {self.animal_id}"




class Bioson:
    def __init__(self, name: str, animal_id: int, constructor):
        self.name = name
        self.animal_id = animal_id
        self.constructor = constructor

    def play_sound(self):
        return "Moo"

    def __str__(self):
        return f"Class {Bioson.__name__} name: {self.name}; id: {self.animal_id}"


class Parrot:
    def __init__(self, name: str, animal_id: int, constructor):
        self.name = name
        self.animal_id = animal_id
        self.constructor = constructor

    def play_sound(self):
        return "honk"

    def __str__(self):
        return f"Class {Parrot.__name__} name: {self.name}; id: {self.animal_id}"


class Goose:
    def __init__(self, name: str, animal_id: int, constructor):
        self.name = name
        self.animal_id = animal_id
        self.constructor = constructor

    def play_sound(self):
        return "honk"

    def __str__(self):
        return f"Class {Goose.__name__} name: {self.name}; id: {self.animal_id}"


#Check
anm_1 = Wolf("Wild", 99, True)
print (anm_1)

anm_2 = Lion("Rudy", 5, True)
print (anm_2)

anm_3 = Bioson ("Bucky", 54, True)
print (anm_3)

anm_4 = Parrot ("Kaar", 4, True)
print (anm_4)

anm_5 = Goose ("Long", 1, True)
print (anm_5)



