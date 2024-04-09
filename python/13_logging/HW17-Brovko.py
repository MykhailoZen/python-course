# There should be at least two logging levels: debug and info.
# All print statements should be replaced with logging.
# Configure logging to print all log messages to the console,
# and write INFO+ messages to a log file.

import logging

c_handler = logging.StreamHandler()
f_handler = logging.FileHandler("app.log", mode="w")
c_handler.setLevel(logging.DEBUG)
f_handler.setLevel(logging.INFO)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
    handlers=[c_handler, f_handler],
)

logger = logging.getLogger(__name__)


class Zoo:

    def __init__(self):
        self._animals = []
        logging.debug("Zoo class created")
        self.cells: int = 4
        self.animals_held: int = 0

    def add_animal(self, animal):
        if self.animals_held < self.cells:
            self._animals.append(animal)
            self.animals_held += 1
            logger.info(
                f"{animal.name} the {animal.__class__.__name__}"
                " was added to the Zoo"
            )
            logger.info(f"{self.animals_held} out "
                        f"of {self.cells} cells are taken")
        else:
            logger.warning("The Zoo is full!")

    def remove_animal(self, animal):
        self._animals.remove(animal)
        self.animals_held -= 1
        logger.info(
            f"{animal.name} the {animal.__class__.__name__} "
            "was removed from the Zoo"
        )
        logger.info(f"{self.animals_held} out of {self.cells} cells are taken")


class Animal:

    def __init__(self, name, id):
        self.name = name
        self.id = id
        logger.debug(f"{self.__class__.__name__} created")

    def __str__(self):
        return (
            f"class {self.__class__.__name__} "
            f"name {self.name} "
            f"id {self.id} "
            f"sounds like {self.play_sound()}"
        )

    def play_sound(self):
        logger.info("sound played")
        return self.sound


class Wolf(Animal):
    sound = "Woof"


class Lion(Animal):
    sound = "Roar"


class Bison(Animal):
    sound = "Moo"


class Parrot(Animal):
    sound = "Honk"


class Goose(Animal):
    sound = "Honk"


def main():

    zoo = Zoo()
    # an instance of zoo created

    wolf = Wolf("Igor", 1)
    lion = Lion("Ostap", 2)
    bison = Bison("Oleg", 3)
    parrot = Parrot("Natalia", 4)
    goose = Goose("Fedir", 5)

    zoo.add_animal(wolf)
    zoo.add_animal(lion)
    zoo.add_animal(bison)
    zoo.add_animal(parrot)
    zoo.add_animal(goose)
    zoo.remove_animal(lion)

    wolf.play_sound()

    logger.debug("finished")


if __name__ == "__main__":
    main()
