#!/usr/bin/python3
"""Class definition of a Rectangle"""


class Rectangle:
    """Rectangle Class

    Defines a rectangle with exception handling

    It also uses the property decorator for the getter and setter methods
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Prints a message upon deletion of rectangle instance"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Calculates area of rectangle"""
        a = self.__width * self.__height
        return (a)

    def perimeter(self):
        """Calculates perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            p = 0
        else:
            p = 2 * (self.__height + self.__width)
        return (p)

    def __draw(self):
        """Draws the rectangle"""
        shape = ''
        w = self.__width
        h = self.__height

        if w == 0 or h == 0:
            return (shape)

        for i in range(h):
            for j in range(w):
                shape += "#"
            if i != h - 1:
                shape += "\n"
        return (shape)

    def __str__(self):
        """Returns a string representing the shape fo the rectangle"""
        return(self.__draw())

    def __repr__(self):
        """Returns a representation of the rectangle"""
        w = str(eval("self.width"))
        h = str(eval("self.height"))

        return 'Rectangle(' + w + ', ' + h + ')'
