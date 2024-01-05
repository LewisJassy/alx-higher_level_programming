#!/usr/bin/python3


def print_square(size):
    """Print a square of size size"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float):
        raise ValueError("size must be an integer")
    for _ in range(size):
        print("#" * size)
