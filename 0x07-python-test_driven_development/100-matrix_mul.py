#!/usr/bin/python3

def matrix_mul(m_a, m_b):
    # Check if m_a and m_b are lists
    if not (isinstance(m_a, list) and isinstance(m_b, list)):
        raise TypeError("m_a must be a list or m_b must be a list")

    # Check if m_a and m_b are non-empty lists of lists
    if not (all(isinstance(row, list) for row in m_a) and all(isinstance(row, list) for row in m_b)):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")

    if not (m_a and all(m_a) and m_b and all(m_b)):
        raise ValueError("m_a can't be empty or m_b can't be empty")

    # Check if elements are integers or floats
    for matrix, matrix_name in [(m_a, 'm_a'), (m_b, 'm_b')]:
        for row in matrix:
            if not all(isinstance(elem, (int, float)) for elem in row):
                raise TypeError(f"{matrix_name} should contain only integers or floats")

    # Check if matrices are rectangles
    if len(set(len(row) for row in m_a)) > 1:
        raise TypeError("each row of m_a must be of the same size")

    if len(set(len(row) for row in m_b)) > 1:
        raise TypeError("each row of m_b must be of the same size")

    # Check if matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]

    return result
