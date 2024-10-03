#!/usr/bin/python3
import math

''' A module for working with Pascal's triangle. '''


def pascal_triangle(n):
    '''Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.'''

    list_of_rows = []

    if type(n) is not int or n <= 0:
        return []

    for row in range(n):
        columns = []
        for col in range(row + 1):

            if col == 0 or col == row:
                columns.append(1)
            else:
                columns.append((int(math.comb(row, col))))

        list_of_rows.append(columns)

    return list_of_rows
