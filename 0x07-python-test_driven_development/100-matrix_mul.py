#!/usr/bin/python3
'''This module contains two functions:
    get_matrix_size and matrix_mul.
'''


def get_matrix_sizes(matrix_1, matrix_2, name_1, name_2):
    '''Computes the size of a matrix and performs some
        validation.
    Args:
        matrix (list): The matrix.
        name (str): The name of the matrix.
    Returns:
        list. The rows and columns of the given matrix.
    '''
    funcs = (
        lambda txt: '{} must be a list'.format(txt),
        lambda txt: '{} can\'t be empty'.format(txt),
        lambda txt: '{} must be a list of lists'.format(txt),
        lambda txt: '{} should contain only integers or floats'.format(txt),
        lambda txt: 'each row of {} must be of the same size'.format(txt),
        lambda l: all(map(lambda n: isinstance(n, (int, float)), l)),
    )
    size_0 = [0, 0]
    size_1 = [0, 0]
    if not isinstance(matrix_1, list):
        raise TypeError(funcs[0](name_1))
    if not isinstance(matrix_2, list):
        raise TypeError(funcs[0](name_2))
    size_0[0] = len(matrix_1)
    size_1[0] = len(matrix_2)
    if size_0[0] == 0:
        raise ValueError(funcs[1](name_1))
    if size_1[0] == 0:
        raise ValueError(funcs[1](name_2))
    if not all(map(lambda x: isinstance(x, list), matrix_1)):
        raise TypeError(funcs[2](name_1))
    if not all(map(lambda x: isinstance(x, list), matrix_2)):
        raise TypeError(funcs[2](name_2))
    if all(map(lambda x: len(x) == 0, matrix_1)):
        raise ValueError(funcs[1](name_1))
    if all(map(lambda x: len(x) == 0, matrix_2)):
        raise ValueError(funcs[1](name_2))
    if not all(map(lambda x: funcs[5](x), matrix_1)):
        raise TypeError(funcs[3](name_1))
    if not all(map(lambda x: funcs[5](x), matrix_2)):
        raise TypeError(funcs[3](name_2))
    size_0[1] = len(matrix_1[0])
    size_1[1] = len(matrix_2[0])
    if not all(map(lambda x: len(x) == size_0[1], matrix_1)):
        raise TypeError(funcs[4](name_1))
    if not all(map(lambda x: len(x) == size_1[1], matrix_2)):
        raise TypeError(funcs[4](name_2))
    return size_0, size_1


def matrix_mul(mtx_a, mtx_b):
    '''Multiplies 2 matrices.
    Args:
        mtx_a (list): First matrix.
        mtx_b (list): Second matrix.
    Returns:
        list: A list of lists of the products of the two given matrices.
    Raises:
        ValueError: If mtx_a's column count isn't equal to
        mtx_b's row count.
    '''
    size_a, size_b = get_matrix_sizes(mtx_a,
                                      mtx_b, 'mtx_a', 'mtx_b')
    # A x B only works if column_count in A == row_count in B
    if size_a[1] != size_b[0]:
        raise ValueError('mtx_a and mtx_b can\'t be multiplied')
    else:
        res = []
        for row_a in mtx_a:
            row_res = []
            for i in range(size_b[1]):
                cell_args = zip(range(size_a[1]), row_a)
                val = map(lambda x: x[1] * mtx_b[x[0]][i], cell_args)
                row_res.append(sum(list(val)))
            res.append(row_res)
        return res
