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

    if a != int:
        return("a must be an integer")
    if b!= int:
        return("b must be an integer")
    
    return int(a + b)
