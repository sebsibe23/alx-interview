# N Queens Problem

## Description

The N Queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. This project involves writing a Python program to solve the N Queens problem using a backtracking algorithm. The program outputs all possible solutions, where each solution is a unique configuration of the chessboard with N queens.

## Concepts Covered

- **Backtracking Algorithms**: Understanding how backtracking algorithms work to explore all potential solutions to a problem and backtrack when a solution cannot be completed.
- **Recursion**: Using recursive functions to implement backtracking algorithms.
- **List Manipulations in Python**: Creating and manipulating lists to store the positions of queens on the board.
- **Python Command Line Arguments**: Handling command-line arguments with the `sys` module.

## Requirements

- **Editors**: `vi`, `vim`, `emacs`
- **Execution Environment**: The code will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3)
- **Code Style**: PEP 8 (version 1.7.*)
- **Execution Permissions**: All files must be executable

## Usage

To run the program, use the following command:

```sh
./0-nqueens.py N
```

Where `N` is an integer representing the size of the chessboard and the number of queens to place. The value of `N` must be greater than or equal to 4.

### Example

```sh
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```

## Error Handling

The program handles several types of errors:

- If the user provides the wrong number of arguments:
  ```sh
  $ ./0-nqueens.py
  Usage: nqueens N
  ```

- If `N` is not an integer:
  ```sh
  $ ./0-nqueens.py not_a_number
  N must be a number
  ```

- If `N` is smaller than 4:
  ```sh
  $ ./0-nqueens.py 3
  N must be at least 4
  ```

## Implementation

The main script is `0-nqueens.py`, and it includes:

- **Input Validation**: Ensures the correct number of arguments, that `N` is an integer, and that `N` is at least 4.
- **Backtracking Algorithm**: Uses recursion to explore all valid configurations of queens on the board.
- **Solution Output**: Prints each solution in the specified format.

## Repository

- **GitHub Repository**: [alx-interview](https://github.com/alx-interview)
- **Directory**: `0x05-nqueens`
- **File**: `0-nqueens.py`

## Author

sebsibe solomon https://github.com/sebsibe23

```

### Steps to Run the Code

1. Ensure the script has execute permissions:
   ```sh
   chmod +x 0-nqueens.py
   ```

2. Execute the script with the desired board size:
   ```sh
   ./0-nqueens.py 4
   ```
