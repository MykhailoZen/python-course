"""3) Create classes for Wolf, Lion, Bioson, Parrtot, and Goose

a) Each class should have fields: name(str), id(int) and constructor.

b) Each class should have the method "play_sound()" which returns the string with the sound of the animal
(Use "Roar" for wolf and lion, "Moo" for bison, and "honk" for goose and parrot).

c) Create method which represents the current class object as a string
e.g. output in print command should be like "class Lion name Alex id 2"."""


class Wolf:

    class_name = (__qualname__)

    def __init__(self):
        self.name = "wolfiiiie"
        self.animal_id = 0
    def play_sound(self):
        return "Roar"
    def animal_info(self):
        info_string = f"class {self.class_name} name {self.name} id {self.animal_id}"
        print(info_string)


class Lion:

    class_name = (__qualname__)

    def __init__(self):
        self.name = "king lion"
        self.animal_id = 1
    def play_sound(self):
        return "Roar"
    def animal_info(self):
        info_string = f"class {self.class_name} name {self.name} id {self.animal_id}"
        print(info_string)

class Bioson:

    class_name = (__qualname__)

    def __init__(self):
        self.name = "bisssie"
        self.animal_id = 2
    def play_sound(self):
        return "Moo"
    def animal_info(self):
        info_string = f"class {self.class_name} name {self.name} id {self.animal_id}"
        print(info_string)


class Parrtot:

    class_name = (__qualname__)

    def __init__(self):
        self.name = "pirate P"
        self.animal_id = 3
    def play_sound(self):
        return "honk"
    def animal_info(self):
        info_string = f"class {self.class_name} name {self.name} id {self.animal_id}"
        print(info_string)

class Goose:

    class_name = (__qualname__)

    def __init__(self):
        self.name = "Montana"
        self.animal_id = 4
    def play_sound(self):
        return "honk"
    def animal_info(self):
        info_string = f"class {self.class_name} name {self.name} id {self.animal_id}"
        print(info_string)

init_wolf = Wolf()
init_lion = Lion()
init_bioson = Bioson()
init_parrtot = Parrtot()
init_goose = Goose()

print(init_wolf.play_sound())
init_wolf.animal_info()

print(init_lion.play_sound())
init_lion.animal_info()

print(init_bioson.play_sound())
init_bioson.animal_info()

print(init_parrtot.play_sound())
init_parrtot.animal_info()

print(init_goose.play_sound())
init_goose.animal_info()
