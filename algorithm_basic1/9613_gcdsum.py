from sys import stdin
from itertools import combinations
from math import gcd

input = stdin.readline
n = int(input())
ans = []
temp = 0
for _ in range(n):
    comb = list(combinations(list(map(int, input().split()))[1:],2))
    for (a,b) in comb:
        temp += gcd(a,b)
    ans.append(temp)
    temp=0

print(*ans,sep='\n')