#Refactored Code:
class Zoo:
    _animals = []
    def __init__(self, list):
        self.list = list

    def adding(self, name, id):
        self._animals.append((self.name, self.id))

    def removing(name, id):
        self._animals.remove((self.name, self.id))

    def inspecting(self):
        print(self._animals)


class Mammals():
    def prpt(self):
        print("Properties of Mammalas...")

class Birds():
    def prpt(self):
        print("Propertioes of Birds...")

class Wolf(Zoo, Mammals):
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.adding(self.name, self.id)

    def play_sound(self):
            print("Roar")

    def representing_method(self):
        print(f"Current class:{self.__class__.__name__}, Name: {self.name}, Id: {self.id}")

class Lion(Zoo, Mammals):
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.adding(self.name, self.id)

    def play_sound(self):
            print("Roar")

    def representing_method(self):
        print(f"Current class:{self.__class__.__name__}, Name: {self.name}, Id: {self.id}")

class Bioson(Zoo, Mammals):
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.adding(self.name, self.id)

    def play_sound(self):
        print("Moo")

    def representing_method(self):
        print(f"Current class:{self.__class__.__name__}, Name: {self.name}, Id: {self.id}")

#2 usage
class Parrot(Zoo, Birds):
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.adding(self.name, self.id)

    def play_sound(self):
        print("Honk")

    def representing_method(self):
        print(f"Current class:{self.__class__.__name__}, Name: {self.name}, Id: {self.id}")

class Goose(Zoo, Birds):
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.adding(self.name, self.id)

    def play_sound(self):
        print("Honk")

    def representing_method(self):
        print(f"Current class:{self.__class__.__name__}, Name: {self.name}, Id: {self.id}")


#Initilizing
anim = [Wolf("asa", 2), Lion('Lionik', 43), Wolf('sosik', 22)]
soso = Zoo(anim)
soso.inspecting()
Lion1 = Lion("Balex", 1)
soso.inspecting()


Lion0 = Lion("Alex", 0)

Lion1 = Lion("Balex", 1)
Wolf0 = Wolf("Wolfik", 0)
Wolf1 = Wolf("Moolfik", 1)
Bioson0 = Bioson("Bios", 0)
Bioson1 = Bioson("Uefi", 1)
Parrot0 = Parrot("Parrotik", 0)
Parrot1 = Parrot("Repeatik", 1)
Goose0 = Goose("TryFly", 0)
Goose1 = Goose("FlyTry", 1)

#Inspecting severals attributes
print(Bioson1.id)
print(Goose0.name)
print(Wolf0.name)
print(Lion0.id, end="\n\n")

#Several Sounds
Bioson1.play_sound()
Parrot1.play_sound()
Goose0.play_sound()
Lion1.play_sound()
print()

#Several representing methods
Lion1.representing_method()
Parrot0.representing_method()
Goose1.representing_method()
print()


Wolf1.prpt()
Bioson0.prpt()
Goose0.prpt()
