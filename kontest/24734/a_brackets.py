import os
import sys
import inspect
from typing import List, Tuple

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"
ERR_INT = 'Ошибка в строке "{}"\nПроверьте входные данные: to_int("{}").'


def check_seq(string) -> str:
    pairs = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    brackets = []
    for char in string:
        if char in '({[':
            brackets += char
        if len(brackets):
            last = brackets[-1]
        else:
            return False
        if char in ')}]':
            if char == pairs[last]:
                brackets.pop()
            else:
                return False
    if len(brackets):
        return False
    else:
        return True


def gen_brackets(length, prefix=''):
    if length == 0:
        if check_seq(prefix):
            print(prefix)
    else:
        gen_brackets(length - 1, prefix + '(')
        gen_brackets(length - 1, prefix + ')')


def brackets(length) -> List[str]:
    result = []
    gen_brackets(length*2)
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

    return length,


def write_data(data) -> None:
    full_filename = get_filename_in_current_dir(OUTPUT_FILE)

    with open(full_filename, "w") as fo:
        fo.writelines(data)


def main() -> None:
    data = read_data()
    result = brackets(*data)
    # write_data(result)


if __name__ == '__main__':
    main()
