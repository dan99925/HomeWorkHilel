from string import ascii_uppercase
from string import digits

base = int(input("введите число системы от 2 до 36"))
value = int(input("введите число"))


def convert(x_base, y_value):
    str_map = digits + ascii_uppercase
    result = ''
    while y_value > 0:
        result = str_map[y_value % x_base] + result
        y_value = y_value // x_base
    return result


print(convert(base, value))
