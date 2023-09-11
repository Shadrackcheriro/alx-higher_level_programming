#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for arr in matrix:
        for num in arr:
            if num != arr[0]:
                print(" ", end='')
            print("{:d}".format(num), end='')
        print()
