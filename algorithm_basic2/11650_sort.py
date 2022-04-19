import sys
input = sys.stdin.readline
n = int(input())

arr=[]
for i in range(n):
    arr.append(input().split())

arr.sort()
for i in arr:
    print(i[0],i[1])
    
