import random

lst = [random.randint(10, 30) for _ in range(10)]
k = int(input("input number of index >= 0 and <= {}: ".format(len(lst)-1)))
c = int(input("input number"))
lst.append(0)
for i in range(len(lst) - 1, k, -1):
    lst[i] = lst[i - 1]

print(lst)
lst[k] = c
print(lst)