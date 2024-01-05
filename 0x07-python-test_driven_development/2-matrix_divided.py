#!/usr/bin/python3
"""
    This function takes in a matrix and a divisor and returns 
    a new matrix where each element of the original matrix is
    divided by the divisor.

    Parameters:
    matrix (list): a matrix of integers or floats
    div (float): the divisor to be used for division

    Returns:
    list: a new matrix where each element is the result of the 
    division of the corresponding element in the original matrix 
    and the divisor
"""


def matrix_divided(matrix, div):
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0 and div == 0.0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("Each element of the matrix must be an integer or float")

    # Perform matrix division
    result_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return result_matrix
