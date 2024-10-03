#!/usr/bin/python3
''' A module for working with Pascal's triangle. '''


def pascal_triangle(n):
    '''Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.'''

    triangle = []

    if type(n) is not int or n <= 0:
        return []

    for row in range(n):
        columns = []
        for col in range(row + 1):

            if col == 0 or col == row:
                columns.append(1)
            elif row > 0 and col > 0:
                value = triangle[row - 1][col - 1] + triangle[row - 1][col]
                columns.append(value)

        triangle.append(columns)

    return triangle
