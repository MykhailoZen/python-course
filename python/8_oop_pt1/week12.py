class Zoo:
    _animals = ["Wolf", "Lion", "Bioson", "Parrtot", "Goose"]

    def __init__(self):
        pass
    def show_list():
        return Zoo._animals

    def add_animal(animal_id):
        Zoo._animals.append(animal_id)

    def remove_animal(animal_id):
        try:
            Zoo._animals.remove(animal_id)
        except Exception as error:
            print(error)
            print("animal not in list")


init_zoo = Zoo()
#print(Zoo.show_list())
#print(Zoo.add_animal("Cat"))
#print(Zoo.show_list())
print(Zoo.remove_animal("Lffffon"))
print(Zoo.show_list())

