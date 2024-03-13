

class Zoo:
    def __init__(self):
        self._animals = []

    def add_element(self, name_animal, id_animal, species_animal):
        animal_classes = {
            "Wolf": Wolf,
            "Lion": Lion,
            "Bison": Bison,
            "Parrot": Parrot,
            "Goose": Goose
        }
        animal_class = animal_classes.get(species_animal)
        if animal_class:
            animal = animal_class(name_animal, id_animal)
            self._animals.append(animal)
            print(f"Added {animal} to the zoo.")
        else:
            print("Invalid species. Please choose from: Wolf, Lion, Bison, Parrot, or Goose.")

    def remove_element(self, name_animal):
        self._animals = [animal for animal in self._animals if animal.name_animal != name_animal]

    def display_animals(self):
        print("Animals in the zoo:")
        for animal in self._animals:
            print(f"- {animal}")

    def play_animal_sound(self, name_animal):
        animal = next((animal for animal in self._animals if animal.name_animal == name_animal), None)
        if animal:
            print(f"{animal.name_animal} says: {animal.play_sound()}")
        else:
            print(f"Animal '{name_animal}' not found in the zoo.")


class Animal:
    def __init__(self, name_animal, id_animal):
        self.name_animal = name_animal
        self.id_animal = id_animal

    def __str__(self):
        return f"class {self.__class__.__name__} name {self.name_animal} id {self.id_animal}"

    def play_sound(self):
        pass
        raise NotImplementedError("Subclass must implement abstract method")


class Wolf(Animal):
    def play_sound(self):
        return "Roar"


class Lion(Animal):
    def play_sound(self):
        return "Roar"


class Bison(Animal):
    def play_sound(self):
        return "Moo"


class Parrot(Animal):
    def play_sound(self):
        return "Honk"


class Goose(Animal):
    def play_sound(self):
        return "Honk"


def main():
    zoo = Zoo()

    while True:
        print("\nWhat would you like to do?\n"
              "1. Add animal\n"
              "2. Remove animal\n"
              "3. Display animals\n"
              "4. Play animal sound\n"
              "5. Exit\n")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            print("\nAdding a new animal:")
            name = input("Enter animal name: ")
            animal_id = int(input("Enter animal ID: "))
            species_animal = input("Enter animal species (Wolf, Lion, Bison, Parrot, Goose): ").capitalize()
            zoo.add_element(name, animal_id, species_animal)

        elif choice == "2":
            name_animal = input("Enter animal name to remove: ")
            zoo.remove_element(name_animal)
            print(f"{name_animal} removed from the zoo.")

        elif choice == "3":
            zoo.display_animals()

        elif choice == "4":
            name_animal = input("Enter animal name to play sound: ")
            zoo.display_animals()
            zoo.play_animal_sound(name_animal)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
