#!/usr/bin/python3
"""This module inherits from the list class"""


class MyList(list):
    """A class that inherits from list class"""
    def print_sorted(self):
        """function that prints a sorted list"""
        print(sorted(self))
