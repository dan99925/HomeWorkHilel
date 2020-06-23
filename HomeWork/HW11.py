
size = int(input("number"))
for i in range(size // 2 + 1):
    for j in range(size):
        if i == size // 2 or size // 2 - i == j or j == i + size // 2:
            print('*  ', end ='')
        else:
            print('   ', end='')
    print()
print()

size = int(input("number"))
for i in range(size // 2 + 2):
    for j in range(size):
        if i < size // 2 + 1 and size // 2 - i <= j <= i + size // 2:
            print('*  ', end ='')
        else:
            print('   ', end='')
    print()

print()

size = int(input("number"))
for i in range(size):
    for j in range(size):
        if i < size // 2 + 1 and size // 2 - i <= j <= i + size // 2:
            print('*  ', end='')
        elif i > size // 2 and (j == size - i - 1 + size // 2 or j == size // 2 - (size - i -1)):
            print('*  ', end ='')
        else:
            print('   ', end='')
    print()

print()

size = int(input("number"))
for i in range(size):
    for j in range(size):
        if i < size // 2 + 1 and size // 2 - i <= j <= i + size // 2:
            print('*  ', end='')
        elif i > size // 2 and (j == size - i - 1 + size // 2 or j == size // 2 - (size - i -1)) or j == size // 2:
            print('*  ', end ='')
        else:
            print('   ', end='')
    print()