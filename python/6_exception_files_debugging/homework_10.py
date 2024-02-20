def file_worker(file_path, action, text=None):
    """This function can perform 3 operations with files: write, add, read.
        Three arguments must be given:
        path to the file, text to write, correct action 'w', 'a', 'r' """

    try:
        with open(file_path, action) as test_file:
            if action == "w":
                test_file.write(text)
                print("Your text was written to the file.")
            elif action == "a":
                test_file.write(text)
                print("Your text was added to the file.")
            elif action == "r":
                file_text = test_file.read()
                print("File's content: \n", file_text)
    except ValueError:
        print("Wrong action with file")
    except FileNotFoundError:
        print("There is no such file")
    except Exception as e:
        print("There is something wrong: ", e)


file_worker("test_text_file.txt", "w", "1. Some info \n") # correct writing
file_worker("test_text_file.txt", "a", "2. Additional info\n") # correct adding
file_worker("test_text_file.txt", "r", ) # correct reading

file_worker("wrong_file.txt", "r") # wrong filename
file_worker("test_text_file.txt", "wrong_file_operation", "Some info") # wrong operation
