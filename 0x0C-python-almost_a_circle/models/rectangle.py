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
        """Update attributes of the Rectangle instance with positional arguments."""
        if len(args) > 0:
            self.id = args[0] if len(args) > 0 else self.id
            self.width = args[1] if len(args) > 1 else self.width
            self.height = args[2] if len(args) > 2 else self.height
            self.x = args[3] if len(args) > 3 else self.x
            self.y = args[4] if len(args) > 4 else self.y
        
        else:
            self.id = kwargs.get("id", self.id)
            self.width = kwargs.get("width", self.width)
            self.height = kwargs.get("height", self.height)
            self.x = kwargs.get("x", self.x)
            self.y = kwargs.get("y", self.y)

    def to_dictionary(self):
        attrs = ["id", "size", "x", "y"]
        return {k: getattr(self, k) for k in attrs}
