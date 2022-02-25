from math import gcd
n = int(input())
ans = []


for i in range(n):
    a,b = map(int,input().split())
    ans.append(a*b // gcd(a,b))

for i in ans:
    print(i)
