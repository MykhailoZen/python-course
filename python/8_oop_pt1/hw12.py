# 1) Create the class "Zoo" with a protected list named "animals"
class Zoo:
    _animals = []
    # 2) Add methods for adding and removing elements from the list.
    def adding(name, id):
        Zoo._animals.append((name, id))

    def removing(name, id):
        Zoo._animals.remove((name, id))
    # Additional method for list all animals in total.
    def inspecting():
        print(Zoo._animals)

# 3) Create classes for Wolf, Lion, Bioson, Parrtot, and Goose
# a) Each class should have fields: name(str), id(int) and constructor.
class Wolf:
    def __init__(self, name, id):
        self.name = name
        self.id = id



    def play_sound(self):
            print("Roar")




    def representing_method(self):
        print(f"Current class:{self.__class__.__name__}, Name: {self.name}, Id: {self.id}")

class Lion:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def play_sound(self):
            print("Roar")

    def representing_method(self):
        print(f"Current class:{self.__class__.__name__}, Name: {self.name}, Id: {self.id}")


class Bioson:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def play_sound(self):
            print("Moo")

    def representing_method(self):
        print(f"Current class:{self.__class__.__name__}, Name: {self.name}, Id: {self.id}")

class Parrot:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def play_sound(self):
            print("Honk")

    def representing_method(self):
        print(f"Current class:{self.__class__.__name__}, Name: {self.name}, Id: {self.id}")

class Goose:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def play_sound(self):
        print("Honk")

    def representing_method(self):
        print(f"Current class:{self.__class__.__name__}, Name: {self.name}, Id: {self.id}")

#Initilizing
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

# Zoo.adding()
Zoo.adding(Lion0.name, Lion0.id)
Zoo.adding(Bioson0.name, Bioson0.id)
Zoo.adding(Wolf1.name, Wolf1.id)
Zoo.adding(Parrot0.name, Parrot0.id)

# Zoo.inspecting()
Zoo.inspecting()
Zoo.removing(Lion0.name, Lion0.id)
Zoo.inspecting()
