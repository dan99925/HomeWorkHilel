
size = int(input("number"))
for i in range(size):
    for j in range(size * 2 - 1):
        if i == size - 1 or size - i - 1 == j or j == i + size - 1:
            print('* ', end ='')
        else:
            print('  ', end='')
    print()
print()

size = int(input("number"))
for i in range(size):
    for j in range(size * 2):
        if i < size and size - i - 1 <= j <= i + size - 1:
            print('* ', end ='')
        else:
            print('  ', end='')
    print()

print()

size = int(input("number"))
for i in range(size * 2 - 1):
    for j in range(size * 2 - 1):
        if i < size and size - i <= j + 1 <= i + size:
            print('* ', end='')
        elif i > size // 2 and (j == size * 2 - i - 3 + size or j - 1 == size - (size * 2 - i)):
            print('* ', end ='')
        else:
            print('  ', end='')
    print()

print()

size = int(input("number"))
for i in range(size * 2 - 1):
    for j in range(size * 2 - 1):
        if i < size and size - i <= j + 1 <= i + size:
            print('* ', end='')
        elif i > size // 2 and (j == size * 2 - i - 3 + size or j - 1 == size - (size * 2 - i)) or j == size - 1:
            print('* ', end ='')
        else:
            print('  ', end='')
    print()
