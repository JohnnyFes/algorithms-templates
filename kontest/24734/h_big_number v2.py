import os
import sys
import inspect
from typing import List, Tuple

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"
ERR_INT = 'Ошибка в строке "{}"\nПроверьте входные данные: to_int("{}").'


def big_first(num1, num2) -> bool:
    return int(num1 + num2) > int(num2 + num1)


def insertion_sort_by_comparator(array, comp):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and comp(item_to_insert, array[j-1]):
            array[j] = array[j-1]
            j -= 1
        array[j] = item_to_insert
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
