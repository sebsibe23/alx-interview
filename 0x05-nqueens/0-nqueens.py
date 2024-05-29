#!/usr/bin/python3
"""
N queens solution finder module.

This module provides a solution to the N queens problem,
which involves placing N queens on an N×N chessboard
such that no two queens can attack each other.

Functions:
    get_input() -> int
        Retrieves and validates the program's argument.

    is_attacking(pos0, pos1) -> bool
        Checks if two queens are in attacking positions.

    group_exists(group) -> bool
        Checks if a group exists in the list of solutions.

    build_solution(row, group)
        Builds a solution for the N queens problem.

    get_solutions()
        Gets the solutions for the given chessboard size.
"""

import sys

solutions = []
"""List of possible solutions to the N queens problem."""

n = 0
"""Size of the chessboard."""

pos = None
"""List of possible positions on the chessboard."""


def get_input():
    """
    Retrieves and validates the program's argument.

    Returns:
        int: The size of the chessboard.

    Raises:
        SystemExit: If the argument is invalid.
    """
    global n
    n = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_attacking(pos0, pos1):
    """
    Checks if the positions of two queens are in an attacking mode.

    Args:
        pos0 (list or tuple): The first queen's position.
        pos1 (list or tuple): The second queen's position.

    Returns:
        bool: True if the queens are in an attacking position, else False.
    """
    if pos0[0] == pos1[0] or pos0[1] == pos1[1]:
        return True
    return abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])


def group_exists(group):
    """
    Checks if a group exists in the list of solutions.

    Args:
        group (list of list of int): A group of possible positions.

    Returns:
        bool: True if it exists, otherwise False.
    """
    global solutions
    for stn in solutions:
        i = 0
        for stn_pos in stn:
            for grp_pos in group:
                if stn_pos == grp_pos:
                    i += 1
        if i == n:
            return True
    return False


def build_solution(row, group):
    """
    Builds a solution for the N queens problem.

    Args:
        row (int): The current row in the chessboard.
        group (list of list of int): The group of valid positions.
    """
    global solutions
    global n
    if row == n:
        tmp0 = group.copy()
        if not group_exists(tmp0):
            solutions.append(tmp0)
    else:
        for col in range(n):
            a = (row * n) + col
            matches = zip([pos[a]] * len(group), group)
            used_positions = map(lambda x: is_attacking(x[0], x[1]), matches)
            group.append(pos[a].copy())
            if not any(used_positions):
                build_solution(row + 1, group)
            group.pop()


def get_solutions():
    """
    Gets the solutions for the given chessboard size.
    """
    global pos, n
    pos = list(map(lambda x: [x // n, x % n], range(n ** 2)))
    build_solution(0, [])


if __name__ == "__main__":
    n = get_input()
    get_solutions()
    for solution in solutions:
        print(solution)
