# ID 88878258
import os
import sys
import inspect
from typing import List, Tuple

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"
ERR_INT = 'Ошибка в строке "{}"\nПроверьте входные данные: to_int("{}").'


def to_int(string) -> int:
    if not string.isdigit():
        caller = inspect.getframeinfo(inspect.stack()[1][0])
        message = ERR_INT.format(caller.code_context[0].rstrip(), string)
        sys.exit(message)
    return int(string)


def near_zero(count, numbers) -> str:
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
        if numbers[i] == '0':
            zero_index = i
            continue
        if zero_index is not None:
            if result[i] > (zero_index - i):
                result[i] = zero_index - i

    return ' '.join(map(str, result))


def get_filename_in_current_dir(filename) -> str:
    current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    return os.path.join(current_dir, filename)


def read_data() -> Tuple[int, List[str]]:
    full_filename = get_filename_in_current_dir(INPUT_FILE)

    with open(full_filename, "r") as fi:
        count = to_int(fi.readline().rstrip())
        numbers = fi.readline().rstrip().split(' ')

    return count, numbers


def write_data(data) -> None:
    full_filename = get_filename_in_current_dir(OUTPUT_FILE)

    with open(full_filename, "w") as fo:
        fo.write(data)


def main() -> None:
    data = read_data()
    result = near_zero(*data)
    write_data(result)


if __name__ == '__main__':
    main()
