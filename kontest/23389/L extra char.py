import os
import sys


def read_data(fi):
    s = fi.readline().rstrip()
    t = fi.readline().rstrip()
    return s, t


def extra_char(s, t):
    s = list(s)
    t = list(t)
    s.sort()
    t.sort()
    for i in range(0, len(s)):
        if s[i] != t[i]:
            return t[i]
    return t[i + 1]


current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
fi = open(os.path.join(current_dir, "input.txt"), "r")
fo = open(os.path.join(current_dir, "output.txt"), "w")

args = read_data(fi)
output = extra_char(*args)
fo.writelines(output)

fi.close()
fo.close()
