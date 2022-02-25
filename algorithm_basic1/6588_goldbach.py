import sys
num = 1000000
isprime = [True]*num
for i in range(2, int((num)**0.5)+1):#에라토스테네스 체 만들기
    if isprime[i]:
        for j in range(i*2,num,i):
            isprime[j] = False

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    
    flag = 0

    for i in range(3, len(isprime)):
        if isprime[i] and isprime[n-i]:
            print(str(n)+" = "+str(i)+" + "+str(n-i))
            flag=1
            break
    if flag==0:
        sys.stdout.write("Goldbach's conjecture is wrong.")
    
