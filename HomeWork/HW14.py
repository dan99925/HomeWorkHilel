import random

print(len(set([random.randint(10, 30) for _ in range(10)]) & set([random.randint(10, 50) for _ in range(20)])))
print()
