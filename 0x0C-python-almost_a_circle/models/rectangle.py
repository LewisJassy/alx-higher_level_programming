#!/usr/bin/python3
"""Module containing Square class"""
from models.base import Base
class Rectangle(Base):
    """Class to represent a rectangle deriving from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize new square with width, height, and offsets.

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int): width offset for drawing rectangle
            y (int): height offset for drawing rectangle
            id: identifier for instance. If None, then object count

        Raise:
            TypeError: If `width`, `height`, `x`, or `y` are not ints.
            ValueError: If `width` or `height` are <= 0, or `x` or `y`
                are < 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get the value for width"""
        return self.__width
    @width.setter
    def width(self, value):
        """set the value for width with type and value validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be an > 0")
        self.__width = value
        
    @property
    def height(self):
        """get the value for height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """set the value for height with type and value validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be an > 0")
        self.__height = value
    
    @property
    def x(self):
        """Get the value of x"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """set the value of x with type and value validation"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
    @property
    def y(self):
        """get the value of y"""
        return self.__y
    
    @y.setter
    def y(self, value):
        """set the value of y with type and value validation"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle"""
        result = self.__height * self.__width 
        return result
    
    def display(self):
        """Display the Rectangle instance by printing it to stdout using '#'."""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + '#' * self.__width)

    def __str__(self):
        """function that returns values of rectangle in string format"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
    # checks if there is positional argument, if there is no it falls back to update the attributes 
    def update(self, *args, **kwargs):
        """Update Rectangle instances with *args and **kwargs.
        Order of *args is 'id', 'size', 'x', 'y'. **kwargs can be in
        any order.

        Example:
            >>> r = Rectangle(2, 2)
            >>> args = [6]; kwargs = {"height": 4, "y": 3}
            >>> r.update(*args, **kwargs)
            >>> print(r)
            [Rectangle] (6) 0/3 - 6/4
        """
        if len(args) > 0:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i, attr in enumerate(attrs):
                if i < len(args):
                    setattr(self, attr, args[i])
                else:
                    setattr(self, attr, kwargs.get(attr, getattr(self, attr)))
        else:
            for attr, value in kwargs.items():
                if attr != 'id':
                    setattr(self, attr, value)
    def to_dictionary(self):
        """Return dictionary representation of writable attributes."""
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width
        }
