#Refactored Code:
class Zoo:
    def __init__(self):
        self._animals = []

    def add(self, animal):
        self._animals.append(animal)

    def remove(self, animal):
        if animal in self._animals:
            self._animals.remove(animal)
        else:
            print(f"{animal} is not in the Zoo list")
            pass

    def inspect(self):
        print(self._animals)

class Animal:
    def __init__(self, name):
        self.name = name

    def represent_method(self):
        print(f"Current class:{self.__class__.__name__}, Name: {self.name}")

class Mammal(Animal):
    def prpt(self):
        print("Properties of Mammalas: Fur, Vertebrates, Produce milk")

class Bird(Animal):
    def prpt(self):
        print("Propertioes of Birds: Feathers, Wings, Beaks or Bills.")

class Wolf(Mammal):
    def play_sound(self):
            print("Roar")

class Lion(Mammal):
    def play_sound(self):
            print("Roar")

class Bioson(Mammal):
    def play_sound(self):
        print("Moo")

class Parrot(Bird):
    def play_sound(self):
        print("Honk")

class Goose(Bird):
    def play_sound(self):
        print("Honk")

#Initilizing
my_zoo = Zoo()

lion_alex = Lion("Alex")
lion_balex = Lion("balex")
parrot_papu = Parrot("papu")

my_zoo.add(lion_alex.name)
my_zoo.add(lion_balex.name)
my_zoo.remove(parrot_papu.name)
my_zoo.remove(lion_balex.name)

goose_brad = Goose("Brad")
my_zoo.add(goose_brad.name)

lion_alex.prpt()
lion_alex.represent_method()
my_zoo.inspect()
