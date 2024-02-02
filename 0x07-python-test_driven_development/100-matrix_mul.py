#!/usr/bin/python3
"""implementation  matrix multiplication"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
        m_a (list): First matrix
        m_b (list): Second matrix

    Returns:
        list: Result matrix multiplication

    Raises:
        TypeError: If input matrices are not valid
        ValueError: If matrices can't be multiplied
    """

    # Check if m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    # check if m_a and m_b are not empty
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    # Check if m_a is a list of lists and contains only integers or floats
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        if len(row) == 0:
            raise ValueError("m_a can't be empty")
        for val in row:
            if not isinstance(val, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    # Check if m_b is a list of lists and contains only integers or floats
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        if len(row) == 0:
            raise ValueError("m_b can't be empty")
        for val in row:
            if not isinstance(val, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    # Check if m_a and m_b are not empty
    # if not (m_a and m_a[0]) or not (m_b and m_b[0]):
    #     raise ValueError("m_a and m_b can't be empty")

    # Check if all rows of m_a have the same size
    row_size_a = len(m_a[0])
    if any(len(row) != row_size_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    # Check if all rows of m_b have the same size
    row_size_b = len(m_b[0])
    for i in range(len(m_b)):
        if (len(m_b[i]) != row_size_b):
            raise TypeError("each row of m_b must be of the same size")

    # Check if the matrices can be multiplied (columns of m_a == rows of m_b)
    if row_size_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            element = 0
            for k in range(len(m_b)):
                element += m_a[i][k] * m_b[k][j]
            row.append(element)
        result.append(row)

    return (result)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
