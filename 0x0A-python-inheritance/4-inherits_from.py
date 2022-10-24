#!/usr/bin/python3
"""
This module checks if object is an instance of a class that inherited
(directly or indirectly) from a specified class
"""


def inherits_from(obj, a_class):
    """
    checks if an object is an inherited instance of a class
    Args:
        obj(any): The object to check
        a_class(type): The class to match the type of obj to
    Returns: True - if obj an inherited instance of a_class
             Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
