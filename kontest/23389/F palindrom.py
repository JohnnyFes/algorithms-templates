import os
import sys
import re


def read_data(fi):
    line = fi.readline().strip().lower()
    return re.sub(r'\W+', '', line)


def palindrom(line):
    result = True
    length = len(line)
    for i in range(0, int(length / 2)):
        if line[i] != line[length - i - 1]:
            result = False
            break
    return str(result)


current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
fi = open(os.path.join(current_dir, "input.txt"), "r")
fo = open(os.path.join(current_dir, "output.txt"), "w")
output = palindrom(read_data(fi))
fo.writelines(output)
fi.close()
fo.close()
