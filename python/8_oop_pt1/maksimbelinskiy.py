class Zoo:

    __animals = []

    def __init__(self):
        pass

    def addEl(self, element):
        self.__animals.append(element)

    def delEl(self, element):
        self.__animals.remove(element)

    def prnEl(self):
        print(self.__animals)

class Wolf:

    __wolfid = 0

    def __init__(self, name):
        self.name = name
        Wolf.__wolfid += 1
        self.id = Wolf.__wolfid

    def play_sound(self):
        print("Roar")

    def whoami(self):
        cname = type(self).__name__
        print(f"Class: {cname}, Name: {self.name}, ID: {self.id}")


class Lion:

    __lionid = 0

    def __init__(self, name):
        self.name = name
        Lion.__lionid += 1
        self.id = Lion.__lionid

    def play_sound(self):
        print("Roar")

    def whoami(self):
        cname = type(self).__name__
        print(f"Class: {cname}, Name: {self.name}, ID: {self.id}")



class Bison:

    __bisonid = 0

    def __init__(self, name):
        self.name = name
        Bison.__bisonid += 1
        self.id = Bison.__bisonid

    def play_sound(self):
        print("Moo")

    def whoami(self):
        cname = type(self).__name__
        print(f"Class: {cname}, Name: {self.name}, ID: {self.id}")


class Goose:

    __gooseid = 0

    def __init__(self, name):
        self.name = name
        Goose.__gooseid += 1
        self.id = Goose.__gooseid

    def play_sound(self):
        print("Honk")

    def whoami(self):
        cname = type(self).__name__
        print(f"Class: {cname}, Name: {self.name}, ID: {self.id}")

class Parrot:

    __parrotid = 0

    def __init__(self, name):
        self.name = name
        Parrot.__parrotid += 1
        self.id = Parrot.__parrotid

    def play_sound(self):
        print("Honk")

    def whoami(self):
        cname = type(self).__name__
        print(f"Class: {cname}, Name: {self.name}, ID: {self.id}")