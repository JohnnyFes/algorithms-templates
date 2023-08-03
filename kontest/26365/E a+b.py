import os
import sys


def summ_sort(n, q, k) -> str:
    q.sort()
    left = 0
    right = n - 1
    while left < right:
        cur_sum = q[left] + q[right]
        if cur_sum == k:
            return '{} {}'.format(q[left], q[right])
        if cur_sum > k:
            right -= 1
        else:
            left += 1
    return 'None'


def summ_set(n, q, k) -> str:
    prev = set()
    for number in q:
        iseek = k - number
        if iseek in prev:
            return '{} {}'.format(number, iseek)
        else:
            prev.add(number)
    return 'None'


current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
fi = open(os.path.join(current_dir, "input.txt"), "r")
fo = open(os.path.join(current_dir, "output.txt"), "w")
n, q, k = fi.read().splitlines()
n = int(n)
q = list(map(int, q.split(' ')))
k = int(k)
fo.write(summ_set(n, q, k))
fi.close()
fo.close()
