
x1 = int(input("First_coordinate"))
y1 = int(input("Second_coordinate"))
x2 = int(input(("coordinate of movement_1")))
y2 = int(input(("coordinate of movement_2")))
point1x = x1 - 2
point1y = y1 - 1
point2x = x1 - 1
point2y = y1 - 2
point3x = x1 + 2
point3y = y1 + 1
point4x = x1 + 1
point4y = y1 + 2
point5x = x1 + 2
point5y = y1 - 1
point6x = x1 - 2
point6y = y1 + 1
point7x = x1 - 1
point7y = y1 + 2
point8x = x1 + 1
point8y = y1 - 2
if point1x >= 1 and point1y >= 1 and point1x <= 8 and point1y <= 8 and point1x == x2 and point1y == y2:
    print(True)
elif point2x >= 1 and point2y >= 1 and point2x <= 8 and point2y <= 8 and point2x == x2 and point2y == y2:
    print(True)
elif point3x >= 1 and point3y >= 1 and point3x <= 8 and point3y <= 8 and point3x == x2 and point3y == y2:
    print(True)
elif point4x >= 1 and point4y >= 1 and point4x <= 8 and point4y <= 8 and point4x == x2 and point4y == y2:
    print(True)
elif point5x >= 1 and point5y >= 1 and point5x <= 8 and point5y <= 8 and point5x == x2 and point5y == y2:
    print(True)
elif point6x >= 1 and point6y >= 1 and point6x <= 8 and point6y <= 8 and point6x == x2 and point6y == y2:
    print(True)
elif point7x >= 1 and point7y >= 1 and point7x <= 8 and point7y <= 8 and point7x == x2 and point7y == y2:
    print(True)
elif point8x >= 1 and point8y >= 1 and point8x <= 8 and point8y <= 8 and point8x == x2 and point8y == y2:
    print(True)
else:
    print(False)
