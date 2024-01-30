#!/usr/bin/python3
"""matrix multiplication function using NumPy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices

    Args:
        m_a (lists of ints/floats): The first matrix
        m_b (lists of ints/floats): The second matrix
    """

    return (np.matmul(m_a, m_b))
