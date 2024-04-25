#!/usr/bin/python3
'''Module for working with Pascal's triangle.

This module provides functionality to generate Pascal's
triangle up to a given integer.
'''


def pascal_triangle(n):
    '''Creates a list of lists representing Pascal's triangle.

    Args:
        n (int): The number of rows to generate in the Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.

    Raises:
        TypeError: If the input `n` is not an integer.
        ValueError: If the input `n` is less than or equal to 0.
    '''
    triangle = []

    try:
        if type(n) is not int or n <= 0:
            raise ValueError("Input must be a positive integer.")

        for i in range(n):
            line = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    line.append(1)
                elif i > 0 and j > 0:
                    line.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            triangle.append(line)

    except (TypeError, ValueError) as e:
        # Print error message or handle the exception as needed
        print(f"Error: {str(e)}")
        return triangle

    return triangle
