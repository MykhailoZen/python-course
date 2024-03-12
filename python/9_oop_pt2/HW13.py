class Zoo:
    def __init__(self):
        self._animals = []

    def animal_add(self, animal_type):
        self._animals.append(animal_type)

    def animal_remove(self, animal_type):
        if animal_type in self._animals:
            self._animals.remove(animal_type)
        else:
            print("Let's find it in Kyiv Zoo")
class Animal:
    def __init__(self, animal_type, animal_id, sound):
        self.animal_type = animal_type
        self.animal_id = animal_id
        self.sound = sound

    def animal_full_info(self):
        return f"Class:     {self.__class__.__name__} \n" \
               f"Name:      {self.animal_type} \n" \
               f"ID:        {self.animal_id} \n" \
               f"Scream:    {self.sound}"

    @classmethod
    def animal_class_creation(cls, animal_type, animal_name, animal_id):
        sounds = {"Wolf": "ROAR!", "Lion": "RAOR!", "Bison": "MOO!", "Goose": "HONK!", "Parrot": "HONK!"}

        if animal_type in sounds:
            sound = sounds[animal_type]
            return globals()[animal_type](animal_name, animal_id, sound)
        else:
            raise ValueError("Is this an animal?")


class Wolf(Animal):
    def __init__(self, animal_name, animal_id, sound):
        super().__init__(animal_name, animal_id, sound)


class Lion(Animal):
    def __init__(self, animal_name, animal_id, sound):
        super().__init__(animal_name, animal_id, sound)


class Bison(Animal):
    def __init__(self, animal_name, animal_id, sound):
        super().__init__(animal_name, animal_id, sound)


class Goose(Animal):
    def __init__(self, animal_name, animal_id, sound):
        super().__init__(animal_name, animal_id, sound)

class Parrot(Animal):
    def __init__(self, animal_name, animal_id, sound):
        super().__init__(animal_name, animal_id, sound)


wolf = Animal.animal_class_creation(animal_type="Wolf", animal_name="YARIK", animal_id="123456")
bison = Animal.animal_class_creation(animal_type="Bison", animal_name="TOLIK", animal_id="2131312sdff")

kyiv_zoo = Zoo()

kyiv_zoo.animal_add(wolf)
kyiv_zoo.animal_add(bison)

print(Wolf.animal_full_info(wolf))