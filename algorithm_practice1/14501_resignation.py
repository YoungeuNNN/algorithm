n = int(input())
t=[]
p=[]
dp=[]

for i in range(n):
    a,b = map(int,input().split())
    t.append(a)
    p.append(b)
    dp.append(b)

dp.append(0)
for i in range(n-1,-1,-1):
    if i+t[i]>n:
        dp[i] = dp[i+1] #이걸 위해 dp에 미리 append 0
    else:
        dp[i] = max(p[i]+dp[i+t[i]],dp[i+1])

print(dp[0])
