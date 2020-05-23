#!/usr/bin/python3
"""
Multiplication 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    function that multiplies 2 matrices
    """
    if type(m_a) is not list:
        raise TypeError('m_a must be a list')
    elif type(m_b) is not list:
        raise TypeError('m_b must be a list')
    elif type(m_a) is None:
        raise ValueError('m_a can\'t be empty')
    elif type(m_b) is None:
        raise ValueError('m_b can\'t be empty')

    m_c = [[0 for row in range(len(m_a))] for col in range(len(m_b[0]))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                m_c[i][j] += m_a[i][k] * m_b[k][j]
    return(m_c)
