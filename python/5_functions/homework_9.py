from typing import Union
def calculate_rectangle_area(length: Union[float, int], width: Union[float, int]) -> Union[float, int]:
    """
    Function calculate rectangle area.

    :param length: rectangle length
    :param width: rectangle width
    :return: area of the rectangle
    """
    return length * width


print(calculate_rectangle_area(8, 4))
print(calculate_rectangle_area(3.5, 1.5))
print(calculate_rectangle_area(109, 87))