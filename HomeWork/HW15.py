
# Написать функцию arithmetic, принимающую 3 аргумента:
# первые 2 - числа, третий - операция, которая должна быть произведена над ними.
# Функция должна вернуть результат вычислений зависящий от третьего аргумент +, сложить их; если -,
# то вычесть; * — умножить; / — разделить (первое на второе).
# В остальных случаях вернуть строку "Неизвестная операция".
a = int(input("first number"))
b = int(input("second number"))
c = input("symbo (+, -, *, /)")
def calculation(x, y, symbol):
    if symbol == "+":
        return (x + y)
    elif symbol == "-":
        return (x - y)
    elif symbol == "*":
        return (x * y)
    elif symbol == "/":
        return (x / y)
    else:
        return ("Неизвестная операция")
print(calculation(a, b, c))
