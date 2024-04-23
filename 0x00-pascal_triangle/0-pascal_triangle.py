#!/usr/bin/python3
"""
The Pascal's triangle as a list of lists
"""
def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal's triangle of n.

    Args:
        n (int): The number of rows in the Pascal's triangle.

    Returns:
        list: The Pascal's triangle as a list of lists.

    Raises:
        ValueError: If n is less than or equal to 0.

    """
    try:
        # Check for invalid input
        if n <= 0:
            raise ValueError("n should be greater than 0.")

        # Initialize the Pascal's triangle
        triangle = [[1]]

        # Generate the remaining rows of the triangle
        for i in range(1, n):
            row = [1]  # The first element of each row is always 1
            for j in range(1, i):
                # Calculate the element by summing the two elements above it
                element = triangle[i - 1][j - 1] + triangle[i - 1][j]
                row.append(element)
            row.append(1)  # The last element of each row is always 1
            triangle.append(row)

        return triangle
    except ValueError as e:
        print("Error:", str(e))
