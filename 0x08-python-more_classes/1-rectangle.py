#!/usr/bin/python3
"""Module containing Rectangle class"""


class Rectangle:
    """
    Initialize a new Rectangle object with the specified width and height.

    Parameters:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.

    Raises:
    ValueError: If either width or height is negative.
    TypeError: If width or height are not integers.
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def width(self):
        return self.__width
    
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def height(self):
        return self.__height
    
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
