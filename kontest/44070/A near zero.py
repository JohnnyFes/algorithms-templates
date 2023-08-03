import os
import sys

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def near_zero(count, numbers):
    result = [count] * count
    for i in range(0, count):
        if numbers[i] == '0':
            result[i] = 0

            left = i - 1
            step = 1
            while left >= 0 and numbers[left] != '0':
                if step < result[left]:
                    result[left] = step
                else:
                    break
                step += 1
                left -= 1

            right = i + 1
            step = 1
            while right < count and numbers[right] != '0':
                if step < result[right]:
                    result[right] = step
                else:
                    break
                step += 1
                right += 1

    return ' '.join(map(str, result))


def main():
    current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

    fi = open(os.path.join(current_dir, INPUT_FILE), "r")
    fo = open(os.path.join(current_dir, OUTPUT_FILE), "w")

    count = int(fi.readline())
    numbers = fi.readline().split(' ')

    fo.write(near_zero(count, numbers))

    fi.close()
    fo.close()


if __name__ == '__main__':
    main()
