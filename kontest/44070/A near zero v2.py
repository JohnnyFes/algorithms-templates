# ID 88847784
import os
import sys

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def near_zero(count, numbers):
    result = []
    zero_index = None
    for i in range(0, count):
        if numbers[i] == '0':
            zero_index = i
            result += [0]
            continue
        if zero_index is not None:
            result += [i - zero_index]
        else:
            result += [count]

    zero_index = None
    for i in reversed(range(0, count)):
        print('|', numbers[i], '|')
        if numbers[i] == '0':
            zero_index = i
            continue
        if zero_index is not None:
            if result[i] > (zero_index - i):
                result[i] = zero_index - i

    return ' '.join(map(str, result))


def main():
    current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

    fi = open(os.path.join(current_dir, INPUT_FILE), "r")
    fo = open(os.path.join(current_dir, OUTPUT_FILE), "w")

    count = int(fi.readline())
    numbers = fi.readline().rstrip().split(' ')

    fo.write(near_zero(count, numbers))

    fi.close()
    fo.close()


if __name__ == '__main__':
    main()
