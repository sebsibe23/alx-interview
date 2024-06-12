#!/usr/bin/python3
"""
2D matrix rotation module.

This module provides a function to rotate
an m byn 2D matrix in place by 90
degrees clockwise.

Function:
    rotate_2d_matrix(matrix): Rotates the given
    2D matrix in place.

Parameters:
    matrix (list of list of int): The 2D matrix
    to be rotated. Each inner list
    represents a row in the matrix.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates an m by n 2D matrix in place.

    Args:
        matrix (list of list of int): The 2D matrix
        to be rotated. Each inner
        list represents a row in the matrix.

    Returns:
        None

    This function modifies the input matrix in
    place by rotating it 90 degrees
    clockwise.
    """
    if type(matrix) != list:
        return
    if len(matrix) <= 0:
        return
    if not all(map(lambda x: type(x) == list, matrix)):
        return
    rows = len(matrix)
    cols = len(matrix[0])
    if not all(map(lambda x: len(x) == cols, matrix)):
        return
    c, r = 0, rows - 1
    for i in range(cols * rows):
        if i % rows == 0:
            matrix.append([])
        if r == -1:
            r = rows - 1
            c += 1
        matrix[-1].append(matrix[r][c])
        if c == cols - 1 and r >= -1:
            matrix.pop(r)
        r -= 1
