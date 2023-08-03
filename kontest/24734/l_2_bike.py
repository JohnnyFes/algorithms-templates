import os
import sys
import inspect
from typing import List, Tuple

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"
ERR_INT = 'Ошибка в строке "{}"\nПроверьте входные данные: to_int("{}").'


def find_day(price_by_days, left, right, price):
    if right <= left:
        return -1
    mid = (left + right) // 2
    cur_price = price_by_days[mid]
    if price > cur_price:
        return find_day(price_by_days, mid + 1, right, price)
    elif price <= cur_price:
        day = find_day(price_by_days, left, mid, price)
        return mid + 1 if day == -1 else day


def two_bike(number_days, money_box_by_days, bike_price) -> List[str]:
    result = []
    result += str(find_day(money_box_by_days, 0, len(money_box_by_days), bike_price)) + ' '
    result += str(find_day(money_box_by_days, 0, len(money_box_by_days), bike_price * 2))
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
        number_days = to_int(fi.readline().rstrip())
        money_box_by_days = [to_int(item) for item in fi.readline().rstrip().split()]
        bike_price = to_int(fi.readline().rstrip())

    return number_days, money_box_by_days, bike_price


def write_data(data) -> None:
    full_filename = get_filename_in_current_dir(OUTPUT_FILE)

    with open(full_filename, "w") as fo:
        fo.writelines(data)


def main() -> None:
    data = read_data()
    result = two_bike(*data)
    write_data(result)


if __name__ == '__main__':
    main()
