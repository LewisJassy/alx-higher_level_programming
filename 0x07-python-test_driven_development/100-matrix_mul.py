#!/usr/bin/python3

def matrix_mul(m_a, m_b):
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if len(m_a)!= len(m_b):
        raise ValueError("m_a and m_b must have the same number of rows")
    if len(m_a[0])!= len(m_b):
        raise ValueError("m_a and m_b must have the same number of columns")
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            sum = 0
            for k in range(len(m_b)):
                sum += m_a[i][k] * m_b[k][j]
            m_a[i][j] = sum
    return m_a
