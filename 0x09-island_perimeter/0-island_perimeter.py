#!/usr/bin/python3
"""Island perimeter computing.
"""


def island_perimeter(grid):
    """Computes the perimeter of an island with no lakes."""
    if not isinstance(grid, list):
        return 0

    perimeter = 0
    rows = len(grid)

    for i, row in enumerate(grid):
        cols = len(row)
        for j, cell in enumerate(row):
            if cell == 1:
                # Check all four edges directly
                perimeter += (
                    (i == 0 or grid[i - 1][j] == 0) +  # Top edge
                    (j == cols - 1 or grid[i][j + 1] == 0) +  # Right edge
                    (i == rows - 1 or grid[i + 1][j] == 0) +  # Bottom edge
                    (j == 0 or grid[i][j - 1] == 0)  # Left edge
                )
    return perimeter
