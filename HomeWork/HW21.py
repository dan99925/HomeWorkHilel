
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def lst_revers(x):
    for i in range(len(lst) // 2):
        a = lst[i]
        lst[i] = lst[len(lst) - i - 1]
        lst[len(lst) - i - 1] = a
    return x


print(lst_revers(lst))
# lst1 = [int(item) for item in input("Enter the list items : ").split()]
