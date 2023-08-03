import os
import sys
import inspect
from typing import List, Tuple

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"
ERR_INT = 'Ошибка в строке "{}"\nПроверьте входные данные: to_int("{}").'


def merge_flowerbed(a, b):
    print(a, b)
    if (a[0] - b[0]) * (a[1] - b[1]) < 0 or (a[0] <= b[0] and a[1] <= b[1]):
        result = [min(a[0], b[0]), max(a[1], b[1])]
        return result


def merge_sort(array):
    if len(array) == 1:
        return array
    left = merge_sort(array[0 : len(array) // 2])
    right = merge_sort(array[len(array) // 2: len(array)])
    result = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        merged = merge_flowerbed(left[l], right[r])
        if merged:
            result += merged
            l += 1
            r += 1
            continue
        if left[l] <= right[r]:
            result += left[l]
            l += 1
        else:
            result += right[r]
            r += 1

    while l < len(left): 
        result += left[l]
        l += 1
    while r < len(right):
        result += right[r]
        r += 1

    return result


def flowerbed(array) -> List[str]:
    result = []
    array = list(filter(lambda x: x is not None, merge_sort(array)))
    for item in array:
        result += ' '.join(list(map(str, item))) + '\n'
    return result


def get_filename_in_current_dir(filename) -> str:
    return os.path.join(
        os.path.dirname(os.path.abspath(sys.argv[0])),
        filename
    )


def to_int(string) -> int:
    if not string.lstrip('-').isdigit():
        caller = inspect.getframeinfo(inspect.stack()[1][0])
        message = ERR_INT.format(caller.code_context[0].rstrip(), string)
        sys.exit(message)
    return int(string)


def read_data() -> Tuple[int, List[int], int]:
    full_filename = get_filename_in_current_dir(INPUT_FILE)

    with open(full_filename, "r") as fi:
        number = to_int(fi.readline().rstrip())
        array = []
        for i in range(0, number):
            array += [[to_int(item) for item in fi.readline().rstrip().split()]]

    return array,


def write_data(data) -> None:
    full_filename = get_filename_in_current_dir(OUTPUT_FILE)

    with open(full_filename, "w") as fo:
        fo.writelines(data)


def main() -> None:
    data = read_data()
    result = flowerbed(*data)
    write_data(result)


if __name__ == '__main__':
    main()
