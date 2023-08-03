import os
import sys
from typing import List, Tuple

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


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


def get_filename_in_current_dir(filename) -> str:
    current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    return os.path.join(current_dir, filename)


def read_data() -> Tuple[int, List[str]]:
    full_filename = get_filename_in_current_dir(INPUT_FILE)

    with open(full_filename, "r") as fi:
        string = fi.readline().rstrip()

    return string


def write_data(data) -> None:
    full_filename = get_filename_in_current_dir(OUTPUT_FILE)

    with open(full_filename, "w") as fo:
        fo.writelines(data)


def main() -> None:
    data = read_data()
    result = str(check_seq(data))
    write_data(result)


if __name__ == '__main__':
    main()
