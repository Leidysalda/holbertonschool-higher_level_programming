#!/usr/bin/python3
"""
Use module Numpy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    function that multiplies 2 matrices by using the module NumPy
    """
    A = np.asarray(m_a)
    B = np.asarray(m_b)

    if A.shape[-1] != B.shape[0]:
        raise TypeError('Error')
        return None

    if res and res.shape == (A.shape[0], B.shape[-1]):
        np.copyto(res, np.matmul(A, B))
        return res

    return np.matmil(A, B)
