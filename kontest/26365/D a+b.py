import os
import sys


def summ(n, q, k) -> str:
    for i in range(0, n):
        for j in range(i + 1, n):
            if q[i] + q[j] == k:
                return '{} {}'.format(q[i], q[j])
    return 'None'


current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
fi = open(os.path.join(current_dir, "input.txt"), "r")
fo = open(os.path.join(current_dir, "output.txt"), "w")
n, q, k = fi.read().splitlines()
n = int(n)
q = list(map(int, q.split(' ')))
k = int(k)
fo.write(summ(n, q, k))
fi.close()
fo.close()
