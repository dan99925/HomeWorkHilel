# Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.
a = int(input("year"))

def is_year_leap(year):
# високосный год делиться на 4:
    if year % 4 != 0:
        return (False)
    elif year % 100 == 0:
        if year % 400 == 0:
            return (True)
        else:
            return (False)
    else:
        return (True)
print(is_year_leap(a))
