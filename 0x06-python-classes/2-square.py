#!/usr/bin/python3
"""Creating a class Square that defines a square"""


class Square:
    """Defining a square"""

    def __init__(self, size=0):
        """Initializing the square object
        Args:
            size(int): the size of the square defined
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than zero(0)
        """
        if type(size) is int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

