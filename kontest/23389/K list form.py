import os
import sys


def read_data(fi):
    n = int(fi.readline())
    x = fi.readline().rstrip().split(' ')
    k = int(fi.readline())
    return n, x, k


def prepare_lists(n, x, k):
    k = str(k)
    len_k = len(k)
    if n > len_k:
        k = '0' * (n - len_k) + k
    else:
        x = '0' * (len_k - n) + ''.join(x)
    return x, k


def sum_list_num(n, x, k):
    x, k = prepare_lists(n, x, k)
    result = list(x)
    memo = 0
    index = len(k) - 1
    while index >= 0:
        summ = str(int(x[index]) + int(k[index]) + memo)
        if len(summ) > 1:
            result[index] = summ[1]
            memo = int(summ[0])
        else:
            result[index] = summ[0]
            memo = 0
        index -= 1
    if memo:
        result.insert(0, str(memo))
    return ' '.join(result)


current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
fi = open(os.path.join(current_dir, "input.txt"), "r")
fo = open(os.path.join(current_dir, "output.txt"), "w")

args = read_data(fi)
output = sum_list_num(*args)
fo.writelines(output)

fi.close()
fo.close()
