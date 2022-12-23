#!/usr/bin/python3
"""Contains a class defintion of a Square"""


class Square:
    """Square Class
    This class defines the size of the Square
    with exception handling.

    It also uses the property decorator for the getter and setter methods
    """

    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            self.__size = size

        if size < 0:
            raise ValueError("size must be >= 0")

        if self.__check_tuple(position) is False \
                or self.__check_index(position) is False \
                or self.__check_ints(position) is False \
                or self.__check_values(position) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            self.__size = value

        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if self.__check_tuple(position) is False \
                or self.__check_index(position) is False \
                or self.__check_ints(position) is False \
                or self.__check_values(position) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def __check_tuple(self, value):
        if type(value) is tuple:
            return True
        else:
            return False

    def __check_index(self, value):
        if len(value) == 2:
            return True
        else:
            return False

    def __check_ints(self, value):
        if type(value[0]) is int and type(value[1]) is int:
            return True
        else:
            return False

    def __check_values(self, value):
        if value[0] >= 0 and value[1] >= 0:
            return True
        else:
            return False

    def area(self):
        squareArea = self.__size ** 2

        return (squareArea)

    def my_print(self):
        if self.__size == 0:
            print()
            return None

        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                print('')

        for j in range(1, self.area() + 1):
            if j % self.__size == 1:
                print('{:>{w}}'.format('#', w=self.__position[0] + 1), end='')
            else:
                print('#', end='')

        if j % self.__size == 0 and j > 0:
            print()
