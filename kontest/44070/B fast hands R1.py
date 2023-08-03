# ID 88877845
import os
import sys
import inspect
from typing import List, Tuple

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"
PLAYERS_COUNT = 2
KEYS_COUNT = 9
KEYBOARD_LINES = 4
ERR_INT = 'Ошибка в строке "{}"\nПроверьте входные данные: to_int("{}").'


def to_int(string) -> int:
    if not string.isdigit():
        caller = inspect.getframeinfo(inspect.stack()[1][0])
        message = ERR_INT.format(caller.code_context[0].rstrip(), string)
        sys.exit(message)
    return int(string)


def int_keyboard(keyboard) -> List[List[int]]:
    inted_keyboard = []
    for line in keyboard:
        line = line.replace('.', '0')
        line = list(line)
        line = list(map(to_int, line))
        inted_keyboard += [line]
    return inted_keyboard


def get_keys_games(keyboard) -> Tuple[List[int], int]:
    keys = [0] * (KEYS_COUNT + 1)
    games = 0
    for line in int_keyboard(keyboard):
        for key in line:
            if key:
                keys[key] += 1
            if key > games:
                games = key
    return keys, games


def fast_hands(count, keyboard) -> str:
    result = 0
    keys, games = get_keys_games(keyboard)
    for game in range(1, games + 1):
        if keys[game] and count * PLAYERS_COUNT >= keys[game]:
            result += 1
    return str(result)


def get_filename_in_current_dir(filename) -> str:
    current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    return os.path.join(current_dir, filename)


def read_data() -> Tuple[int, List[str]]:
    full_filename = get_filename_in_current_dir(INPUT_FILE)

    with open(full_filename, "r") as fi:
        count = to_int(fi.readline().rstrip())
        keyboard = list(fi.readline().rstrip() for i in range(0, KEYBOARD_LINES))

    return count, keyboard


def write_data(data) -> None:
    full_filename = get_filename_in_current_dir(OUTPUT_FILE)

    with open(full_filename, "w") as fo:
        fo.write(data)


def main() -> None:
    data = read_data()
    result = fast_hands(*data)
    write_data(result)


if __name__ == '__main__':
    main()
