#!/usr/bin/python3
"""
Multiplication 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    function that multiplies 2 matrices
    """
    filas_a = len(m_a)
    col_a = len(m_a[0])
    filas_b = len(m_b)
    col_b = len(m_b[0])

    return(mulMatrices(m_a, m_b))
