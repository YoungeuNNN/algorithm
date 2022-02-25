from sys import stdin

n = int(stdin.readline())
ans = []

if n ==1 : 
    print('')

for i in range(2,n+1):
    if n%i == 0:
        while n%i == 0:
            ans.append(i)
            n = n/i

print(*ans,sep='\n')

