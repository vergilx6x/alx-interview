#!/usr/bin/python3
"""2D matrix rotation module.
"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix in place."""
    if not (isinstance(matrix, list) and
            matrix and
            all(isinstance(row, list) for row in matrix)):
        return

    rows, cols = len(matrix), len(matrix[0])
    if not all(len(row) == cols for row in matrix):
        return

    rotated = []
    for c in range(cols):
        rotated.append([matrix[r][c] for r in range(rows - 1, -1, -1)])

    matrix.clear()
    matrix.extend(rotated)
