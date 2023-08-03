import os
import sys


def func(a, x, b, c):
    y = a * x * x + b * x + c
    return str(y)


current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
fi = open(os.path.join(current_dir, "input.txt"), "r")
fo = open(os.path.join(current_dir, "output.txt"), "w")
args = map(int, fi.readline().split(' '))
fo.write(func(*args))
fi.close()
fo.close()
