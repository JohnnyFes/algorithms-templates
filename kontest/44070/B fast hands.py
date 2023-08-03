# ID 88848360
import os
import sys

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"
PLAYERS_COUNT = 2
KEYS_COUNT = 9
KEYBOARD_LINES = 4

def key_count(keyboard):
    keys = [0] * (KEYS_COUNT + 1)
    games = 0
    for line in keyboard:
        line = list(map(int, list(line.replace('.', '0'))))
        for key in line:
            if key:
                keys[key] += 1
            if key > games:
                games = key

    return keys, games


def fast_hands(count, keyboard):
    result = 0
    keys, games = key_count(keyboard)
    for t in range(1, games + 1):
        if keys[t] and count * PLAYERS_COUNT >= keys[t]:
            result += 1
    return str(result)


def main():
    current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

    fi = open(os.path.join(current_dir, INPUT_FILE), "r")
    fo = open(os.path.join(current_dir, OUTPUT_FILE), "w")

    count = int(fi.readline())
    keyboard = list(fi.readline().rstrip() for i in range(0, KEYBOARD_LINES))

    fo.write(fast_hands(count, keyboard))

    fi.close()
    fo.close()


if __name__ == '__main__':
    main()
