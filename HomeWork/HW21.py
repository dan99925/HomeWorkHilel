
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(lst) // 2):
    tmp = lst[i]
    lst[i] = lst[len(lst) - i - 1]
    lst[len(lst) - i - 1] = tmp
    lst = list(lst)
print(lst)
