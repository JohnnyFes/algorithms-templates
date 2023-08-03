import os
import sys
import inspect
from typing import List, Tuple

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"
ERR_INT = 'Ошибка в строке "{}"\nПроверьте входные данные: to_int("{}").'


def bubble_sort(length, array) -> List[str]:
    result = []
    changed = False
    while not changed:
        for i in range(0, length - 1):
            next_item = array[i + 1]
            if array[i] > next_item:
                array[i + 1] = array[i]
                array[i] = next_item
                changed = True
        if changed or not result:
            result += ' '.join(map(str, array)) + '\n'
        if changed:
            changed = False
        else:
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
        length = to_int(fi.readline().rstrip())
        array = [to_int(item) for item in fi.readline().rstrip().split()]

    return length, array


def write_data(data) -> None:
    full_filename = get_filename_in_current_dir(OUTPUT_FILE)

    with open(full_filename, "w") as fo:
        fo.writelines(data)


def main() -> None:
    data = read_data()
    result = bubble_sort(*data)
    write_data(result)


if __name__ == '__main__':
    main()
