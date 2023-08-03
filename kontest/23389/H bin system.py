import os
import sys


def read_data(fi):
    lines = []
    for line in fi:
        lines.append(line.rstrip())
    len_0 = len(lines[0])
    len_1 = len(lines[1])
    if len_0 > len_1:
        lines[1] = '0' * (len_0 - len_1) + lines[1]
    else:
        lines[0] = '0' * (len_1 - len_0) + lines[0]
    return lines


def sum_binary(n, m):
    summ = ''
    i = len(n) - 1
    memo = 0
    while i >= 0:
        k = int(n[i]) + int(m[i]) + memo
        if k == 3:
            summ = '1' + summ
            memo = 1
        if k == 2:
            summ = '0' + summ
            memo = 1
        if k == 1:
            summ = '1' + summ
            memo = 0
        if k == 0:
            summ = '0' + summ
            memo = 0
        i -= 1
    if memo:
        summ = '1' + summ
    return summ


current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
fi = open(os.path.join(current_dir, "input.txt"), "r")
fo = open(os.path.join(current_dir, "output.txt"), "w")

output = sum_binary(*read_data(fi))
fo.writelines(output)

fi.close()
fo.close()
