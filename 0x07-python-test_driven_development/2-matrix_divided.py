#!/usr/bin/python3
"""
This module defines a matrix division function
"""


def matrix_divided(matrix, div):
    """This function divides all elements of a matrix by a given number
    Args:
        matrix: A list of lists (matrix)- members can be of type ints or floats
        div: Number to be used for the division (can be a float or an integer)
    Raises:
        TypeError: If the matrix contains non-numbers
        TypeError: If the matrix contains rows of different sizes
        TypeError: If div is not an int or float
        ZeroDivisionError: If div is 0
    Returns:
        A new matrix which represents the result of the divisions
    """
    row_len = 0
    mtrx_type_e = "matrix must be a matrix (list of lists) of integers/floats"
    mtrx_len_e = "Each row of the matrix must have the same size"
    div_type_e = "div must be a number"
    div_zero_e = "division by zero"

    row_len = 0
    if type(matrix) is not list:
        raise TypeError(mtrx_type_e)

    for row in matrix:
        if type(row) is not list:
            raise TypeError(mtrx_type_e)
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError(mtrx_type_e)
        if len(row) is not row_len and row_len != 0:
            raise TypeError(mtrx_len_e)
        row_len = len(row)

    if type(div) not in [int, float]:
        raise TypeError(div_type_e)
    if div == 0:
        raise ZeroDivisionError(div_zero_e)

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
