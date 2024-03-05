class Zoo:
    def __init__(self):
        self._animals = []

    def animal_add(self, animal):
        self._animals.append(animal)

    def animal_remove(self, animal):
        if animal in self._animals:
            self._animals.remove(animal)
        else:
            print("Not found. Try to find it in Kyiv Zoo")


class Animal():
    def __init__(self, name, animal_id, sound):
        self.name = name
        self.animal_id = animal_id
        self.sound = sound

    def animal_sound(self):
        return self.sound


    def __str__(self):
        return f"Class: {self.__class__.__name__}, Name: {self.name}, ID: {self.animal_id}"


class Wolf():
    def __init__(self, name, animal_id):
        self.animal = Animal(name, animal_id, "Roar")

    def animal_sound(self):
        return self.animal.animal_sound()


class Lion:
    def __init__(self, name, animal_id):
        self.animal = Animal(name, animal_id, "Roar")

    def animal_sound(self):
        return self.animal.animal_sound()

class Bison:
    def __init__(self, name, animal_id):
        self.animal = Animal(name, animal_id, "Moo")

    def animal_sound(self):
        return self.animal.animal_sound()

class Goose:
    def __init__(self, name, animal_id):
        self.animal = Animal(name, animal_id, "honk")

    def animal_sound(self):
        return self.animal.animal_sound()

class Parrot:
    def __init__(self, name, animal_id):
        self.animal = Animal(name, animal_id, "honk")

    def animal_sound(self):
        return self.animal.animal_sound()


berlin_zoo = Zoo()

bison = Bison("Bull", 2221)
wolf = Wolf("Whitey", 201)
parrot = Parrot("Cox", 32)
lion = Lion("Alex", 111)
goose = Goose("Gun", 999)

berlin_zoo.animal_add(wolf)
berlin_zoo.animal_add(parrot)
berlin_zoo.animal_remove(bison)
berlin_zoo.animal_add(lion)
berlin_zoo.animal_add(goose)
berlin_zoo.animal_add(bison)


