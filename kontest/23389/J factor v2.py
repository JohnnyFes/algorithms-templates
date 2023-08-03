import os
import sys
import math


def read_data(fi):
    number = int(fi.readline())
    return number


def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 1
    return True


def get_dividers(number):
    result = []
    ending = number if number < 10 else round(math.sqrt(number))
    for probe in range(2, ending):
        if number % probe == 0:
            result += [probe]
            result += [int(number / probe)]
    return result


def filter_prime(numbers):
    result = []
    for number in numbers:
        if is_prime(number):
            result += [number]
    return result


def is_factor(number):
    if is_prime(number):
        return str(number)
    deviders = get_dividers(number)
    primes = filter_prime(deviders)
    result = []
    curNum = number
    index = 0
    while curNum != 1:
        if curNum % primes[index] != 0:
            index += 1
        else:
            curNum = int(curNum / primes[index])
            result += [primes[index]]
    return ' '.join(str(n) for n in result)


current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
fi = open(os.path.join(current_dir, "input.txt"), "r")
fo = open(os.path.join(current_dir, "output.txt"), "w")

number = read_data(fi)
output = is_factor(number)
fo.writelines(output)

fi.close()
fo.close()
