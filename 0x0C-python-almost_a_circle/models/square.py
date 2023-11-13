#!/usr/bin/python3
from models.rectangle import Rectangle

"""Defines a Square Class"""


class Square(Rectangle):
    """A class to create square objects from"""
    def __init__(self, size, x=0, y=0, id=None):
        """
               Initiates an instance
               Args:
                   size: size of the square
                   x: position on x-axis
                   y: position on y-axis
                   id: id of the Rectangle object
               """
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        """Returns string representation of object"""
        return f"[Square] \
({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Updates the attributes of a rectangle"""
        if not args or len(args) == 0:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
        else:
            lin = len(args)
            if lin:
                self.id = args[0]
            if lin >= 2:
                self.size = args[1]
            if lin >= 3:
                self.x = args[2]
            if lin >= 4:
                self.y = args[3]

    def to_dictionary(self):
        """Returns dictionary representation of the object"""
        dic = {'id': self.id, 'size': self.size}
        dic.update({'x': self.x, 'y': self.y})
        return dic
