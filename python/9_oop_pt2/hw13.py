
#Refactor your previous homework in an OOP way.



#1 Task
#adding only if/else for  removing_animal function; new  printing for checking
class Zoo:
    def __init__(self):
        self._animals = []
#2 Task
    def adding_animal(self, animal):
        self._animals.append(animal)

    def removing_animal(self, animal):
        if animal in self._animals:
            self._animals.remove(animal)
        else:
            print(f"Typed animal {animal} is not found in Zoo list and not removed")



    def printing_animals(self):
        print(f"Animals list in Zoo:{self._animals}")

#check
zoopark = Zoo()
zoopark.adding_animal("Pes Patron")
zoopark.adding_animal("Kit Syrskyi")
zoopark.adding_animal("Holub Chotkyi")
zoopark.removing_animal("Holub Chotkyi")
zoopark.removing_animal("Pterodaktl")

zoopark.printing_animals()


#create a new clasa Animal for using inheritance in Wolf, Lion, Parrot, Goose classes; and additional sound info in sting output
class Animal:

    def __init__(self, name: str, animal_id: int):
        self.name = name
        self.animal_id = animal_id

    def play_sound(self):
        pass

    def __str__(self):
        return f"Class {type(self).__name__}; name: {self.name}; id: {self.animal_id}; animal sound: {self.play_sound()}"

#using Overriding Methods in Wolf, Lion, Parrot, Goose classes for change individual sound
#3 Task
class Wolf(Animal):

    def play_sound(self):
        return "Roar"

class Lion(Animal):
    def play_sound(self):
        return "Roar"

class Bioson(Animal):
    def play_sound(self):
        return "Moo"

class Parrot(Animal):

    def play_sound(self):
        return "honk"

class Goose(Animal):

    def play_sound(self):
        return "honk"


#Check
anm_1 = Wolf("Wild", 99)
print (anm_1)

anm_2 = Lion("Rudy", 5)
print (anm_2)

anm_3 = Bioson ("Bucky", 54)
print (anm_3)

anm_4 = Parrot ("Kaar", 4)
print (anm_4)

anm_5 = Goose ("Long", 1)
print (anm_5)







