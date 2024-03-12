class Zoo:
    def __init__(self):
        self._animals = []

    def add_element(self, animal):
        self._animals.append(animal)

    def remove_element(self, animal):
        if animal in self._animals:
            self._animals.remove(animal)
        else:
            print(f"{animal} is not in the Zoo!")
