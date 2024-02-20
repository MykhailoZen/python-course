def funny(file_type, file_path, content=None):
    try:
        if file_type == "write":
            with open(file_path, "w") as file:
                file.write(content)
                print(content)
                print("Cool story")
        elif file_type == "read":
            with open(file_path, "r") as file:
                print(file.read())
        else:
            print("What a story?")

    except FileNotFoundError:
        print("Wrong name")
    except Exception as e:
        print(e)
    else:
        print("Correct name")
    finally:
        print("The End!")


funny("write", "Click_bate.txt", "new content")

