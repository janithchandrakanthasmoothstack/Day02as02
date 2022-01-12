
import sys


inputNumber = int(input("Number? "))
d = dict()
for i in range(1, inputNumber + 1):

    d[i] = i * i

print(d)