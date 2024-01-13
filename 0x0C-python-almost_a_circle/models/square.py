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
        """Getter method for the size attribute"""
        return self.width
    
    @size.setter
    def size(self, value):
        """Setter method for the size attribute."""
        setattr(self, "width", value)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"