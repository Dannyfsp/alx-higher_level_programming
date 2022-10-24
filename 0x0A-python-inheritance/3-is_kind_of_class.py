#!/usr/bin/python3
"""
This module checks if object is an instance of a class
or an inherited class
"""


def is_kind_of_class(obj, a_class):
    """
    checks if an object is an instance or inherited instance of a class
    Args:
        obj(any): The object to check
        a_class(type): The class to match the type of obj to
    Returns: True - if obj an instance or inherited instance of a_class
             Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
