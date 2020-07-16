
l = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]

# var 1
def result(lst):
    id = lst[0]
    summ = lst[2] * lst[3]
    if summ < 100:
        summ += 10
    return (id, summ)

temp = list(map(lambda y: result(y), l))
print(temp)

# var 2
temp = list(map(lambda y: (y[0], y[2] * y[3] if (y[2] * y[3]) > 100 else (y[2] * y[3]) + 10), l))

print(temp)
