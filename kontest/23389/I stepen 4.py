import os
import sys


def read_data(fi):
    number = int(fi.readline())
    return number


def is_four_stepen(number):
    result = True
    while number > 1 and result:
        if number % 4 == 0:
            number = int(number / 4)
        else:
            result = False
    return str(result)


current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
fi = open(os.path.join(current_dir, "input.txt"), "r")
fo = open(os.path.join(current_dir, "output.txt"), "w")

number = read_data(fi)
output = is_four_stepen(number)
fo.writelines(output)

fi.close()
fo.close()
