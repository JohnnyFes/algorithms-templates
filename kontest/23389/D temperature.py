import os
import sys


def read_data(fi):
    n = int(fi.readline())
    temp = list(map(int, fi.readline().split(' ')))
    return n, temp


def get_haos(n, temp):
    days = set()
    if n == 1:
        days.add(n)
    else:
        for i in range(1, n - 1):
            if temp[i + 1] < temp[i] and temp[i - 1] < temp[i]:
                days.add(i + 1)
        if temp[0] > temp[1]:
            days.add(1)
        if temp[n - 1] > temp[n - 2]:
            days.add(n)

    return str(len(days))


current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
fi = open(os.path.join(current_dir, "input.txt"), "r")
fo = open(os.path.join(current_dir, "output.txt"), "w")
days = get_haos(*read_data(fi))
fo.write(days)
fi.close()
fo.close()
