#!/usr/bin/python3
"""
This module contains a function that prints a square
"""


def print_square(size):
    """
    This function that prints a square with the character #
    Args:
        size(int): This represents the length of the square
    Raises:
        TypeError: if size is not an integer
        TypeError: if size is a float and less than zero
        ValueError: if size is less than zero
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    print(("#" * size + "\n") * size, end="")
