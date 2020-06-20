#
# size = int(input("number"))
# for i in range(size):
#     for j in range(size):
#         if i == size // 2 or i == size // 2 - j or j == i + size // 2:
#             print('*  ', end ='')
#         else:
#             print('   ', end='')
#     print()

size = int(input("number"))
for i in range(size):
    for j in range(size):
        if i == size // 2 or i == size // 2 - j or j == i + size // 2:
            print('*  ', end ='')
        else:
            print('   ', end='')
    print()
"""
i > j >= size - i tringle down:
i > j <= size - i tringle left:

"""



# size = int(input("number"))
# for i in range(size):
#     for j in range(size):
#         if i == size // 2 or i == size // 2 - j or j == i + size // 2 or i == size // 2 + j or j == size // 2 - i + size:
#             print('*  ', end ='')
#         else:
#             print('   ', end='')
#     print()




# size = int(input("number"))
# for i in range(size // 2 + 1):
#     for j in range(size):
#         if i == 0 or i == j or j == size - i - 1 or i < j < size - i:
#             print('*  ', end ='')
#         else:
#             print('   ', end='')
#     print()
