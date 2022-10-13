#!/usr/bin/python3
"""A square module containing a class that defines a square and it's size
checking if the given values are correct and a setter and getter methods
to set or get it. Some equivalence methods are present to help handle the use
of comparators. There's also an area methof that returns the area of the square
"""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Initializing the Square object.
        Args:
            size(int): the size of the square.
        """
        self.size = size

    def __eq__(self, other):
        """Sets the compare equality behaviour of the square object
        Args:
            other(Square): the Square object to compare with
        """
        if type(other) is Square:
            return self.area() == other.area()

    def __lt__(self, other):
        """Sets the compare less than behavior of the Square object
        Args:
            other(Square): the Square object to compare with
        """
        if type(other) is Square:
            return self.area() < other.area()

    def __le__(self, other):
        """Sets the compare less equal than behaviour of the square object
        Args:
            other(Square): the Square object to compare with
        """
        if type(other) is Square:
            return self.area() <= other.area()

    @property
    def size(self):
        """Get or Set the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Returns the current square area."""

        return self.__size ** 2
