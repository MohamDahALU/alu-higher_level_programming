#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            print("{}".format(col), end=" ")
        print("")


print_matrix_integer([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
