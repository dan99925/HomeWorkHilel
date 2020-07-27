from string import ascii_uppercase
from string import digits

str_map = digits + ascii_uppercase
base = int(input("введите число системы от 2 до 36"))
value = int(input("введите число"))
result = ''
while value > 0:
    result = str_map[value % base] + result
    value = value // base

print(result)
