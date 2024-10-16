def file_function(operation, file_path, content =""):
    try:
        with open(file_path, 'r+') as f:
            if operation == 'read':
                print(f.read())

            elif operation == 'write':
                f.write(content)

            else:
                print('This operation is not supported.')

        f.close()


    except FileNotFoundError:
        print('Incorrect file path. Please type again.')
    except UnboundLocalError as e:
        print(e)
    except Exception as e:
        print(e)

file_function('read', 'file.txt')
file_function('write','file.txt', 'New content to write\n')




