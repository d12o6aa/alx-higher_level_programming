#!/usr/bin/python3


"""Module for Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """
    A representation of the Rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

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

    def area(self):
        return self.__width * self.__height

    def display(self):
        x = 0
        for x in range(self.__y):
            print()

        x = 0
        for x in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width, end="")
            print()

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y}" \
               f" - {self.width}/{self.height}"

    def __updata(self, id=None, width=None, height=None, x=None, y=None):
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):

        if args:
            self.__updata(*args)
        elif kwargs:
            self.__updata(**kwargs)

    def to_dictionary(self):
        """Returns dictionary representation of this class."""
        return {"id": self.id,
                "width": self.__width,
                "height": self.__height,
                "x": self.__x,
                "y": self.__y}
