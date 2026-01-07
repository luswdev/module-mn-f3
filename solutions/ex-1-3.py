#!./venv/bin/python3

import numpy

print("Exercise #1\n")

print("3. Some more finger-flexing with lists and tuples\n")

print("a)")

alist = numpy.arange(4321, 1234, -42)
print(f"last element is {alist[-1]}\n")

print("b)")
blist = alist[::-1]
print(f"last element is {blist[-1]}, length: {len(blist)}\n")

clist = alist.copy()
for i in range(1, 43):
    clist[i - 1] += i

print(f"c) {clist}\n")

dlist1 = [1, 2, 3]
dlist2 = [4, 42, 6]
dlist3 = [7, 8, 9]

list_of_lists = [dlist1, dlist2, dlist3]
print(f"d) {list_of_lists[1][1]}\n")

elist = list(range(10, 18))

# start with 12
elist[2:6] = ['This', 'is', 'absolutely', 'incredible']
elist[-1] = 'impossible'

print(f"e) {elist}\n")
