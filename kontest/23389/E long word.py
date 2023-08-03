import os
import sys


def read_data(fi):
    length = int(fi.readline())
    words = fi.readline()[:length].strip().split(' ')
    return words


def get_long(words):
    long_word = ''
    for word in words:
        if len(word) > len(long_word):
            long_word = word
    return long_word, str(len(long_word))


current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
fi = open(os.path.join(current_dir, "input.txt"), "r")
fo = open(os.path.join(current_dir, "output.txt"), "w")
output = get_long(read_data(fi))
fo.writelines('\n'.join(output) + '\n')
fi.close()
fo.close()
