import math
#에라토스테네스의 체를 만든다. 
m,n = map(int,input().split())
prime = [True]*(n+1)
prime[0], prime[1] = False, False



for i in range(2,int(math.sqrt(n+1))):
    if prime[i]:
        for j in range(2*i,len(prime),i):
            prime[j] = False
    
for i in range(m,n+1):
    if prime[i]:
        print(i)
