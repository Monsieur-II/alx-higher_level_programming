#!/usr/bin/python3
"""Defines a Rectangle Class"""
from base import Base


class Rectangle(Base):
    """
    A class to create Rectangle objects from
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initiates an instance
        Args:
            width: the width
            height the height
            x: position on x-axis
            y: position on y-axis
            id: id of the Rectangle object
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.width_height_validator("width", width)
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.width_height_validator("height", height)
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.x_y_validator("x", x)
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.x_y_validator("y", y)
        self.__y = y

    @staticmethod
    def width_height_validator(name, value):
        """validates value of name"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    @staticmethod
    def x_y_validator(name, value):
        """validates value of name"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def __str__(self):
        """Returns string representation of rectangle"""
        return "[Rectangle] \
({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def display(self):
        """Prints square with '#'"""
        if any(size == 0 for size in [self.__height, self.__width]):
            print()
        else:
            position = (self.__x, self.__y)
            for i in range(position[1]):
                print()
            x = position[0]
            for i in range(self.__height):
                print(' ' * x, end="")
                print('#' * self.__width)

    def update(self, *args, **kwargs):
        """Updates the attributes of a rectangle"""
        if not args or len(args) == 0:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
        else:
            lin = len(args)
            if lin:
                self.id = args[0]
            if lin >= 2:
                self.width = args[1]
            if lin >= 3:
                self.height = args[2]
            if lin >= 4:
                self.x = args[3]
            if lin >= 5:
                self.y = args[4]

    def to_dictionary(self):
        """Returns dictionary representation of the object"""
        dic = {'id': self.id, 'width': self.width, 'height': self.height}
        dic.update({'x': self.x, 'y': self.y})
        return dic
