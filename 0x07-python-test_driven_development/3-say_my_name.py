#!/usr/bin/python3

"""
    This function takes in two strings as input and returns a tuple of two strings.
    If the last_name parameter is not provided, it is initialized to an empty string.
    If the first_name parameter is an empty string and the last_name parameter is also an empty string,
    then the function raises a ValueError.
    Otherwise, the function returns a tuple of the two strings.

    Args:
        first_name (str): The first name of the person.
        last_name (str, optional): The last name of the person. Defaults to "".

    Raises:
        TypeError: If the input type is not a string.
        ValueError: If the first_name parameter is an empty string and the last_name parameter is also an empty string.

    Returns:
        tuple: A tuple of two strings, which are the first and last names, respectively.
    """
def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if first_name == "" and last_name == "":
        raise ValueError("String is empty")
    return first_name, last_name