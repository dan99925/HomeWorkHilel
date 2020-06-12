
start_value = int(input("Введи число"))

degree = 1
N = 0
while degree * 2 < start_value:
    degree *= 2
    N += 1
print(N, degree)
