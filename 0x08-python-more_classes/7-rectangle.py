#!/usr/bin/python3

"""Defines a recangle"""


class Rectangle:
    """Represents an rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Inits an instance"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __str__(self):
        self.my_print()
        return ""

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        if any(side == 0 for side in [self.width, self.height]):
            return 0
        else:
            return (2 * self.width) + (2 * self.height)

    def my_print(self):
        if self.perimeter:
            x = self.height
            y = self.width
            z = self.print_symbol
            for i in range(self.height):
                print(str(z) * y, end="" if i == (x - 1) else "\n")
