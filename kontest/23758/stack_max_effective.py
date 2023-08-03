import os
import sys
from typing import List, Tuple

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


class Stack:
    def __init__(self):
        self.items = []
        self.max = []

    def push(self, item):
        self.items.append(item)
        if len(self.max):
            self.max.append(max(self.max[-1], item))
        else:
            self.max.append(item)

    def pop(self):
        item = self.items.pop()
        self.max.pop()
        return item

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def get_max(self):
        return self.max[-1]


def stack_max(count, commands) -> List[str]:
    stack = Stack()
    result = []
    for item in commands:
        item = item.rstrip()
        if item == 'get_max':
            if stack.size() > 0:
                result += str(stack.get_max()) + '\n'
            else:
                result += 'None\n'
            continue
        if item == 'pop':
            if stack.size() > 0:
                stack.pop()
            else:
                result += 'error\n'
            continue
        pushco = item.split(' ')
        if pushco[0] == 'push':
            stack.push(int(pushco[1]))
    return result


def get_filename_in_current_dir(filename) -> str:
    current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    return os.path.join(current_dir, filename)


def read_data() -> Tuple[int, List[str]]:
    full_filename = get_filename_in_current_dir(INPUT_FILE)

    with open(full_filename, "r") as fi:
        count = int(fi.readline().rstrip())
        commands = fi.readlines()

    return count, commands


def write_data(data) -> None:
    full_filename = get_filename_in_current_dir(OUTPUT_FILE)

    with open(full_filename, "w") as fo:
        fo.writelines(data)


def main() -> None:
    data = read_data()
    result = stack_max(*data)
    write_data(result)


if __name__ == '__main__':
    main()
