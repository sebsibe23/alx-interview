#!/usr/bin/python3
"""Island perimeter computing module.
This module contains a function to compute
the perimeter of an island represented in
a grid, where 1 indicates land and 0
indicates water.
"""


def island_perimeter(grid):
    """Computes the perimeter of an island with no lakes.
    The function iterates through the grid
    and checks each cell. If the cell is
    land (1), it checks the neighboring
    cells. The perimeter is increased
    based on the presence of water or grid
    edges.

    Args:
        grid (list of list of int): A binary
        grid where 1 represents land and 0
        represents water.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    try:
        if not isinstance(grid, list):
            return 0
        n = len(grid)
        for i, row in enumerate(grid):
            m = len(row)
            for j, cell in enumerate(row):
                if cell == 0:
                    continue
                # Determine if each side of the cell is water or grid edge
                top_edge = (i == 0 or (len(grid[i - 1]) > j and
                                       grid[i - 1][j] == 0))
                right_edge = (j == m - 1 or (m > j + 1 and
                                             row[j + 1] == 0))
                bottom_edge = (i == n - 1 or (len(grid[i + 1]) > j and
                                              grid[i + 1][j] == 0))
                left_edge = (j == 0 or row[j - 1] == 0)

                edges = (top_edge, right_edge, bottom_edge, left_edge)
                # Add to perimeter for each water or edge adjacent to the cell
                perimeter += sum(edges)
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
    return perimeter
