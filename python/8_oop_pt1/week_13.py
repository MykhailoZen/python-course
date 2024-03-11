class Zoo:
    _animals = ["Wolf", "Lion", "Bioson", "Parrtot", "Goose"]

    def __init__(self):
        pass


class ShowList(Zoo):
    def show_animal_list():
        return Zoo._animals


class AddAnimal(Zoo):
    def add_animal_list(animal_id):
        Zoo._animals.append(animal_id)


class RemoveAnimal(Zoo):
    def remove_animal_list(animal_id):
        try:
            Zoo._animals.remove(animal_id)
        except Exception as error:
            print(error)
            print("animal not in list")




print(ShowList.show_animal_list())
AddAnimal.add_animal_list("Cat")
print(ShowList.show_animal_list())
(RemoveAnimal.remove_animal_list("Lion"))
print(ShowList.show_animal_list())
