students = {'Alan': 68, 'Roslyn': 48, 'Bertha': 50, 'Sally': 95, 'Rachel': 11, 'John': 95,
            'Derek': 82, 'Kevin': 34, 'Michael': 31, 'Richard': 12}


def find_score():
    while True:
        search = input("Enter a name of the student to find out the score (or type 'Stop' to exit): ")

        if search.lower() == "stop":
            print("Done")
            break

        if search in students:
            print("Student %s has %d points." % (search, students[search]))
            break
        else:
            print("Unfortunately, there is no %s on the list, please try again." % search)


# Call the function
find_score()