def OperateFile(file_operation_type, file_path, file_content='not_empty'):
    """ Function operates the input file - reads or writes """
    message = "[Message]: "
    try:
        if (file_operation_type.lower() == 'read' or file_operation_type.lower() == "r"):
            with open(file_path, 'r') as file:
                file_content = file.read()
            message += f"File has been read.\n[Content]: {file_content}"
        elif (file_operation_type.lower() == "write" or file_operation_type.lower() == "w"):
            with open(file_path, 'w') as file:
                file.write(file_content)
            message += f"File has been written to.\n[Content]: {file_content}"
        else:
            message += "Unknown file operation type.\nPossible types are: 'write', 'w', 'read', 'r'."
    except FileNotFoundError:
        message += "Specified filename not found. Please provide a valid filename."
    except Exception as e:
        message += f"Unknown error occurred: {e}"
    finally:
        message += "\nFunction operation has ended.\n"
    return message

print(f"Call#1\n{OperateFile('read', 'file1.txt')}")
print(f"Call#2\n{OperateFile('w', 'file1.txt', 'Something1')}")
print(f"Call#3\n{OperateFile('r', 'file2.txt')}")
print(f"Call#4\n{OperateFile('rw', 'file2.txt', 'Something2')}")