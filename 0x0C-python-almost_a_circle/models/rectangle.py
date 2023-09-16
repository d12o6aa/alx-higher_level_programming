#!/usr/bin/python3


"""Module for Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """
    A representation of the Rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id=None)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width of this rectangle."""
        return self.__width

    @width.setter
    def width(self, v):
        self.validation("width", v)
        self.__width = v

    @property
    def height(self):
        """Height of this rectangle."""
        return self.__height

    @height.setter
    def height(self, v):
        self.validation("height", v)
        self.__height = v

    @property
    def x(self):
        """x of this rectangle."""
        return self.__x

    @x.setter
    def x(self, v):
        self.validation("x", v)
        self.__x = v

    @property
    def y(self):
        """Y of this rectangle."""
        return self.__y

    @y.setter
    def y(self, v):
        self.validation("y", v)
        self.__y = v

    def validation(self, name, v):

        if type(v) is not int:
            raise TypeError(f"{name} must be an integer")
        if v <= 0 and (name == "height" or name == "width"):
            raise ValueError(f"{name} must be > 0")
        if (name == "y" or name == "x") and v < 0:
            raise ValueError(f"{name} must be >= 0")
