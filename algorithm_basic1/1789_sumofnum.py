import sys


#서로 다른 n개의 자연수의 합이 s, 자연수n의 최댓값은?

s = int(input())
sum,n = 0,1


while (1):
    sum += n
    if sum>s:
        break
    n +=1

    
print(n-1)
