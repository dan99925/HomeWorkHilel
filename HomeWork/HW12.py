import random

lst = [random.randint(10, 30) for _ in range(10)]
print(lst)
k = int(input("input number of index"))
for i in range(k + 1, len(lst)):
    lst[i - 1] = lst[i]
lst.pop()
print(lst)
