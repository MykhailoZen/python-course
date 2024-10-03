import argparse

parser = argparse.ArgumentParser(description='Simple Multiplication')
parser.add_argument('--width', '-w',dest='given_width', type=float,
                    nargs=1, default=1, help='Given width of the rectangle')
parser.add_argument('--length', '-l',dest='given_length', type=float,
                    nargs=1, default=1, help='Given length of the rectangle')

option = parser.parse_args()

class Multipicator:
    def __init__(self, width, length):
        self.area=width*length

try:
    if option.given_width[0] < 0 or option.given_length[0] < 0:
        print("User has to define width and length of rectangle, they cannot be negative")
        exit()
    our_object=Multipicator(option.given_width[0],option.given_length[0])
    print(f"Current rectangle area is {our_object.area}")
except TypeError:
    print("User has to define width and length of rectangle, for help use -h option")
