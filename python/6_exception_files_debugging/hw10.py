
def file_operation(work_with_file, file_path):
    try:
        if work_with_file == "write":
            with open(file_path, "w") as file:
                info_w = input("Write a text: ")
                file.write(info_w)
        elif work_with_file == "read":
            with open(file_path, "r") as file:
                print(file.read())
    except Exception as e:
        print(e)

file_operation("write", "sample.txt")
file_operation("read", "sample.txt")
