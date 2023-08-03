import os
import sys


def read_data(fi):
    n = int(fi.readline())
    m = int(fi.readline())
    matrix = []
    for i in range(0, n):
        matrix.append(list(map(int, fi.readline().rstrip().split(' '))))

    y = int(fi.readline())
    x = int(fi.readline())

    return n, m, matrix, x, y


def get_neighbors(n, m, matrix, x, y):
    neighbors = []
    if x > 0:
        neighbors.append(matrix[y][x - 1])
    if x < m - 1:
        neighbors.append(matrix[y][x + 1])
    if y > 0:
        neighbors.append(matrix[y - 1][x])
    if y < n - 1:
        neighbors.append(matrix[y + 1][x])
    neighbors.sort()
    return ' '.join(map(str, neighbors))


current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
fi = open(os.path.join(current_dir, "input.txt"), "r")
fo = open(os.path.join(current_dir, "output.txt"), "w")
neighbors = get_neighbors(*read_data(fi))
fo.write(neighbors)
fi.close()
fo.close()
