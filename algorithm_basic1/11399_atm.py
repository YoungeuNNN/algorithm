
n=int(input())
p=list(map(int,input().split()))
p = sorted(p)
sum=0

for i in p:
    sum += i*n
    n -=1

print(sum)



