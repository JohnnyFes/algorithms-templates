import os
import sys


def func(*args):
    odd = even = 0
    for num in args:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    return 'WIN' if abs(odd - even) == 3 else 'FAIL'


current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
fi = open(os.path.join(current_dir, "input.txt"), "r")
fo = open(os.path.join(current_dir, "output.txt"), "w")
args = map(int, fi.readline().split(' '))
fo.write(func(*args))
fi.close()
fo.close()
