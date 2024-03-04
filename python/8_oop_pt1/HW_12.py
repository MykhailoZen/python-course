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
        _animals (list): Protected list of animals in the zoo.
    Methods:
        get_animal: Returns a list of animals (if in the future we need to work with a list of animals.).
        add_animal: Adds an animal to the list.
        remove_animal: Removes an animal from the zoo.
    """
    def __init__(self):
        self._animals = []

    def get_animal(self):
        return self._animals

    def add_animal(self, animal):
        try:
            if not isinstance(animal, str):
                raise ValueError("Value must be a string")
            self._animals.append(animal)
        except ValueError as err:
            print(f"Error setting value: {err}")

    def remove_animal(self, animal):
        try:
            self._animals.remove(animal)
        except ValueError:
            print(f"Error: {animal} - not found in the zoo.")

    def __str__(self):
        return f"<Zoo> with {len(self._animals)} animals: {self._animals}"


class Animal:
    """
    A parent class representing animals.
    This class contains a constructor for creating instances of child classes.
    Attributes:
        name (str): The name of the animal.
        id (int): The unique identifier of the animal.
    Class Attributes:
        _sound: Define a variable in the parent class (None), will be redefined to be unique for child classes (str).
        _animal_count (int): A class-level counter to keep track of the number of animals created.
    Methods:
        __init__: Initializes an instance of the Animals class.
        __str__: Returns a string representation of the animal.
        __repr__: Returns a string representation of the animal suitable for debugging.
        play_sound: Returns a string representing the sound made by the animal.
    """
    _sound = None
    _animal_count = 0

    def __init__(self, name):
        self.name = name
        Animal._animal_count += 1
        self.id = Animal._animal_count

    def __str__(self):
        return f"{self.name} has id: {self.id}"

    def __repr__(self):
        class_name = type(self).__name__
        return f" class {class_name}(name={self.name!r}, id={self.id!r})"

    def play_sound(self):
        return f"{self.name} says {self._sound}"


class Wolf(Animal):
    _sound = "Roar"


class Lion(Animal):
    _sound = "Roar"


class Bison(Animal):
    _sound = "Moo"


class Parrot(Animal):
    _sound = "Honk"


class Goose(Animal):
    _sound = "Honk"


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
    # Getting a list of animals
    print(animal1.get_animal())
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
