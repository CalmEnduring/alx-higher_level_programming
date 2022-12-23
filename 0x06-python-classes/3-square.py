#!/usr/bin/python3
"""Contains a class definition of Square"""


class Square:
    """Square Class
    This class defines the attritbute size of the Square
    with exception handling
    """

    def __init__(self, size=0):
        if not type(size) is int:
            raise TypeError("size must be an integer")
        else:
            self.__size = size

        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculates the area of the square"""
        squareArea = self.__size ** 2

        return (squareArea)
