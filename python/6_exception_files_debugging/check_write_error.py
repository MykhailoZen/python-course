try:
    new_file = open("Click_bate.txt", "a")
    new_file.write(" cool story Bob")
    new_file.close()

    new_file = open("Click_bate.txt", "r")
    print(new_file.read())

    new_file = open("Click_bate.txt", "w")
    new_file.write("Not a cool story")
    new_file.close()

    new_file = open("Click_bate.txt", "R")  # put wrong name of the file or incorrect mode
    print(new_file.read())
except FileNotFoundError:
    print("Wrong name")
except Exception as e:
    print(e)
else:
    print("Correct name")
finally:
    print("The End!")
