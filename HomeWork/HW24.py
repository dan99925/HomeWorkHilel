from random import randint


rows = 8
cols = 10

lst = [[randint(10, 80) for _ in range(cols)] for _ in range(rows)]
lst_2 = [0 for _ in range(cols)]

for i in range(len(lst)):
    n = 0
    for j in range(len(lst[i])):
        lst_2[j] += lst[i][j]
        print('{:>4}'.format(lst[i][j]), end='')
        n += lst[i][j]
    print('{:>8}'.format(n), end='')
    print()
print()

for z in range(len(lst_2)):
    print('{:>4}'.format(lst_2[z]), end='')
print()