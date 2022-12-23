#!/usr/bin/python3
"""Contains a class defintion of a Square"""


class Square:
    """Square Class
    This class defines the size of the Square
    with exception handling.

    It also uses the property decorator for the getter and setter methods
    """

    def __init__(self, size=0):
        if type(size) is not int:
            return TypeError("size must be an integer")
        else:
            self.size = size

        if size < 0:
            return ValueError("size must be >= 0")

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            return TypeError("size must be an integer")
        else:
            self.__size = value

        if value < 0:
            return ValueError("size must be >= 0")

    def area(self):
        squareArea = self.__size ** 2

        return (squareArea)
