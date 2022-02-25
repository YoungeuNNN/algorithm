from sys import stdin
from math import gcd

input = stdin.readline
n,s = map(int,input().split())
cor = list(map(int,input().split()))
for i in range(n): #동생의 위치 
    cor[i] = abs(cor[i]-s)
    
g = min(cor)
for i in cor:
    g = gcd(i,g)

print(g)