
x1 = int(input("First_coordinate"))
y1 = int(input("Second_coordinate"))
x2 = int(input("coordinate of movement_1"))
y2 = int(input("coordinate of movement_2"))
dx = x1 - x2
dy = y1 - y2
if dx < 0:
    dx *= -1
if dy < 0:
    dy *= -1
if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print(True)
else:
    print(False)
