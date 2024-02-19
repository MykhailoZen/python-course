#The function have 3 arguments: File operation type ,File path ,Content (optional argument).

def function_file (operation_type, path_file, content = None): #The function  perform actions with the file
    try:

        if operation_type == "r":
            with open(path_file, "r") as file:
                print(file.read())
        elif operation_type == "w":
            with open(path_file, "w") as file:
                file.write(content)
               #print(content) - for check content after writing
        elif operation_type == "a":
            with open(path_file, "a") as file:
                file.write(content)
        elif operation_type == "x":
            with open(path_file, "x") as file:
                pass
        else:
            print(f"{operation_type} is unknown operation yet.")
# error handling
    except FileExistsError:
        print(f"{path_file} file is created early. Try another name.")
    except FileNotFoundError:
        print(f"{path_file} not found. Check a path file.")
    except Exception as e:
        print(f" {e} error. You request is unknown for us. Pls edit a request and try again.")




function_file("x", "test.txt") # check a FileExistsError
function_file("r", "test_eror.txt") # check a FileNotFoundError
function_file("w", "test.txt", "12345" ) # check writing a content to file
function_file("a", "test.txt", "additional text " ) #check adding text  to file content
function_file("calling", "test.txt", "text" ) #check wrong operation_type






