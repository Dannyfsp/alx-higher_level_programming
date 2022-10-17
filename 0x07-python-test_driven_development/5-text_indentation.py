#!/usr/bin/python3
"""
text_indentation module
This module contains a function that indents texts
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    Args:
        text(str): The string to be printed
    Raises:
        TypeError: if text is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    line = ""
    for c in range(len(text)):
        line += text[c]
        if text[c] in ".?:":
            print((line + "\n").lstrip(" "))
            line = ""
    print(line.lstrip(" "), end="")
