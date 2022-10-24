#!/usr/bin/python3
"""
This module defines a base geometry class BaseGeometry
"""


class BaseGeometry:
    """Represents base geometry"""

    def area(self):
        """method not yet implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate a parameter as an integer
        Args:
            name(str): The name of the parameter
            value(int): The parameter to validate
        Raises:
            TypeError: If value is not an integer
            ValueError: if value is less than or equals 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
