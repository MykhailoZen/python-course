# Practice-coding:
#
# Create a Python file with the next classes:
# 1) Create the class "Zoo" with a protected list named "animals"
# 2) Add methods for adding and removing elements from the list.
# 3) Create classes for Wolf, Lion, Bison, Parrot, and Goose
# a) Each class should have fields: name(str), id(int) and constructor.
# b) Each class should have the method "play_sound()" which returns the string with the sound of the animal
# (Use "Roar" for wolf and lion, "Moo" for bison, and "honk" for goose and parrot).
# c) Create method which represents the current class object as a string e.g. output in print command should
# be like "class Lion name Alex id 2".

class Zoo:
    """Class for representing a zoo.
    This class is designed to store and manage a list of animals in a zoo.
    Attributes:
        __animals (list): List of animals in the zoo.
    Methods:
        add_animal(animal): Adds an animal to the zoo.
        remove_animal(animal): Removes an animal from the zoo.
    """
    def __init__(self):
        self.__animals = []

    def add_animal(self, animal):
        try:
            if not isinstance(animal, str):
                raise ValueError("Value must be a string")
            self.__animals.append(animal)
        except ValueError as err:
            print(f"Error setting value: {err}")

    def remove_animal(self, animal):
        try:
            self.__animals.remove(animal)
        except ValueError:
            print(f"Error: {animal} - not found in the zoo.")

    def __str__(self):
        return f"Zoo list contain: {self.__animals}"


class Animals:
    """
    A parent class representing animals.
    This class contains a constructor for creating instances of child classes.
    Attributes:
        name (str): The name of the animal.
        id (int): The unique identifier of the animal.
    Class Attributes:
        __animal_count (int): A class-level counter to keep track of the number of animals created.
    Methods:
        __init__: Initializes an instance of the Animals class.
        __str__: Returns a string representation of the animal.
        __repr__: Returns a string representation of the animal suitable for debugging.
        play_sound: Returns a string representing the sound made by the animal.
    """
    __animal_count = 0

    def __init__(self, name):
        self.name = name
        Animals.__animal_count += 1
        self.id = Animals.__animal_count

    def __str__(self):
        return f"{self.name} has id: {self.id}"

    def __repr__(self):
        class_name = type(self).__name__
        return f" class {class_name}(name={self.name!r}, id={self.id!r})"

    def play_sound(self, sound):
        return f"{self.name} says {sound}"


class Wolf(Animals):
    def play_sound(self, sound="Roar"):
        return super().play_sound(sound)

class Lion(Animals):
    def play_sound(self, sound="Roar"):
        return super().play_sound(sound)

class Bison(Animals):
    def play_sound(self, sound="Moo"):
        return super().play_sound(sound)

class Parrot(Animals):
    def play_sound(self, sound="Honk"):
        return super().play_sound(sound)

class Goose(Animals):
    def play_sound(self, sound="Honk"):
        return super().play_sound(sound)



if __name__ == "__main__":
    # Example usage class Zoo:
    print("Example usage class Zoo:")
    # Creating an Instance of a Class
    animal1 = Zoo()
    # Adding a valid element
    animal1.add_animal("wolf")
    animal1.add_animal("tiger")
    # Adding an incorrect element
    animal1.add_animal(10)
    # Removing a Present Element
    animal1.remove_animal("wolf")
    # Removing a missing element
    animal1.remove_animal("parrot")
    # Displaying the contents of a list
    print(animal1)

    # Example usage classes Wolf, Lion, Bison, Parrot, and Goose:
    print("Example usage classes Wolf, Lion, Bison, Parrot, and Goose:")
    # Creating an Instance of a Class
    gray_wolf = Wolf("Gray_Wolf")
    yellow_lion = Lion("Yellow_Lion")
    blue_bison = Bison("Blue_Bison")
    green_parrot = Parrot("Green_Parrot")
    white_goose = Goose("White_Goose")
    # check method "play_sound()" which returns the string with the sound of the animal
    print(gray_wolf.play_sound())
    print(blue_bison.play_sound())
    print(green_parrot.play_sound())
    # method which represents the current class object as a string to the developer
    print(repr(gray_wolf))
    print(repr(white_goose))
    # method which represents the current class object as a string to the user
    print(str(yellow_lion))
    print(blue_bison)
