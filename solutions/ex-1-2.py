#!./venv/bin/python3

import math

print("Exercise #1\n")

print("2. Quadratic equation solver\n")

print("please enter coefficients a, b, and c as ax^2 + bx + c = 0")

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

discriminant = b ** 2 - 4 * a * c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)

    floor_root1 = math.floor(root1 * 1000) / 1000
    floor_root2 = math.floor(root2 * 1000) / 1000
    print(f"x = {floor_root1}, {floor_root2}")
elif discriminant == 0:
    root = -b / (2 * a)
    floor_root = math.floor(root * 1000) / 1000
    print(f"x = {floor_root}")
else:
    realPart = -b / (2 * a)
    imaginaryPart = math.sqrt(-discriminant) / (2 * a)

    floor_realPart = math.floor(realPart * 1000) / 1000
    floor_imaginaryPart = math.floor(imaginaryPart * 1000) / 1000
    print(f"x = {floor_realPart} + {floor_imaginaryPart}i, {floor_realPart} - {floor_imaginaryPart}i")
