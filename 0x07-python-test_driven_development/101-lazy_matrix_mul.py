#!/usr/bin/python3
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    This function multiplies two matrices.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not (all(isinstance(row, list) for row in m_a)):
        raise TypeError("m_a must be a list of lists")
    if not (all(isinstance(row, list) for row in m_b)):
        raise TypeError("m_b must be a list of lists")

    if not (m_a and all(m_a)):
        raise ValueError("m_a can't be empty")
    if not (m_b and all(m_b)):
        raise ValueError("m_b can't be empty")

    for matrix, matrix_name in [(m_a, 'm_a'), (m_b, 'm_b')]:
        for row in matrix:
            if not all(isinstance(elem, (int, float)) for elem in row):
                raise TypeError(f"{matrix_name} should contain only integers or floats")

    if len(set(len(row) for row in m_a)) > 1:
        raise TypeError("each row of m_a must be of the same size")
    if len(set(len(row) for row in m_b)) > 1:
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = np.dot(m_a, m_b)
    return result
