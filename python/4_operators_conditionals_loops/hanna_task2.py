friends = {'Hanna': 45,
           'Ksu': 18,
           'Inna': 19}

girl_name = input("Please, enter the name:")
while girl_name not in friends:
    girl_name = input("Incorrect name. Please, enter another name:")
else:
    if friends[girl_name] < 30:
        print(f"Girl {girl_name} - молодушка")
    else:
        print(f"Girl {girl_name} - выдержаная, как дорогой коньяк")
