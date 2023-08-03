import os
import sys


def read_data(fi):
    number = int(fi.readline())
    return number


def two_stepen(stepen):
    result = 1
    if stepen == 0:
        return result
    for i in range(0, stepen):
        result *= 2
    return result


def bin_matrix(number):
    matrix = []
    index = 0
    while number >= 0:
        calc = two_stepen(index)
        matrix.append(calc)
        number -= calc
        index += 1
    return matrix


def to_binary(number, matrix):
    binary = ''
    index = len(matrix) - 1
    while index >= 0:
        if matrix[index] <= number:
            binary += '1'
            number -= matrix[index]
        else:
            binary += '0'
        index -= 1
    return binary


current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
fi = open(os.path.join(current_dir, "input.txt"), "r")
fo = open(os.path.join(current_dir, "output.txt"), "w")
number = read_data(fi)
output = to_binary(number, bin_matrix(number))
fo.writelines(output)
fi.close()
fo.close()
