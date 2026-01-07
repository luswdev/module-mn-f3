#!./venv/bin/python3

import math

print("Exercise #1\n")

print("1. Finger-flexing\n")

print("a)")
numerator = pow(42, 3) + 17
denominator = (3 / 8) - pow(14, (1 / 2))

print(f"[i] {numerator / denominator}")

step1 = math.tan(0.524)
step2 = pow(step1, math.log(18))
step3 = math.cos(step2)
step4 = math.sin(step3)
final = math.sqrt(step4)

print(f"[ii] {final}")

print("\nb)")

input_num = input("please enter a number...")
print(f"[i] cube: {pow(int(input_num), 3)}, square: {math.pow(int(input_num), 2)}")

