# ID 89369418
import os
import sys
import inspect
from typing import List, Tuple

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"
ERR_INT = 'Ошибка в строке "{}"\nПроверьте входные данные: to_int("{}").'
ERR_VALUE = 'Превышено максимальное значение для "push value": {}'
ERR_DEQUE = 'Превышено максимальное значение размера массива: {}'
ERR_COMMANDS = 'Превышено допустимое количество команд: {}'
ERROR = 'error'
MAX_VALUE = 1000
MAX_DEQUE = 50000
MAX_COMMANDS = 100000


class DequeQueueSized:
    def __init__(self, max_size) -> None:
        self.__queue = [None] * max_size
        self.__max_n = max_size
        self.__head = 0
        self.__tail = 0
        self.__head_back = 0
        self.__tail_back = 0
        self.__size = 0

    def is_empty(self) -> bool:
        return self.__size == 0

    def is_full(self) -> bool:
        return self.__size == self.__max_n

    def size(self) -> int:
        return self.__size

    def push_back(self, item) -> bool:
        if self.is_full():
            return False
        self.__queue[self.__tail_back] = item
        self.__head = self.__tail_back
        self.__tail_back = (self.__tail_back - 1) % self.__max_n
        if self.is_empty():
            self.__tail = (self.__tail + 1) % self.__max_n
        self.__size += 1
        return True

    def push_front(self, item) -> bool:
        if self.is_full():
            return False
        self.__queue[self.__tail] = item
        self.__head_back = self.__tail
        self.__tail = (self.__tail + 1) % self.__max_n
        if self.is_empty():
            self.__tail_back = (self.__tail_back - 1) % self.__max_n
        self.__size += 1
        return True

    def pop_back(self) -> str:
        if self.is_empty():
            raise IndexError
        item = self.__queue[self.__head]
        self.__queue[self.__head] = None
        self.__tail_back = self.__head
        self.__size -= 1
        if self.is_empty():
            self.__tail = self.__tail_back
        else:
            self.__head = (self.__head + 1) % self.__max_n
        return item

    def pop_front(self) -> str:
        if self.is_empty():
            raise IndexError
        item = self.__queue[self.__head_back]
        self.__queue[self.__head_back] = None
        self.__tail = self.__head_back
        self.__size -= 1
        if self.is_empty():
            self.__tail_back = self.__tail
        else:
            self.__head_back = (self.__head_back - 1) % self.__max_n
        return item


def validate_value(item) -> None:
    if abs(item) > MAX_VALUE:
        raise ValueError(ERR_VALUE.format(MAX_VALUE))


def validate_input(cmds_count, queue_len) -> None:
    if queue_len > MAX_DEQUE:
        raise ValueError(ERR_DEQUE.format(MAX_DEQUE))
    if cmds_count > MAX_COMMANDS:
        raise ValueError(ERR_COMMANDS.format(MAX_COMMANDS))


def deque_queue(cmds_count, queue_len, commands) -> List[str]:
    validate_input(cmds_count, queue_len)
    queue = DequeQueueSized(queue_len)
    queue_action = {
        'push_back': queue.push_back,
        'push_front': queue.push_front,
        'pop_back': queue.pop_back,
        'pop_front': queue.pop_front
    }
    result = []
    for command in commands:
        command = command.rstrip()
        push_command = command.split(' ')
        if 'push' in command:
            validate_value(to_int(push_command[1]))
            if not queue_action[push_command[0]](push_command[1]):
                result += f'{ERROR}\n'
        elif 'pop' in command:
            try:
                result += str(queue_action[command]()) + '\n'
            except IndexError:
                result += f'{ERROR}\n'
    return result


def get_filename_in_current_dir(filename) -> str:
    # Одна строка не получается, т.к. по длине по PEP8 не проходит.
    # Именно поэтому сделал через переменную.
    return os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])),
                        filename)


def to_int(string) -> int:
    if not string.lstrip('-').isdigit():
        caller = inspect.getframeinfo(inspect.stack()[1][0])
        message = ERR_INT.format(caller.code_context[0].rstrip(), string)
        sys.exit(message)
    return int(string)


def read_data() -> Tuple[int, int, List[str]]:
    full_filename = get_filename_in_current_dir(INPUT_FILE)

    with open(full_filename, "r") as fi:
        cmds_count = to_int(fi.readline().rstrip())
        queue_len = to_int(fi.readline().rstrip())
        commands = fi.readlines()

    return cmds_count, queue_len, commands


def write_data(data) -> None:
    full_filename = get_filename_in_current_dir(OUTPUT_FILE)

    with open(full_filename, "w") as fo:
        fo.writelines(data)


def main() -> None:
    data = read_data()
    result = deque_queue(*data)
    write_data(result)


if __name__ == '__main__':
    main()
