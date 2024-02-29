# Practice-coding:
#
# Create a Python file with the next classes:
# 1) Create the class "Zoo" with a protected list named "animals"
# 2) Add methods for adding and removing elements from the list.
# 3) Create classes for Wolf, Lion, Bioson, Parrtot, and Goose
# a) Each class should have fields: name(str), id(int) and constructor.
# b) Each class should have the method "play_sound()" which returns the string with the sound of the animal
# (Use "Roar" for wolf and lion, "Moo" for bison, and "honk" for goose and parrot).
# c) Create method which represents the current class object as a string e.g. output in print command should
# be like "class Lion name Alex id 2".

class Zoo:
    def __init__(self):
        self.__animals = []

    def add_animal(self, animal):
        if isinstance(animal, str):
            self.__animals.append(animal)
        else:
            print(f"Error: {animal} - must be a string.")

    def remove_animal(self, animal):
        try:
            self.__animals.remove(animal)
        except ValueError:
            print(f"Error: {animal} not found in the zoo.")

    def __str__(self):
        return f"Zoo list contain{self.__animals}"

# Example usage class Zoo:
# if __name__ == "__main__":
#     # Creating an Instance of a Class
#     animal1 = Zoo()
#     # Adding a valid element
#     animal1.add_animal("wolf")
#     animal1.add_animal("tiger")
#     # Adding an incorrect element
#     animal1.add_animal(10)
#     # Removing a Present Element
#     animal1.remove_animal("wolf")
#     # Removing a missing element
#     animal1.remove_animal("parrot")
#     # Displaying the contents of a list
#     print(animal1)


class Animals:
    animal_count = 0

    def __init__(self, name):
        self.name = name
        Animals.animal_count += 1
        self.id = Animals.animal_count

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

class Parrtot(Animals):
    def play_sound(self, sound="Honk"):
        return super().play_sound(sound)

class Goose(Animals):
    def play_sound(self, sound="Honk"):
        return super().play_sound(sound)

gray_wolf = Wolf("Gray_W")

# Example usage class Zoo:
if __name__ == "__main__":
    print(repr(gray_wolf))
    print(str(gray_wolf))
    print(gray_wolf)
    print(gray_wolf.play_sound())