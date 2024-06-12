# 0x07. Rotate 2D Matrix

## Overview
This project focuses on implementing an in-place algorithm to rotate an n x n 2D matrix by 90 degrees clockwise. The task requires proficiency in matrix manipulation and understanding of in-place operations using Python.

## Project Details
- **Start Date:** June 10, 2024, 6:00 AM
- **End Date:** June 14, 2024, 6:00 AM
- **Checker Release Date:** June 11, 2024, 6:00 AM
- **Auto Review:** At the deadline

## Objective
The main objective of this project is to rotate a given n x n 2D matrix 90 degrees clockwise in place. This involves:
1. Transposing the matrix.
2. Reversing each row of the transposed matrix.

## Key Concepts

### Matrix Representation in Python
- **Lists of Lists:** Understanding how to represent 2D matrices using lists of lists.
- **Access and Modification:** Learning how to access and modify elements in a 2D matrix.

### In-place Operations
- **Efficiency:** Performing operations directly on the data structure without creating copies.
- **Space Complexity:** Minimizing space complexity by editing the matrix in place.

### Matrix Transposition
- **Swapping Rows and Columns:** Understanding and implementing the transposition of a matrix.
- **Intermediate Step:** Transposition as a critical step in rotating the matrix.

### Reversing Rows in a Matrix
- **Row Manipulation:** Reversing the order of elements in each row as part of the rotation.

### Nested Loops
- **Iteration:** Using nested loops to iterate through 2D data structures.
- **Element Modification:** Modifying elements within nested loops to achieve the desired matrix transformation.

## Resources
### Python Official Documentation
- [Data Structures](https://docs.python.org/3/tutorial/datastructures.html): List comprehensions and nested list comprehension.
- [More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

### GeeksforGeeks Articles
- [Inplace rotate square matrix by 90 degrees](https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/)
- [Transpose a matrix in Single line in Python](https://www.geeksforgeeks.org/transpose-matrix-single-line-python/)

### TutorialsPoint
- [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm): Basics of list manipulation in Python.

## Requirements
- **Editors:** vi, vim, emacs
- **Environment:** Ubuntu 20.04 LTS, Python 3.8.10
- **File Requirements:**
  - End with a new line
  - First line: `#!/usr/bin/python3`
  - Use `pycodestyle` style (version 2.8.0)
  - No module imports allowed
  - All modules and functions must be documented
  - Files must be executable

## Task
### Rotate 2D Matrix
- **Description:** Rotate an n x n 2D matrix 90 degrees clockwise.
- **Prototype:** `def rotate_2d_matrix(matrix):`
- **Constraints:**
  - Do not return anything. The matrix must be edited in-place.
  - The matrix will always have 2 dimensions and will not be empty.

### Example
```python
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
```

Expected output:
```python
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

## Repository
- **GitHub Repository:** `alx-interview`
- **Directory:** `0x07-rotate_2d_matrix`
- **File:** `0-rotate_2d_matrix.py`

By mastering the above concepts and utilizing the provided resources, one can implement an efficient in-place rotation algorithm, enhancing problem-solving and algorithmic thinking skills in Python.
sebsibe solomon
