#!/usr/bin/python3
"""Module containing Square class"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Class to represent a square deriving from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.size
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.size = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.__x}/{self.__y} - {self.size}"