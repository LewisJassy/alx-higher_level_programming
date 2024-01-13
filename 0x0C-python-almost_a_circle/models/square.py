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
        """Return a string representation of the Square instance."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
    
    def update(self, *args, **kwargs):
        if len(args) > 0:
            self.id = args[0] if len(args) > 0 else self.id
            self.size = args[1] if len(args) > 1 else self.size
            self.x = args[2] if len(args) > 2 else self.x
            self.y = args[3] if len(args) > 3 else self.y
        else:
            self.id = kwargs.get("id", self.id)
            self.size = kwargs.get("width", self.size)
            self.x = kwargs.get("x", self.x)
            self.y = kwargs.get("y", self.y)