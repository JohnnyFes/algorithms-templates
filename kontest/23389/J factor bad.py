import os
import sys


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


def eratosthenes(n):
    numbers = list(range(n + 1))
    numbers[0] = numbers[1] = False
    for num in range(2, n):
        if numbers[num]:
            for j in range(2 * num, n + 1, num):
                numbers[j] = False
    return numbers


def eratosthenes_effective(n):
    numbers = list(range(n + 1))
    numbers[0] = numbers[1] = False
    for num in range(2, n):
        if numbers[num]:
            for j in range(num * num, n + 1, num):
                numbers[j] = False
    return numbers


def get_least_primes_linear(n):
    lp = [0] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
        for p in primes:
            x = p * i
            if (p > lp[i]) or (x > n):
                break
            lp[x] = p
    return primes, lp


def is_factor(number):
    result = []
    primes = eratosthenes(number)
    if primes[number]:
        return str(number)
    start = 0
    while number > 1:
        for i in range(start, len(primes)):
            prime = primes[i]
            if not prime:
                continue
            if number % prime == 0:
                result.append(prime)
                number = int(number / prime)
                start = i
                if primes[number]:
                    result.append(number)
                    number = 1
                break
    result.sort()
    return ' '.join(str(n) for n in result)


def is_factor2(number):
    result = []
    primes = eratosthenes(number)
    if is_prime(number):
        return str(number)
    start = 2
    while number > 1:
        print(start)
        for i in range(start, len(primes)):
            prime = is_prime(i)
            if not prime:
                continue
            if number % i == 0:
                result.append(i)
                number = int(number / i)
                start = i
                if is_prime(number):
                    result.append(number)
                    number = 1
                break
    result.sort()
    return ' '.join(str(n) for n in result)


def is_factor3(number):
    result = []
    primes = eratosthenes_effective(number)
    if primes[number]:
        return str(number)
    start = 0
    while number > 1:
        for i in range(start, len(primes)):
            prime = primes[i]
            if not prime:
                continue
            if number % prime == 0:
                result.append(prime)
                number = int(number / prime)
                start = i
                if primes[number]:
                    result.append(number)
                    number = 1
                break
    result.sort()
    return ' '.join(str(n) for n in result)


def is_factor4(number):
    result = []
    primes, lp = get_least_primes_linear(number)
    while number > 1:
        result.append(lp[number])
        number = int(number / lp[number])
    result.sort()
    return ' '.join(str(n) for n in result)


def is_factor5(number):
    result = []
    curNum = number
    probe = 2
    while curNum != 1:
        if curNum % probe != 0:
            probe += 1
        else:
            curNum = int(curNum / probe)
            result += [probe]
    return ' '.join(str(n) for n in result)


current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
fi = open(os.path.join(current_dir, "input.txt"), "r")
fo = open(os.path.join(current_dir, "output.txt"), "w")

number = read_data(fi)
output = is_factor5(number)
fo.writelines(output)

fi.close()
fo.close()
