import os
import sys
import inspect
from typing import List, Tuple

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"
ERR_INT = 'Ошибка в строке "{}"\nПроверьте входные данные: to_int("{}").'


def big_first(num1, num2) -> bool:
    # print(num1, num2)
    len_max = max(len(num1), len(num2))
    num1 += '.' * (len_max - len(num1))
    num2 += '.' * (len_max - len(num2))
    for i in range(0, len_max):
        # print(num1[i], num2[i])
        if num1[i] == num2[i]:
            continue
        if num1[i] == '.':
            # print('n1', num1[i-1], num2[i])
            char = num1[i-1]
            for j in range(i, len(num2)):
                # print(char, num2[j])
                if char == num2[j] and j != len(num2) - 1:
                    continue
                # print(char > num2[j])
                return char > num2[j]
        if num2[i] == '.':
            # print('n2', num1[i], num2[i-1])
            char = num2[0]
            for j in range(i, len(num1)):
                # print(char, num1[j])
                if char == num1[j] and j != len(num1) - 1:
                    continue
                # print(char < num1[j])
                return char < num1[j]
        # print(num1[i] > num2[i])
        return num1[i] > num2[i]


def insertion_sort_by_comparator(array, comp):
    for i in range(1, len(array)):
        # print(*array, sep=' ')
        item_to_insert = array[i]
        j = i
        while j > 0 and comp(item_to_insert, array[j-1]):
            array[j] = array[j-1]
            j -= 1
        array[j] = item_to_insert
    # print(*array, sep=' ')
    return ''.join(map(str, array))


def big_number(length, array) -> List[str]:
    return insertion_sort_by_comparator(array, big_first)


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
        length = to_int(fi.readline().rstrip())
        array = fi.readline().rstrip().split()

    return length, array


def write_data(data) -> None:
    full_filename = get_filename_in_current_dir(OUTPUT_FILE)

    with open(full_filename, "w") as fo:
        fo.writelines(data)


def main() -> None:
    data = read_data()
    result = big_number(*data)
    write_data(result)


if __name__ == '__main__':
    main()
