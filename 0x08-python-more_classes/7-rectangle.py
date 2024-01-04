#!/usr/bin/python3
"""Module containing Rectangle class"""


class Rectangle:
    """Class to create a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle with `width` and `height`.

        Args:
            width (int): width of rectangle with value >= 0.
            height (int): height of rectangle with value >= 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """Getter function for `height` attribute.

        Returns: value of `height` attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter function for `height` attribute.

        Args:
            value (int): value to use for `height`.

        Raises:
            TypeError: If `value` is not of type int.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        """Getter function for `width` attribute.

        Returns: value of `width` attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter function for `width` attribute.

        Args:
            value (int): value to use for `width`.

        Raises:
            TypeError: If `value` is not of type int.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    def area(self):
        """Method to compute area of Rectangle instance"""
        return self.width * self.height

    def perimeter(self):
        """Method to compute perimeter length of Rectangle instance.

        Returns: 2 * (w + h) if both `width` and `height` > 0, else 0.
        """
        return 2*(self.width + self.height) * bool(self.width and self.height)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        else:
            result = ""
            for _ in range(self.height):
                result += str(self.print_symbol) * self.width + "\n"
            return result[:-1]

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
