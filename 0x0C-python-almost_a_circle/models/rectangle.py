#!/usr/bin/python3

from models.base import Base
class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
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
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + '#' * self.__width)
        """Display the Rectangle instance by printing it to stdout using '#'."""
