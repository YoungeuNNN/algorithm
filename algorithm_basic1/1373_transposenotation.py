from sys import stdin
#// 연산자는 몫을 내림연산한다. 
#a%b 에서 b의 부호를 따라간다.
n = int(stdin.readline())
ans = []
if n == 0:
    ans.append(0)
while n:
    if n%(-2):
        ans.insert(0,abs(n%-2))
        n = n//-2+1
    else:
        ans.insert(0, abs(n % -2))
        n//=-2   

print(*ans,sep='')
    
