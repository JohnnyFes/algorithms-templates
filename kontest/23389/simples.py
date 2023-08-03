import math


def getDividers(number: int):
    result = []
    for probe in range(2, int(math.sqrt(number))):
        if number % probe == 0:
            result += [probe]
            result += [int(number / probe)]
    return result


def getMultipliers(number: int):
    result = []
    curNum = number
    probe = 2
    while curNum != 1:
        if curNum % probe != 0:
            probe += 1
        else:
            curNum = int(curNum / probe)
            result += [probe]
    return result


def main():
    print(getDividers(50000000001))
    print(getMultipliers(500))


main()
