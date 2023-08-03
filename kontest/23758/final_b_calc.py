# ID 89367894
import os
import sys
import inspect
import operator
from typing import Tuple

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"
ERR_INT = 'Ошибка в строке "{}"\nПроверьте входные данные: to_int("{}").'
ERR_STACK = 'Ошибка! Пустой стэк: "{}"\nПроверьте входные данные.'


class Stack:
    def __init__(self) -> None:
        self.__items = []

    def push(self, item) -> None:
        self.__items.append(item)

    def pop(self) -> int:
        self.check_items()
        return self.__items.pop()

    def size(self) -> int:
        return len(self.__items)

    def check_items(self) -> None:
        if self.size() == 0:
            message = ERR_STACK.format(self.__items)
            sys.exit(message)


def calc(expression) -> Tuple[str]:
    action = {
        '-': operator.sub,
        '+': operator.add,
        '*': operator.mul,
        '/': operator.floordiv
    }
    stack = Stack()
    for item in expression:
        if item in '-+*/':
            a = stack.pop()
            b = stack.pop()
            stack.push(action[item](b, a))
        else:
            stack.push(to_int(item))
    return str(stack.pop()),


def get_filename_in_current_dir(filename) -> str:
    current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    return os.path.join(current_dir, filename)


def to_int(string) -> int:
    if not string.lstrip('-').isdigit():
        caller = inspect.getframeinfo(inspect.stack()[1][0])
        message = ERR_INT.format(caller.code_context[0].rstrip(), string)
        sys.exit(message)
    return int(string)


def read_data() -> Tuple[str]:
    full_filename = get_filename_in_current_dir(INPUT_FILE)

    with open(full_filename, "r") as fi:
        expression = fi.readline().rstrip().split(' ')

    return expression,


def write_data(data) -> None:
    full_filename = get_filename_in_current_dir(OUTPUT_FILE)

    with open(full_filename, "w") as fo:
        fo.writelines(data)


def main() -> None:
    data = read_data()
    result = calc(*data)
    write_data(result)


if __name__ == '__main__':
    main()
