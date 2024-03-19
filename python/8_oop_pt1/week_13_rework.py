class Zoo:
    _animals = []

    def __init__(self):
        pass

    def show_list():
        return Zoo._animals

    def add_animal(animal_name):
        Zoo._animals.append(animal_name)

    def remove_animal(animal_name):
        try:
            Zoo._animals.remove(animal_name)
        except Exception as error:
            print(error)
            print(f"animal {animal_name} not in list")

init_zoo = Zoo()

class Animal:
    def __init__(self, animal_name, animal_id, animal_sound):
        self.animal_name = animal_name
        self.animal_id = animal_id
        self.animal_sound = animal_sound

    def return_name(self):
        return self.animal_name

    def make_noise(self):
        print(self.animal_sound)



class Wolf(Animal):

    #class_name = (__qualname__)

    def __init__(self, name):
        self.animal_name = name
        self.animal_sound = "Roar"
        self.animal_id = 1

class Lion(Animal):

    #class_name = (__qualname__)

    def __init__(self, name):
        self.animal_name = name
        self.animal_sound = "Mrrrr"
        self.animal_id = 2

class Bison(Animal):

    #class_name = (__qualname__)

    def __init__(self, name):
        self.animal_name = name
        self.animal_sound = "Roar"
        self.animal_id = 1

wolfie_1 = Wolf("genrik")
lion_1 = Lion("timon")
lion_2 = Lion("pumba")
bison_1 = Bison("seger")

Zoo.add_animal(wolfie_1.animal_name)
Zoo.add_animal(lion_1.animal_name)
Zoo.add_animal(lion_2.animal_name)
Zoo.add_animal(bison_1.animal_name)

print(Zoo.show_list())

wolfie_1.make_noise()
lion_1.make_noise()
lion_2.make_noise()
bison_1.make_noise()

Zoo.remove_animal("genrik")

print(Zoo.show_list())

Zoo.remove_animal("tonst")

print(Zoo.show_list())