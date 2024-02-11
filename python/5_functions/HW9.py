def calculate_rectangle_area(width, length):
    """
    Area of rectangle calculates by multiplication of width and length of rectangle
    Next steps:
        # Check the type of arguments
        # Check the size of sides
        # Multiply two arguments
    """

    # 1. Check the type of arguments
    if isinstance(width, str):
        try:
            width = int(width)
        except ValueError:
            try:
                width = float(width)
            except ValueError:
                print("Invalid argument of width. Input a valid number!")
                return None
    if isinstance(width, bool):
        width = int(width)

    if isinstance(length, str):
        try:
            length = int(length)
        except ValueError:
            try:
                length = float(length)
            except ValueError:
                print("Invalid argument of length. Input a valid number!")
                return None
    if isinstance(length, bool):
        length = int(length)

    # 2. Check the size of rectangle sides
    if width <= 0 or length <= 0:
        print("One of rectangle side can't be equal 0 or lower. Check the arguments")
        return

    # 3. Multiply two arguments and print the result
    area = width * length
    print("The area of rectangle - " + str(area))

    return area

calculate_rectangle_area(4, 4)
calculate_rectangle_area(4.0, 3)
calculate_rectangle_area(0.1, 0.1)
calculate_rectangle_area("3", 2)
calculate_rectangle_area(10, "10")
calculate_rectangle_area(1e3, "1e8")
calculate_rectangle_area(False, False)
calculate_rectangle_area(True, True)