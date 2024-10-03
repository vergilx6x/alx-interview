import math


def pascal_triangle(n):
    list_of_rows = []

    if n <= 0:
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
