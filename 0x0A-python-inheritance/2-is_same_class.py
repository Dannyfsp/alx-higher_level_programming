#!/usr/bin/python3
"""
This module checks if object is an instance of a class
"""


def is_same_class(obj, a_class):
    """checks if an object is exactly an instance of a given class.
    Args:
        obj(any): The object to check
        a_class(type): The class to match the type of obj to
    Returns: True - if obj is exactly an instance of a_class
             Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    else:
        return False
