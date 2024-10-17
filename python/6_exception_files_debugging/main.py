def file_operation(oper_type, path, content=""):
    if oper_type.lower() == "read":
        with open(path, "r") as file:
            for line in file.readlines():
                print(line, end='')
    elif oper_type.lower() == "add":
        with open(path, "a") as file:
            file.write(content)
    else:
        raise Exception("Unexpected argument of 'oper_type' parameter. Expected values 'r' - read of 'add' - add content in the enf of file.")


file_operation("read", "test_data.txt")

file_operation("add", "test_data.txt", "bla-bla")

