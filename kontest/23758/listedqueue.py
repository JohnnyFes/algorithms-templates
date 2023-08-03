import os
import sys
from typing import List, Tuple

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


class ListedQueue:
    def __init__(self) -> None:
        self.size = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.size == 0

    def get(self):
        if self.is_empty():
            return 'error'
        result = self.head.value
        self.head = self.head.next_item
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return result

    def put(self, item):
        if self.tail is None:
            self.tail = Node(item)
            self.head = self.tail
        else:
            self.tail.next_item = Node(item)
            self.tail = self.tail.next_item
        self.size += 1

    def size(self):
        self.size


def list_queue(cmds_count, commands) -> List[str]:
    queue = ListedQueue()
    result = []
    for item in commands:
        item = item.rstrip()
        pushco = item.split(' ')
        if item == 'size':
            result += str(queue.size) + '\n'
        elif item == 'get':
            result += str(queue.get()) + '\n'
        elif pushco[0] == 'put':
            queue.put(int(pushco[1]))
    return result


def get_filename_in_current_dir(filename) -> str:
    current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    return os.path.join(current_dir, filename)


def read_data() -> Tuple[int, List[str]]:
    full_filename = get_filename_in_current_dir(INPUT_FILE)

    with open(full_filename, "r") as fi:
        cmds_count = int(fi.readline().rstrip())
        commands = fi.readlines()

    return cmds_count, commands


def write_data(data) -> None:
    full_filename = get_filename_in_current_dir(OUTPUT_FILE)

    with open(full_filename, "w") as fo:
        fo.writelines(data)


def main() -> None:
    data = read_data()
    result = list_queue(*data)
    write_data(result)


if __name__ == '__main__':
    main()
