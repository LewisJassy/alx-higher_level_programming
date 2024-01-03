#!/usr/bin/python3
def add_integer(a, b=98):
    """
    This function adds two integers and returns their sum.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of a and b.
    """

    if type(a) is not int or type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int or type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return int(a + b)
