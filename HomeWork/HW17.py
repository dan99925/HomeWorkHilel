a = int(input("введите сторону квадрата"))


def square(length):
    return length ** 2, length * 4, length * (2 ** 1 / 2)


print(square(a))
