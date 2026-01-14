#!./venv/bin/python3

import math

print("Exercise #2\n")

print("1. Finger-flexing\n")

def f(x):
    return math.exp(-x) - 5 * math.sin(x)

print(f"a) f(5) = {f(5)}")

def sign(number):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0

print(f"b) sign(3) = {sign(3)}, sign(-3) = {sign(-3)}, sign(0) = {sign(0)}")

def mean(a):
    return sum(a) / len(a)

print(f"c) mean([1, 2, 3, 4, 5]) = {mean([1, 2, 3, 4, 5])}")

def meanvar(a):
    m = mean(a)
    variance = sum((x - m) ** 2 for x in a) / len(a)
    return variance

alist = [1, 17, 42]
print(f"d) meanvar({alist}) = {meanvar(alist)}")

