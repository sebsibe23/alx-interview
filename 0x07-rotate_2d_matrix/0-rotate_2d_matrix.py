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
    try:
        n = len(matrix)

    # Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row
        for i in range(n):
            matrix[i] = matrix[i][::-1]
    except Exception as ex:
        print(ex)
