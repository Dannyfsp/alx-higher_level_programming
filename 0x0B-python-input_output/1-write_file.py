#!/usr/bin/python3
"""This module defines a write_file method"""


def write_file(filename="", text=""):
    """Writes a string to a UTF8 text file"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
