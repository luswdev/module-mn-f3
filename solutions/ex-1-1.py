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
print(f"[i] cube: {pow(int(input_num), 3)}, square: {math.pow(int(input_num), 2)}\n")

str1 = input("please enter first string...")
str2 = input("please enter second string...")
print(f"[ii] {str1 + str2}\n")

answers = [1, 17, 42]
check_num = input("please enter a number to check...")

check_res = int(check_num) in answers
print(f"[i] {check_res}\n")
