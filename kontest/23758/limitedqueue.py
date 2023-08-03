import os
import sys
from typing import List, Tuple

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


class MyQueueSized():
    def __init__(self, max_size) -> None:
        self.queue = [None] * max_size
        self.max_n = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, item):
        if self.size != self.max_n:
            self.queue[self.tail] = item
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
            return True
        return False

    def pop(self):
        if self.is_empty():
            return None
        item = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.head]

    def size(self):
        return self.size


def limit_queue(cmds_count, queue_len, commands) -> List[str]:
    queue = MyQueueSized(queue_len)
    result = []
    for item in commands:
        item = item.rstrip()
        pushco = item.split(' ')
        if item == 'size':
            result += str(queue.size) + '\n'
        elif item == 'peek':
            result += str(queue.peek()) + '\n'
        elif item == 'pop':
            result += str(queue.pop()) + '\n'
        elif pushco[0] == 'push':
            if not queue.push(int(pushco[1])):
                result += 'error\n'
    return result


def get_filename_in_current_dir(filename) -> str:
    current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    return os.path.join(current_dir, filename)


def read_data() -> Tuple[int, List[str]]:
    full_filename = get_filename_in_current_dir(INPUT_FILE)

    with open(full_filename, "r") as fi:
        cmds_count = int(fi.readline().rstrip())
        queue_len = int(fi.readline().rstrip())
        commands = fi.readlines()

    return cmds_count, queue_len, commands


def write_data(data) -> None:
    full_filename = get_filename_in_current_dir(OUTPUT_FILE)

    with open(full_filename, "w") as fo:
        fo.writelines(data)


def main() -> None:
    data = read_data()
    result = limit_queue(*data)
    write_data(result)


if __name__ == '__main__':
    main()
