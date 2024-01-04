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
        self.__width = 0
        self.__height = 0

        self.width = width
        self.height = height


    @property
    def width(self):
        """getter for width propety"""
        return self.__width
    
    
    @width.setter
    def width(self, value):
        """ setter for width property """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value


    @property
    def height(self):
        """getter for height propety"""
        return self.__height
    
    
    @height.setter
    def height(self, value):
        """ setter for height property """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Return the area of the rectangle.
        """
        return self.width * self.height
    
    def perimeter(self):
        """
        Return the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)