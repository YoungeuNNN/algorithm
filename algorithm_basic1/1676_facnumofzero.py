import math
import sys

n = int(sys.stdin.readline())
fac = str(math.factorial(n))
c = 0

for i in fac[::-1]:
    if i == '0':
        c +=1
    else:
        break

print(c)
