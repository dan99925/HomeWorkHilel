from random import randint
from pprint import pprint

m = 5
matrix = [[randint(1, 50) for _ in range(m)] for _ in range(m)]
temp_ar = [0 for _ in range(m)]


# for row in matrix:
#     for col_ind in range(m):
#         temp_ar[col_ind] += row[col_ind]


def bubble(a, matrix_result=None):
    n = len(a)
    for i in range(n - 1):
        for g in range(n - 1 - i):
            if a[g] > a[g + 1]:
                y = a[g]
                a[g] = a[g + 1]
                a[g + 1] = y
                if matrix_result:
                    for row in matrix_result:
                        k = row[g]
                        row[g] = row[g + 1]
                        row[g + 1] = k
    return a, matrix_result


# _, matrix = bubble(temp_ar, matrix_result=matrix)

for ind in range(m):
    temp_ar = []
    for row_index in range(m):
        temp_ar.append(matrix[row_index][ind])
        temp_ar, _ = bubble(temp_ar)
    if ind % 2 == 0:
        for row_index in range(m):
            matrix[row_index][ind] = temp_ar[row_index]
    else:
        for row_index in range(m):
            matrix[row_index][ind] = temp_ar[m - 1 - row_index]


def view_window(matrix_sum):
    for i in range(len(matrix_sum)):
        for j in range(len(matrix_sum[i])):
            temp_ar[j] += matrix_sum[i][j]
            print('{:>5}'.format(matrix_sum[i][j]), end='')
        print()

    for z in range(len(temp_ar)):
        print('{:>5}'.format(temp_ar[z]), end='')
    print()


print(view_window(matrix))
