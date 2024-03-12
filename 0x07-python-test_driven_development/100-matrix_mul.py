#!/usr/bin/python3

"""Defines a matrix multiplication function."""


def matrix_mul(mtx_a, mtx_b):
    """Multiply two matrices.

    Args:
        mtx_a (list of lists of ints/floats): The first matrix.
        mtx_b (list of lists of ints/floats): The second matrix.
    Raises:
        TypeError: If either mtx_a or mtx_b is not a list of lists of ints/floats.
        TypeError: If either mtx_a or mtx_b is empty.
        TypeError: If either mtx_a or mtx_b has different-sized rows.
        ValueError: If mtx_a and mtx_b cannot be multiplied.
    Returns:
        A new matrix representing the multiplication of mtx_a by mtx_b.
    """

    if mtx_a == [] or mtx_a == [[]]:
        raise ValueError("mtx_a can't be empty")
    if mtx_b == [] or mtx_b == [[]]:
        raise ValueError("mtx_b can't be empty")

    if not isinstance(mtx_a, list):
        raise TypeError("mtx_a must be a list")
    if not isinstance(mtx_b, list):
        raise TypeError("mtx_b must be a list")

    if not all(isinstance(row, list) for row in mtx_a):
        raise TypeError("mtx_a must be a list of lists")
    if not all(isinstance(row, list) for row in mtx_b):
        raise TypeError("mtx_b must be a list of lists")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in mtx_a for num in row]):
        raise TypeError("mtx_a should contain only integers or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in mtx_b for num in row]):
        raise TypeError("mtx_b should contain only integers or floats")

    if not all(len(row) == len(mtx_a[0]) for row in mtx_a):
        raise TypeError("each row of mtx_a must should be of the same size")
    if not all(len(row) == len(mtx_b[0]) for row in mtx_b):
        raise TypeError("each row of mtx_b must should be of the same size")

    if len(mtx_a[0]) != len(mtx_b):
        raise ValueError("mtx_a and mtx_b can't be multiplied")

    inverted_b = []
    for r in range(len(mtx_b[0])):
        new_row = []
        for c in range(len(mtx_b)):
            new_row.append(mtx_b[c][r])
        inverted_b.append(new_row)

    new_matrix = []
    for row in mtx_a:
        new_row = []
        for col in inverted_b:
            prod = 0
            for i in range(len(inverted_b[0])):
                prod += row[i] * col[i]
            new_row.append(prod)
        new_matrix.append(new_row)

    return new_matrix
