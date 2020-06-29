
# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12),
# и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).
a = int(input("введите номер месяца"))
def month(season):
    if season in (1, 2, 12):
        return ("зима")
    elif season in range(3, 6):
        return ("весна")
    elif season in range(6, 9):
        return ("лето")
    elif season in range(9, 11):
        return ("осень")
    else:
        return ("не верно введено число")
print(month(a))